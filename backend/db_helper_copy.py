import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger=setup_logger('db_helper_copy')

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='expense_manager'
    )

    if connection.is_connected():
        print('connection to DB successful')
    else:
        print('Connection to DB failed')
    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()
    cursor.close()
    connection.close()

def fetchall_records():
    logger.info('fetchall_records called')
    with get_db_cursor() as cursor:

        cursor.execute('SELECT * FROM expenses')
        expenses=cursor.fetchall()
        print('fetching all records')
        for expense in expenses:
            print(expense)
        return expenses

def fetch_expenses_by_month():
    logger.info(f'Analysis by month called')
    with get_db_cursor() as cursor:
        cursor.execute(
        '''SELECT DATE_FORMAT(expense_date, '%b-%y') as MNAME, SUM(amount) as total
        FROM expense_manager.expenses
        GROUP BY MNAME, month(expense_date),year(expense_date)
        ORDER BY year(expense_date),month(expense_date);'''
        )
        fa=cursor.fetchall()
        print('collected month wise expenses from db')
        return fa

def fetch_expenses_for_date(expense_date):
    logger.info(f'fetch_expenses_for_date called for {expense_date}')
    with get_db_cursor() as cursor:
        # connection, cursor=get_db_cursor()
        cursor.execute('SELECT * FROM expenses WHERE expense_date=%s',(expense_date,))
        expenses=cursor.fetchall()
    print(f'printing expenses for : {expense_date}')
    for expense in expenses:
        print(expense)
    return expenses

def checking_expenses_for_date(expense_date):
    logger.info(f'checking_expenses_for_date called for {expense_date}')
    with get_db_cursor() as cursor:
        # connection, cursor=get_db_cursor()
        cursor.execute('SELECT * FROM expenses WHERE expense_date=%s',(expense_date,))
        expenses=cursor.fetchall()
        return expenses

def delete_expenses_for_date(expense_date):
    logger.info(f'delete_expense_for_date called for {expense_date}')
    with get_db_cursor(commit=True) as cursor:

        cursor.execute('DELETE FROM expenses WHERE expense_date=%s',(expense_date,))

        print(f'Deleted expenses for : {expense_date}')

def insert_expense(date,amount,category,notes):
    logger.info(f'insert_expense called with {date, amount, category, notes}')
    with get_db_cursor(commit=True) as cursor:
        cursor.execute('INSERT INTO expenses (expense_date, amount, category, notes) VALUES( %s,%s,%s,%s)',(date, amount, category, notes,))
    print('inserted row')
    fetch_expenses_for_date(date)

def fetch_expenses_between(start_dt, end_dt):
    logger.info(f'fetch_expenses_between called for {start_dt,end_dt}')
    with get_db_cursor() as cursor:
        cursor.execute('SELECT category, SUM(amount) as total FROM expenses WHERE expense_date BETWEEN %s and %s GROUP BY category',(start_dt,end_dt,))
        fe=cursor.fetchall()
        return fe

if __name__ == '__main__':
    ind=fetch_expenses_by_month()
    print('printing return input')
    print(ind)
    # f=fetchall_records()
    # print(f)
    # fetch_expenses_for_date('2024/08/02')
    #
    # delete_expenses_for_date('9999-09-09')
    # insert_expense('2025-08-09',2000,'essential','medicines')
    # print(fetch_expenses_between('2024-08-01','2024-08-10'))
    # print(f[0]['expense_date'])
    # print(fetch_expenses_between('2024-08-01', '2024-08-10'))