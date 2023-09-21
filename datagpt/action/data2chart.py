from datagpt.tool.llm_openai import OpenAI
from datagpt.log import logger
import json


# Plan 1: Stable output of config configuration
DATA2CHART_PROMPT_CONFIG = """

## Description
You are a JS engineer proficient in the latest "EChart" framework, responsible for converting data into EChart charts. If the requirement cannot produce content in the appropriate format, please return directly: "ChartError".

My original question was to your "Requirement"
SQL Result comes from the SQL query and is given to you in the task to be solved at the end of this paragraph.

In order to correctly render the results into the EChart chart, please carefully analyze the core query target and SQL Result of the original question.

First, based on the requirements, original question, and the resulting data, consider the following 6 points to analyze which chart type is more suitable:

The range of chart types includes (in order of priority):

1.Gauge chart (if there is only one data point in the array, prioritize using a gauge chart).
2.Pie chart (if the original question involves querying proportions or percentages, prioritize using a pie chart).
3.Radar chart (if the data has a single dimension and the number of data points is <= 6, prioritize generating a radar chart. In this case, the series' data array should contain only one object that includes all the values, and generate a matching indicator array based on the data in the series).
4.Line chart.
5.Scatter plot.
6.Multi-series bar chart (if there are multiple series in the array, prioritize using a bar chart. Additionally, if none of the above 1-5 situations apply, use a bar chart).
If the conditions stated in the parentheses above are met, the corresponding type of graph should be chosen as a priority.

Return all numerical values with a maximum precision of two decimal places.
Next, you can optimize the format of the "result" field, adjusting it to the data structure that you believe is most suitable for rendering the chart of the previously determined TYPE. You can replace the fields as needed.

Then, based on the optimized "result" field, provide me with the complete JS code for the options parameter required by ECharts in the setOption function, ensuring that all dimension axes and titles meet the requirements of the original problem.

You should strictly return three items to me in the following order, adhering to the specific requirements for each field as mentioned in the comments of the JSON format.
The optimized "result" field.
The correct parameters required in the options used for rendering, including: x (corresponding to the field name of the x-axis), y (corresponding to the field name of the y-axis), names of the x-axis and y-axis, title, tooltip, etc. Please do not disclose any other code or comments to me.
The final data format you return should strictly adhere to the following requirements for JSON format. The number of elements in the array should match the number returned by the API, and there should be no additional descriptive text included.
{{
     "result" :{{
           "a":["value1"],
           "b":["value2"]
      }},
     "option":{{
                "type":TYPE,
                "color":["#95a5fd", "#fd7f82", "#fec077", "#fee77d", "#95e38f", "#37bbff", "#74b6ff", "#d09dff","#444547"],
                "grid": {{
                    "top": "10%"
                }},
                "title": {{
                    "text": "XXX",//Replace the original question with more appropriate and concise wording.
                    "left": "center"
                }},
                "legend": {{
                    "orient": "horizontal",
                    "top": "bottom"
                }}
                "xAxis": //only exists when TYPE is bar or lines
                {{
                    "data": [...],//you should realize a function to put all item's name into the array when type is bar or lines
                    "axisLabel": {{
                        "rotate": XXX,//If the number of data points is less than 5, set the value to 0. If it is less than 10, set the value to 30. If it is greater than 15, set the value to 45.
                        "interval": 0
                    }},
                    "show":bool//set true when TYPE is bar or lines.others set false
                }},
                "yAxis": {{}},//only exists when TYPE is bar or lines.
                "series": [{{
                    "name": "Title Based on Your Understanding",
                    "type": TYPE,
                    "radius": "40%",//(gauge:80%,other:40%)                   
                   
                    "data(only exists when TYPE is radar)":
                    [
                        //Only this ONE object exists if TYPE is radar.
                        {{
                            "name":"",
                            "value":number1,number2,...,numberN  // Put all values in the array if TYPE is radar.
                        }}
                        //No more objects! if TYPE is radar
                    ]

                }},{{}}],
                "radar"://only exists when TYPE is radar 
                {{
                    "indicator":
                    [
                        {{
                            "name":"series[0].name",
                            "max":MAX//Retrieve the maximum value from the 'value' array inside the 'series.data' automatically.
                        }},{{
                            "name":"series[1].name",
                            "max":MAX//Ensure that the MAX value equals the previous MAX value
                        }}……
                    ]
                }}
        }}
}}

## Examples
Requirement: Proportion of the area occupied by the top 6 parking spaces in terms of total area.
SQL Result：[["space_name", "space_area"], ["MUJI无印良品", 200.0], ["优衣库", 140.0], ["105", 50.0], ["奈雪の茶", 40.0], ["103", 35.0], ["机房", 35.0]]
Result: {{}}

Requirement: Empty data or data with excessively high dimensions
SQL Result:empty or error format
Result: ChartError

## Task to solve
Requirement: {requirement}
SQL Result：{result}
Result:
"""


