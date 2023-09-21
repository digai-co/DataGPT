from abc import ABCMeta, abstractmethod
from typing import Iterable, List, Optional


class TableInfo:
    name: str
    comment: str

    def __init__(self, name: str, comment: Optional[str] = None):
        self.name = name
        self.comment = comment

    def __str__(self):
        return f"TableInfo(name={self.name}, comment={self.comment})"


class FieldInfo:
    col_name: str
    col_type: str
    col_length: Optional[int]
    col_default: str
    is_nullable: bool
    col_comment: str

    def __init__(
        self,
        col_name: str,
        col_type: str,
        col_length: Optional[int],
        col_default: str,
        is_nullable: bool = False,
        col_comment: Optional[str] = None,
    ):
        self.col_name = col_name
        self.col_type = col_type
        self.col_length = col_length
        self.col_default = col_default
        self.is_nullable = is_nullable
        self.col_comment = col_comment

    def __str__(self):
        return f"FieldInfo(col_name={self.col_name}, col_type={self.col_type}, col_length={self.col_length}, col_default={self.col_default}, is_nullable={self.is_nullable}, col_comment={self.col_comment})"


class RDBMS(metaclass=ABCMeta):
    @abstractmethod
    def get_type(self) -> str:
        pass

    @abstractmethod
    def get_tables(self) -> Iterable[TableInfo]:
        pass

    @abstractmethod
    def get_fields(
        self, table_name: str, schema: str = "public"
    ) -> Iterable[FieldInfo]:
        pass

    @abstractmethod
    def run(self, command: str) -> List:
        pass
