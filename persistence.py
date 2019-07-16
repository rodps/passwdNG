import sqlite3
import datetime

class Persistence():
    """
    this class is responsible for saving and retrieving data in the database.
    """
    
    def __init__(self):
        self.conn = sqlite3.connect('./database/passwdng.db')
        self.cursor = self.conn.cursor()
        with open('./database/passwdng_schema.sql') as db_schema:
            self.cursor.executescript(db_schema.read())

    def add_password(self, username, password, pass_level):
        now = datetime.datetime.now()
        self.cursor.execute('''
            INSERT INTO passwords(username, pass, pass_level, created_at)
            values("{}", "{}", "{}", "{}")
            '''.format(username, password, pass_level, now.strftime("%Y-%m-%d %H:%M")))
        self.conn.commit()

    def get_password(self, username=None):
        if username:
            self.cursor.execute('''
                SELECT *
                FROM passwords
                WHERE username="{}"
                '''.format(username))
            return self.cursor.fetchall()
        self.cursor.execute('''
            SELECT *
            FROM passwords
            ''')
        return cursor.fetchall()
    
    def get_password_groupbyname(self):
        self.cursor.execute('''
            SELECT MAX(id), username, pass, pass_level, created_at
            FROM passwords
            ''')
        return self.cursor.fetchall()

    def delete_password(self, id):
        self.cursor.execute('''
            DELETE FROM passwords
            WHERE id={}
            '''.format(id))
        self.conn.commit()

    def add_conf(self, uppercase, lowercase, numbers, special, total, period):
        now = datetime.datetime.now()
        self.cursor.execute('''
            INSERT INTO conf
            values("{}", "{}", "{}", "{}", "{}", "{}", "{}")
            '''.format(uppercase, lowercase, numbers, special, total, period,
                        now.strftime("%Y-%m-%d %H:%M")))
        conn.commit()

    def get_conf(self, all=False):
        if not all:
            self.cursor.execute('''
                SELECT
                FROM conf
                WHERE id=(
                    SELECT MAX(id)
                    FROM conf
                )''')
            return self.cursor.fetchone()
        self.cursor.execute('''
            SELECT *
            FROM conf
            ''')
        return self.cursor.fetchall()

    def delete_conf(self, id):
        self.cursor.execute('''
            DELETE FROM conf
            WHERE id={}
            '''.format(id))
        conn.commit()

    def close(self):
        self.conn.close()