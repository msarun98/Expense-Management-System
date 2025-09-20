import requests
import streamlit as st
import pandas as pd
# from datetime import datetime

API_URL='http://localhost:9000'

def month_analytics_tab():
    response = requests.get(f'{API_URL}/month_ans/')
    table= response.json()
    rows=[]
    for item in table:
        rows.append({
            "Month": item['MNAME'],
            "Total": round(item['total'])
        })
    rows=pd.DataFrame(rows)
    st.subheader('Month-wise Expense Breakdown')
    st.bar_chart(data=rows.set_index('Month')['Total'], use_container_width=True)
    st.table(rows)


if __name__ == '__main__':
    fy=month_analytics_tab()
    print(fy)