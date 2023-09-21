from typing import Iterable, List

from psycopg_pool import ConnectionPool

from datagpt.tool.db.base import RDBMS, FieldInfo, TableInfo
from datagpt.log import logger


class PostgreSQL(RDBMS):
    def __init__(self, uri: str):
        self._pool = ConnectionPool(uri)

    def get_type(self) -> str:
        return "PostgreSQL"

    def get_tables(self) -> Iterable[TableInfo]:
        with self._pool.connection() as conn:
            with conn.cursor() as cur:
                tb_infos = cur.execute(
                    """
                    SELECT tb.table_name, d.description
                    FROM information_schema.tables tb
                        LEFT JOIN pg_namespace b ON b.nspname = tb.table_schema
                        LEFT JOIN pg_class c ON c.relname = tb.table_name AND c.relnamespace = b.oid
                        LEFT JOIN pg_description d ON d.objoid = c.oid AND d.objsubid = '0'
                    WHERE tb.table_schema = 'public' and tb.table_type = 'BASE TABLE';
                """
                ).fetchall()
                return [TableInfo(name, comment) for name, comment in tb_infos]

    def get_fields(
        self, table_name: str, schema: str = "public"
    ) -> Iterable[FieldInfo]:
        with self._pool.connection() as conn:
            with conn.cursor() as cur:
                fields = cur.execute(
                    """
                    SELECT
                        c.column_name,
                        c.udt_name,
                        character_maximum_length,
                        c.column_default,
                        c.is_nullable,
                        pgd.description AS column_comment
                    FROM
                        information_schema.columns c
                    LEFT JOIN
                        pg_catalog.pg_description pgd ON pgd.objoid = (select oid from pg_class where relnamespace=(select oid from pg_namespace where nspname=%(schema)s) and relname=%(table)s) AND pgd.objsubid = c.ordinal_position
                    WHERE
                        c.table_schema = %(schema)s AND c.table_name = %(table)s
                    ORDER BY
                        c.ordinal_position;
                """,
                    {"table": table_name, "schema": schema},
                ).fetchall()

                return [
                    FieldInfo(name, type, length, default, nullable, comment)
                    for name, type, length, default, nullable, comment in fields
                ]

    def run(self, command: str) -> List:
        try:
            with self._pool.connection() as conn:
                with conn.cursor() as cur:
                    rows = cur.execute(command).fetchall()
                    cols = cur.description
                    rows.insert(0, tuple([col.name for col in cols]))
                    return rows
        except Exception as e:
            logger.error("run sql error: " + str(e))
            return "SqlError"
