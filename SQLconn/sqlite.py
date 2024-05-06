from DBconn import DBconn
import sqlite3
class SQLite(DBconn):
    def __init__(self,file_path:str) -> None:
        super.__init__()
        self.__file_path=file_path
        self._conn=sqlite3.connect(file_path)
        self._engine=self._makeEngine()
    @property
    def URL(self):
        return f'sqlite://{self.__file_path}'