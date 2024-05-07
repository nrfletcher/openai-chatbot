'''
Utility class responsible for persisting and querying data from the SQLite3 database
'''
import sqlite3

class DbUtil:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect('automotives.db')
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.conn.commit()
        self.conn.close()

    def query(self, table: str):
        self.cursor.execute(f'SELECT * FROM {table} LIMIT 150')
        rows = self.cursor.fetchall()
        data: list = []
        columns = [desc[0] for desc in self.cursor.description]

        for row in rows:
            row_dict = dict(zip(columns, row))
            data.append(row_dict)
        
        return data

   