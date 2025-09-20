import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL='http://localhost:9000'

def analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_dt=st.date_input('Enter Start Date',datetime(2024,8,1))
    with col2:
        end_dt=st.date_input('Enter End Date',datetime(2024,8,2))
    if st.button ('Get Analytics'):
        payload={
         "start_date":start_dt.strftime('%Y-%m-%d'),
         "end_date":end_dt.strftime('%Y-%m-%d')
        }
        response = requests.post(f'{API_URL}/analytics/',json=payload)
        response = response.json()

        d={
            'Category':list(response.keys()),
            'Total':[round(response[category]['total'])for category in response],
            'Percentage':[round(response[p]['percentage'])for p in response]
        }

        df=pd.DataFrame(d)
        df_sort=df.sort_values(by='Total',ascending=False)
        st.subheader('Expense Breakdown by Category')
        st.bar_chart(data=df_sort.set_index('Category')['Percentage'],use_container_width=True)
        st.table(df_sort)
