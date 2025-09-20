import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger=setup_logger('db_helper_copy')

@contextmanager
def get_db_cursor(commit=False):

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='expense_manager'
        )
    except Exception as e:
        print(f'exception occurred{e}')

    try:
        if connection.is_connected():
            print('connection to DB successful')
        else:
            print('Connection to DB failed')
        cursor = connection.cursor(dictionary=True)
        try:
            yield cursor
            if commit:
                connection.commit()
        finally:
            cursor.close()
            connection.close()
    except Exception as e:

        print(f"Database error: {e}")
        raise

def fetchall_records():
    logger.info('fetchall_records called')
    with get_db_cursor() as cursor:

        cursor.execute('SELECT * FROM expenses')
        expenses=cursor.fetchall()
        print('fetching all records')
        for expense in expenses:
            print(expense)
        return expenses

if __name__ == '__main__':
    pass
