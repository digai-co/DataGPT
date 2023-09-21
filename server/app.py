import sys, os

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))))


import json
import gradio as gr

from datagpt.datagpt import DataGPT

# Config Mode: Genrating echart option config directly
# Function Mode:Generating option render function which be called to generate option config
render_mode = "Config"
datagpt = DataGPT()


def search(prompt):
    if prompt == "error":
        raise gr.Error("Error!")
    sql, data, chart = datagpt.run(prompt, render_mode)
    return render_chart(sql, data, chart)


def reexcute_sql(prompt, sql):
    sql, data, chart = datagpt.run_sql(prompt, sql, render_mode)
    return render_chart(sql, data, chart)


def render_chart(sql, data, chart):
    if sql == "BeyondError":
        raise gr.Error("Unable to generate SQL statement, please ask in another way!")
    elif data == "SqlError":
        return [
            sql,  # SQL statement
            gr.update(visible=True),
            "",  # chart iframe
            "",  # chart source code
            "",  # data table
            [
                {
                    "": "",
                    "SQL execution encountered an error, You can modify it below and execute it again.": "red",
                },
            ],
            gr.Highlight.update(visible=True),
        ]
    else:
        chart_iframe, chart_source_code = gen_chart_iframe(chart, json.dumps(data))
        return [
            sql,  # SQL statement
            gr.update(visible=True),  # sql data result
            chart_iframe,  # chart iframe
            chart_source_code,  # chart source code
            gen_table_iframe(data),  # data table
            [],
            gr.Highlight.update(visible=False),
        ]


def gen_chart_iframe(echart_option, result_data):
    html = ""
    # Solution 1: Fill with AI-generated Options
    if render_mode == "Config":
        echart_option = json.loads(echart_option.encode("utf-8"))
        echart_option = echart_option["option"]

        html = """
<head>
    <title>DataGPT</title>
        <script src="https://cdn.jsdelivr.net/npm/echarts@5.4.1/dist/echarts.min.js"></script>
</head>
    <body>
        <div id="main" style="width: 100%;height:350px;"></div>
            <script>
                var chart = echarts.init(document.getElementById("main"));
                var option = {option}   
                chart.setOption(option);
            </script>
    </body>
            """
        html = html.format(option=json.dumps(echart_option))

    # Solution 2: Using AI-generated dynamic functions combined with real data to dynamically generate options
    elif render_mode == "Function":
        html = """
<head>
    <title>DataGPT</title>
        <script src="https://cdn.jsdelivr.net/npm/echarts@5.4.1/dist/echarts.min.js"></script>
</head>
<body>
        <div id="main" style="width: 100%;height:350px;"></div>
            <script>
                var chart = echarts.init(document.getElementById("main"));
                {generate_option}
                var sql_result = {result_data}
                var option = generateOption(sql_result);  
                console.log(JSON.stringify(option));
                chart.setOption(option);
            </script>
</body>
            """
        html = html.format(generate_option=echart_option, result_data=result_data)

    return [
        f"""<iframe style="width: 100%; height: 400px" srcdoc='{html}'></iframe>""",
        f"""```html{html}""",
    ]


def gen_table_iframe(data):
    html = """
<head>
</head>
<body>
  <table style="width:100%; border-radius:10px; border:#eee 1px solid; border-spacing:0px; border-collapse:separate; font-size:13px; font-family:Arial;">
    <tr style="background-color:transparent; border:0; height:40px">
        {tds}
    </tr>
    {trs}   
  </table>
</body>
"""
    tds_html = ""
    trs_html = ""
    columns = data[0]

    # render headers
    for col in columns:
        td = """<td style="padding-left:10px;"><strong>{value}<strong></td>"""
        td = td.format(value=str(col))
        tds_html += td

    # render rows
    if len(data) >= 1:
        data = data[1:]
        index = 0
        for row in data:
            tr = """
                <tr style="background-color:{bg_color};border:0;height:40px;">
                    {tds}
                </tr>"""

            bg_color = ""
            if index % 2 == 1:
                bg_color = "transparent"
            else:
                bg_color = "#f9fafb"

            tds = ""
            for col in row:
                td = """<td style="padding-left:10px;">{value}</td>"""
                td = td.format(value=str(col))
                tds += td
            tr = tr.format(tds=tds, bg_color=bg_color)
            trs_html += tr
            index += 1

    html = html.format(tds=tds_html, trs=trs_html)
    return (
        f"""<iframe style="width: 100%; min-height: 640px" srcdoc='{html}'></iframe>"""
    )


def change_mode(mode):
    global render_mode
    render_mode = mode
    if mode == "Config":
        return gr.update(info="Config Mode: Genrating echart option config directly")
    elif mode == "Function":
        return gr.update(
            info="Function Mode:Generating option render function which be called to generate option config"
        )


def launch_app():
    chart_iframe = gr.HTML("Chart")
    chart_source_code = gr.Markdown("Chart source code")

    with gr.Blocks(title="DataGPT", css="label {font-size:12px}") as ui:
        gr.Markdown(
            """
            # DataGPT
            AI Agent for Natural Language Queries to Generate Charts from a Database.
            """
        )

        with gr.Row():
            with gr.Column(scale=2):
                input_prompt = gr.Textbox(
                    value="What are the specific grades of each student in each course?",
                    label="Question",
                    placeholder="Please input question",
                )
                radio = gr.Radio(
                    choices=["Config", "Function"],
                    type="value",
                    value="Config",
                    label="Render Mode",
                    info="Option Config Mode:Genrating echart option config directly",
                )
                btn = gr.Button(value="Submit", variant="primary")
                error_info = gr.HighlightedText(
                    label="",
                    visible=False,
                    combine_adjacent=True,
                    show_legend=True,
                    color_map={
                        "SQL execution encountered an error, You can modify it below and execute it again.": "red"
                    },
                )
                lbl_sql = gr.Code(
                    value="The sql will be displayed here.",
                    language="markdown",
                    interactive=True,
                    lines=1,
                )
                btn_exe_sql = gr.Button(
                    value="Modify and Re-execute the SQL Statement",
                    size="sm",
                    visible=False,
                )
            with gr.Column(scale=2):
                demo = gr.TabbedInterface(
                    [chart_iframe, chart_source_code], ["Chart", "Source Code"]
                )
        with gr.Row():
            table_iframe = gr.HTML("")

        radio.change(change_mode, inputs=[radio], outputs=[radio])
        btn.click(
            search,
            inputs=input_prompt,
            outputs=[
                lbl_sql,
                btn_exe_sql,
                chart_iframe,
                chart_source_code,
                table_iframe,
                error_info,
                error_info,
            ],
        )
        btn_exe_sql.click(
            reexcute_sql,
            inputs=[input_prompt, lbl_sql],
            outputs=[
                lbl_sql,
                btn_exe_sql,
                chart_iframe,
                chart_source_code,
                table_iframe,
                error_info,
                error_info,
            ],
        )
        ui.launch(share=True)


launch_app()
