import sqlite3
import os
from sqlite3 import Error

class Database:

    def __init__(self, db_name):
        self.db_name = db_name
    
    def __enter__(self):
        print(f'Connecting to {os.path.basename(os.path.normpath(self.db_name))}')
        self.conn = sqlite3.connect(self.db_name, timeout=20)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        print('Connection successful.')
        return self
    
    def __exit__(self, type, value, tb):
        if self.conn:
            self.conn.close()
            return

    def insert(self, table, **args):
        query = f'INSERT INTO {table}('

        for key, _ in args.items():
            query += key + ','

        query = query[:-1] + ') VALUES ('

        for _, val in args.items():
            if isinstance(val, str):
                query += '\'' + val + '\','
            else:
                query += str(val) + ','
        
        query = query[:-1] + ')'

        print(query)

    