# plan2: More aggressive dynamic function configuration
DATA2CHART_PROMPT_FUNCTION = """

## Description
You are a JS engineer proficient in the latest "EChart" framework, responsible for converting data into EChart charts. If the requirement cannot produce content in the appropriate format, please return directly: "ChartError".

My original question was to your "Requirement"
SQL Result comes from the SQL query and is given to you in the task to be solved at the end of this paragraph.
In order to correctly render the results into the EChart chart, please carefully analyze the core query target and SQL Result of the original question.

First, based on the requirements, original question, and the resulting data, consider the following 6 points to analyze which chart type is more suitable:

The range of chart types includes (in order of priority):

1.Gauge chart (if there is only one data point in the array, prioritize using a gauge chart).
2.Pie chart (if the original question involves querying proportions or percentages, prioritize using a pie chart).
3.Radar chart (if the data has a single dimension and the number of data points is <= 6, prioritize generating a radar chart. In this case, the series' data array should contain only one object that includes all the values, and generate a matching indicator array based on the data in the series).
4.Line chart.
5.Scatter plot.
6.Multi-series bar chart (if there are multiple series in the array, prioritize using a bar chart. Additionally, if none of the above 1-5 situations apply, use a bar chart).
If the conditions stated in the parentheses above are met, the corresponding type of graph should be chosen as a priority.

Then, you can optimize the format of the 'result' field and adjust it to the data structure that you consider most suitable for rendering the chart of the type determined in the previous step. You can use '...' to indicate the omission of a large amount of data content. You can replace the fields as needed.
Next, based on the optimized 'result' field, please provide me with the complete dynamic JavaScript function that is required to generate the 'option' JSON string parameter for the setOption method in ECharts. In other words, I need you to return dynamic JS code. The requirements for this code are as follows:

1.The first parameter is SQL Result, and in the provided code, this result needs to be dynamically transformed into key data required for various parameters in the options.
2.The type field, which represents the table type, should be defined at the beginning of the function. Determine the specific type based on the above requirements, and directly use this type within the following JSON.
3.The algorithm supports multiple series to ensure that the chart can display the complete data when it comes in.
4.You only return the function code. Once the code is returned, please immediately stop answering.
5.The returned result must adhere to the JSON format required by ECharts options to ensure the complete rendering of the chart.
6.The XXX characters in the JSON example below need to be replaced with the most appropriate content based on your understanding of the requirements.
7.For specific requirements of each field in the returned option, please refer to the comments in the JSON format requirements below.
8.The data format returned by this function must strictly adhere to the following JSON format requirements, and the number of elements in the array should be the same as the data quantity returned by the API (i.e., consistent with the data volume of the first parameter of this function):
{{
                "type":TYPE,
                "color":["#95a5fd", "#fd7f82", "#fec077", "#fee77d", "#95e38f", "#37bbff", "#74b6ff", "#d09dff","#444547"],
                "grid": {{
                    "top": "10%"
                }},
                "title": {{
                    "text": "XXX",//Replace the original question with more appropriate and concise wording.
                    "left": "center"
                }},
                "legend": {{
                    "orient": "horizontal",
                    "top": "bottom"
                }}
                "xAxis": //only exists when TYPE is bar or lines
                {{
                    "data": [...],//you should realize a function to put all item's name into the array when type is bar or lines
                    "axisLabel": {{
                        "rotate": XXX,//If the number of data points is less than 5, set the value to 0. If it is less than 10, set the value to 30. If it is greater than 15, set the value to 45.
                        "interval": 0
                    }},
                    "show":bool//set true when TYPE is bar or lines.others set false
                }},
                "yAxis": {{}},//only exists when TYPE is bar or lines.
                "series": [{{
                    "name": "Title Based on Your Understanding",
                    "type": TYPE,
                    "radius": "40%",//(gauge:80%,other:40%)                   
                   
                    "data(only exists when TYPE is radar)":
                    [
                        //Only this ONE object exists if TYPE is radar.
                        {{
                            "name":"",
                            "value":[number1,number2,...,numberN]//Put all values in the array if TYPE is radar.
                        }}
                        //No more objects! if TYPE is radar
                    ]

                }},{{}}],
                "radar"://only exists when TYPE is radar 
                {{
                    "indicator":
                    [
                        {{
                            "name":"series[0].name",
                            "max":MAX//Retrieve the maximum value from the 'value' array inside the 'series.data' automatically.
                        }},{{
                            "name":"series[1].name",
                            "max":MAX//Ensure that the MAX value equals the previous MAX value
                        }}……
                    ]
                }}
}}


## Examples
Requirement: Proportion of the area occupied by the top 6 parking spaces in terms of total area.
Sql Result:[["space_name", "space_area"], ["nameAA", 200.0], ……, ["nameYY", 35.0], ["nameZZ", 35.0]]
Result: 
function generateOption(apiResultList){{
    var option= {{}};// Initialization of the entire options content, it must be in JSON format.
    var type = "pie";//Here, the comment explains the reasons for choosing the chart type.
    //This is the specific algorithm to break down the apiResultList data.
    //Here is the complete content that meets the requirements of the option:
    //1、build option basic structure by template before
    //2、filling all the titles and data by a dynamic function
    //3、check the option again and promise it works currectly
    return option;
}}
//NO Note!

Requirement: An illogical question
Sql Result:Empty data or data with excessively high dimensions
Result: ChartError
//NO Note!

## Task to solve
Requirement: {requirement}
Sql Result:{result}
Result:
"""


class Data2Chart:
    def __init__(self):
        self.llm = OpenAI()

    def gen_chart(self, requirement: str, result: list, render_mode: str) -> str:
        if render_mode == "Config":
            result = json.dumps(result)
            prompt = DATA2CHART_PROMPT_CONFIG.format(
                requirement=requirement, result=result
            )
        elif render_mode == "Function":
            # TODO:Provide fewer data samples and allow AI to know the format based on limited data
            # if len(result) >= 3:
            #     result = [result[0],result[1],result[-1]]
            result = json.dumps(result)
            prompt = DATA2CHART_PROMPT_FUNCTION.format(
                requirement=requirement, result=result
            )

        return self.llm.ask(prompt)
