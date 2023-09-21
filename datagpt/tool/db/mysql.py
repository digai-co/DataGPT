from typing import Iterable, List
from datagpt.tool.db.base import RDBMS, FieldInfo, TableInfo

from urllib.parse import urlparse
import mysql.connector

from datagpt.log import logger


class MySQL(RDBMS):
    def __init__(self, uri: str):
        self._uri = uri

        o = urlparse(uri)
        config = {
            "host": o.hostname,
            "port": o.port,
            "user": o.username,
            "password": o.password,
            "database": o.path[1:],
        }

        self._conn = mysql.connector.connect(**config)

    def get_type(self) -> str:
        return "MySQL"

    def get_tables(self) -> Iterable[TableInfo]:
        cur = self._conn.cursor()
        cur.execute(
            """
            SELECT table_name, table_comment
            FROM information_schema.tables
            WHERE table_schema = DATABASE();
        """
        )
        tb_infos = cur.fetchall()
        cur.close()

        return [TableInfo(name, comment) for name, comment in tb_infos]

    def get_fields(
        self, table_name: str, schema: str = "public"
    ) -> Iterable[FieldInfo]:
        cur = self._conn.cursor()
        cur.execute(
            """
            SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, COLUMN_DEFAULT, IS_NULLABLE, COLUMN_COMMENT
            FROM information_schema.columns
            WHERE table_schema = DATABASE() AND table_name = %s
            ORDER BY ORDINAL_POSITION;
        """,
            (table_name,),
        )
        fields = cur.fetchall()
        cur.close()

        return [
            FieldInfo(name, type, length, default, nullable, comment)
            for name, type, length, default, nullable, comment in fields
        ]

    def run(self, command: str) -> List:
        try:
            cur = self._conn.cursor()
            cur.execute(command)
            rows = cur.fetchall()
            cols = cur.description
            rows.insert(0, tuple([col[0] for col in cols]))
            return rows
        except Exception as e:
            logger.error("run sql error: " + str(e))
            return "SqlError"
        finally:
            cur.close()
