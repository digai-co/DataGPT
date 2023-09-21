from datagpt.action import text2sql, fetch_data, data2chart
from datagpt.log import logger


class DataGPT:
    def __init__(self):
        self.text2sql = text2sql.Text2SQL()
        self.fetchdata = fetch_data.FetchData()
        self.data2chart = data2chart.Data2Chart()

    def run(self, text: str, render_mode: str):
        """from text to chart"""

        logger.debug(f"input text: {text}")
        sql = self.text2sql.gen_sql(text)
        if sql == "BeyondError":
            return sql, None, None

        logger.debug(f"generated sql: {sql}")
        return self.__excute_sql(sql, text, render_mode)

    def run_sql(self, text: str, sql: str, render_mode: str):
        """from sql to chart"""

        logger.debug(f"input sql: {sql}")
        return self.__excute_sql(sql, text, render_mode)

    def __excute_sql(self, sql, text, render_mode):
        data = self.fetchdata.fetch(sql)
        if data == "SqlError":
            return sql, data, None

        logger.debug(f"fetched data: {data}")
        chart = self.data2chart.gen_chart(text, data, render_mode)
        logger.debug(f"rendered chart: {chart}")

        return sql, data, chart
