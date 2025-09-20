import mysql.connector
try:
    print(1)
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='expense_manager'
    )
    print("Connected!")
    conn.close()
    print('closed.')
except Exception as e:
    print(f"Connect failed: {e}")
#
# import pymysql
# try:
#     conn = pymysql.connect(
#         host='localhost',
#         user='root',
#         password='root',
#         database='expense_manager'
#     )
#     print("Connected!")
#     conn.close()
# except Exception as e:
#     print(f"Connect failed: {e}")

# import os
# print(os.environ['PATH'])

