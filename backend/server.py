import db_helper_copy
from datetime import date
from fastapi import FastAPI,Body, HTTPException
from typing import List
from pydantic import BaseModel




class Expense(BaseModel):
    amount:float
    category:str
    notes:str

class DateRange(BaseModel):
    start_date:date
    end_date:date

app=FastAPI()

@app.get('/expenses/{expense_date}',response_model=List[Expense])
def get_expenses_for_date(expense_date:date):
    # return f'recd {expense_date}'
    expenses=db_helper_copy.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500,detail='Expense retrieval failed')
    return expenses

@app.get('/month_ans/')
def get_month_analytics():
    m = db_helper_copy.fetch_expenses_by_month()
    if m is None:
        raise HTTPException(status_code=500,detail='Expense updation failed')
    return m


@app.post('/expenses/{expense_date}')
def add_or_update_expenses(expense_date:date,expenses:List[Expense]=Body(...)):
    db_helper_copy.delete_expenses_for_date(expense_date)
    for e in expenses:
        db_helper_copy.insert_expense(expense_date,e.amount,e.category,e.notes)
    if expenses is None:
        raise HTTPException(status_code=500,detail='Expense updation failed')
    return 'expenses added'

@app.post('/analytics/')
def date_wise_analytics(date_range: DateRange):
    data=db_helper_copy.fetch_expenses_between(date_range.start_date,date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500,detail='Expense summary retrieval failed')
    total=sum([i['total']for i in data])
    breakdown={}
    for i in data:
        perct=(i['total']/total)*100 if ((total !=0) and (i['total']!=0)) else 0
        breakdown[i['category']]={
            'total':i['total'],
            'percentage':round(perct,2)
        }
    return breakdown

if __name__=='__main__':
    fi=get_month_analytics()
    print(fi)
#     a=[
#     {"amount": 100, "category": "Food", "notes": "Lunch"},
#     {"amount": 50, "category": "Transport", "notes": "Bus fare"}
# ]

    # print(add_or_update_expenses('2024-08-13',a))
#     delete_expenses_for_date('2024-08-13')