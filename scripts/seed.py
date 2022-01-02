import sqlite3
from sqlite3 import Error
import requests
import json
import sys
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Seed:

    db_path = "../main/database"
    db_name = "github_users.db"

    def _create_dir(self):
        path = os.path.join(basedir, self.db_path)
        
        return os.mkdir(path)

    def _sql_connection(self):
        path_file = f"{self.db_path}/{self.db_name}"
        path_dir = os.path.join(basedir, path_file)
        path = os.path.join(basedir, self.db_path)
        isFile = os.path.exists(path)
        if not isFile:
            print("Dir not found")
            os.makedirs(path, exist_ok=False)
        
        print(f"Path: {path_dir}")
        try:
            con = sqlite3.connect(path_dir)
            
            return con
        except Error:
            print(Error)

    def _create_sql_table(self, con):

        cursorObj = con.cursor()

        user_table =  cursorObj.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
        ).fetchall()

        if user_table == []:
            cursorObj.execute(
                "CREATE TABLE users(id integer PRIMARY KEY, "
                "username text, avatar_url text, type text, url text)"
                )
        else:
            print("Table already exists")
        con.commit()
        print("Created Users Table")

    def _insert_user_table(self, con):
        cursorObj = con.cursor()
        # Insert a row of data
        # cursorObj.execute(
        #     "INSERT INTO users "
        #     "VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
        
        n = len(sys.argv)
        print("Total arguments passed:", n)
        # print(sys.argv[2])
        api_url = 'https://api.github.com/users'
        res_api = requests.get(api_url)
        data = json.loads(res_api.text)
        check_t = False
        for i in range(len(data)):
            if len(sys.argv) > 1:
                if str(sys.argv[1]) == '-t' or str(sys.argv[1]) == '--total':
                    if i <= int(sys.argv[2]):
                        print("Adding Data to users table")
                        cursorObj.execute(
                            "INSERT OR IGNORE INTO users "
                            "VALUES ('%d','%s','%s','%s', '%s')"
                            % (data[i]['id'], data[i]['login'], 
                                data[i]['avatar_url'], data[i]['type'], data[i]['url'])
                            ) 
                        # print(f'i-{i}, data: {data[i]}')
                        print("Added Data to users table")
                        
                else:
                    check_t = True

            else:
                print("No args passed to script")
                if i <= 150:
                    cursorObj.execute(
                                "INSERT INTO users "
                                "VALUES ('%d','%s','%s','%s', '%s')"
                                % (data[i]['id'], data[i]['login'], 
                                    data[i]['avatar_url'], data[i]['type'], data[i]['url'])
                            )
                print("Added to table")

        if check_t:
            print("Please use --total or -t to pass number of users to be inserted")

        # Save (commit) the changes
        con.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        con.close()

    def select_all(self, page=None, limit=25):
        
        list_all = []
        con = self._sql_connection()
        cur = con.cursor()
        count = cur.execute('SELECT COUNT(*) FROM users').fetchone()
        count_res = count[0]
        print(f"Counting - {count_res}")
        cursor = cur.execute('SELECT * FROM users ORDER BY id LIMIT %d' % limit).fetchall()
        if page:
            last_val = int(page) * limit
            print(f"last val: {last_val}")
            cursor = cur.execute(
                'SELECT * FROM users ORDER BY id LIMIT %d OFFSET %d' % (limit, last_val)).\
                    fetchall()
            # cursor = cur.execute(
            #     'SELECT * FROM users GROUP BY id HAVING COUNT(*) > %d ORDER BY id LIMIT %d OFFSET %d' % (last_val, limit)).\
            #         fetchall()
        for row in cursor:
            list_all.append(row)
            # for r in row:
            #     list_all.append(r)
        # names = [{description[0]: description} for description in cursor.description]
        print(list_all)
        return list_all

    def order_by(self, value):
        
        list_all = []
        con = self._sql_connection()
        cur = con.cursor()
        cursor = cur.execute('SELECT * FROM users ORDER BY %s' % value).fetchall()
        
        for row in cursor:
            list_all.append(row)

        return list_all

    def filter_username(self, username):
        
        list_all = []
        con = self._sql_connection()
        cur = con.cursor()
        cursor = cur.execute("SELECT * FROM users WHERE username=:username", {"username": username}).fetchall()

        
        for row in cursor:
            list_all.append(row)

        return list_all
    
    def filter_id(self, uid):
        
        list_all = []
        con = self._sql_connection()
        cur = con.cursor()
        cursor = cur.execute("SELECT * FROM users WHERE id=:id", {"id": uid}).fetchall()

        for row in cursor:
            list_all.append(row)

        return list_all

    def create_table(self):
        con = self._sql_connection()

        self._create_sql_table(con)

        # self.insert_user_table(con)
    
    def insert_record(self):
        con = self._sql_connection()

        self._insert_user_table(con)

    def count_rows(self):
        con = self._sql_connection()
        cur = con.cursor()
        cursor = cur.execute('SELECT COUNT(*) FROM users')
        cur_result = cursor.fetchone()
        return cur_result[0]

    
def main():
    users = Seed()
    users.create_table()
    users.insert_record()
    users.select_all()

# def main():
#     n = len(sys.argv)
#     print("Total arguments passed:", n)
#     # print(sys.argv[2])
#     api_url = 'https://api.github.com/users'
#     res_api = requests.get(api_url)
#     data = json.loads(res_api.text)
#     count = 0
#     check_t = False
#     for i in range(len(data)):
#         if len(sys.argv) > 1:
#             if str(sys.argv[1]) == '-t' or str(sys.argv[1]) == '--total':
#                 if i <= int(sys.argv[2]):
#                     print(f'i-{i}, data: {data[i]}')
            
#             else:
#                 check_t = True
#                 # print("Please use --total or -t to pass number of users to be inserted")
#         else:
#             print("No args passed to script")
#             print(f"Data: {data[i]}")

#     if check_t:
#         print("Please use --total or -t to pass number of users to be inserted")
#     # print(f'length- {len(data)}')


if __name__ == '__main__':
    main()