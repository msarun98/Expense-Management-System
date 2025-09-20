from backend import db_helper_copy
# from backend.db_helper_copy import fetchall_records

def test_expenses_for_date_aug_1():
    c=db_helper_copy.fetch_expenses_for_date('2024-08-01')
    assert len(c)==4
    assert c[0]['amount']==1227
    assert c[1]['notes']=='Groceries for the week'
    assert c[2]['amount']==1200
    assert c[3]['amount']==300

def test_expenses_for_date_invalid_date():

    d=db_helper_copy.fetch_expenses_for_date('9999-08-01')
    assert len(d)==0

def test_insert_and_delete_rows():

    db_helper_copy.insert_expense('9999-09-09',999,'test','na')
    x = db_helper_copy.checking_expenses_for_date('9999-09-09')
    assert len(x) == 1
    assert x[0]['amount'] == 999
    assert x[0]['notes'] == 'na'
    assert x[0]['category'] == 'test'

    db_helper_copy.delete_expenses_for_date('9999-09-09')
    y=db_helper_copy.checking_expenses_for_date('9999-09-09')
    assert len(y)==0
def test_fetch_expenses_between():
    z=db_helper_copy.fetch_expenses_between('2024-08-01','2024-08-10')
    assert z[0]['category']=='Entertainment'
    assert z[0] ['total']==305
    assert z[1]['category']=='Shopping'
    assert z[1]['total'] == 770
    assert z[2]['category'] == 'Food'
    assert z[2]['total'] == 1255
    assert z[3]['category']=='Other'
    assert z[3]['total']==105
    assert z[4]['category']=='Rent'
    assert z[4]['total']==2777