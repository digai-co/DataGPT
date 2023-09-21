from datagpt.config import config
from datagpt.tool.db import db


class FetchData:
    def __init__(self):
        self.db = db

    def fetch(self, sql: str):
        return self.db.run(sql)
