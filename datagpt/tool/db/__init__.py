from datagpt.config import config
from datagpt.log import logger
from datagpt.tool.db.mysql import MySQL
from datagpt.tool.db.postgres import PostgreSQL


def get_db():
    db_type = config.get("database.type")
    db_uri = config.get("database.uri")
    if db_type == "postgresql":
        return PostgreSQL(db_uri)
    elif db_type == "mysql":
        return MySQL(db_uri)
    else:
        logger.exception("No vaild database config")


db = get_db()

__all__ = ["db"]
