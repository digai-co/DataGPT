from datagpt.config import config
from datagpt.util import root
from datagpt.memory.faiss import FaissStore
from datagpt.tool.llm_openai import OpenAI
from datagpt.log import logger
from datagpt.tool.db import db

TEXT2SQL_PROMPT = """
## Description
You are a data engineer responsible for translating the requirements of management or business 
personnel into SQL statements that can be executed in {database_type}. Information about each table 
in the database will be provided to you, including table names, table descriptions, field names, 
types, and descriptions for each field. You need to select the relevant tables based on this 
information and write the corresponding SQL statements. If the requirements go beyond the information 
provided by these tables, please be sure to return: "BeyondError."

Note: ONLY ONE sql statement for each requirement.


## Examples
Requirement: Find the name, employee ID, and age of the oldest employee.
SQL: SELECT employee_id, name FROM staff ORDER BY age DESC LIMIT 1;

Requirement: Who is my best friend?
SQL: BeyondError

## Database Information
{database_schema}

## Task to solve
Requirement: {requirement}
SQL:
"""


class Text2SQL:
    def __init__(self):
        self.llm = OpenAI()

    def gen_sql(self, requirement: str) -> str:
        # Search top k tables related to this requirement from long-term memory
        memory_dir = config.get("memory.dir")
        schema_file = config.get("memory.schema_file")
        if not (root / memory_dir / f"{schema_file}.pkl").exists():
            self._cache_schema(memory_dir, schema_file)

        schema_store = FaissStore(memory_dir, schema_file)
        schema = schema_store.search(requirement)
        
        # Generate sql for this requirement
        prompt = TEXT2SQL_PROMPT.format(
            database_type=db.get_type(), database_schema=schema, requirement=requirement
        )
        sql = self.llm.ask(prompt)
        if sql == "BeyondError":
            logger.error(f"Error on generating sql for [{requirement}]")

        return sql

    def _cache_schema(self, memory_dir: str, schema_file: str):
        """Cache schemas of all tables to long-term memory"""
        schemas = {}

        tables = db.get_tables()
        for table in tables:
            fields = db.get_fields(table.name)
            schema = "\n".join(
                [
                    f"col:{f.col_name}, type:{f.col_type}, description:{f.col_comment}"
                    for f in fields
                ]
            )
            schemas[
                f"{table.name}:{table.comment}"
            ] = f"table: {table.name}\ntable description: {table.comment}\ncolumns information:\n{schema}\n"

        schema_store = FaissStore(memory_dir, schema_file)
        schema_store.write(schemas)
