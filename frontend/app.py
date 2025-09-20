import streamlit as st
from add_update import add_update_tab
from analytics_by_day import analytics_tab
from analytics_by_month import month_analytics_tab

API_URL='http://localhost:9000'
st.title('Expense Management System')

# expense_date=st.date_input('Expense Date:   ')
# if expense_date:
#     st.write(f'Fetching expenses for {expense_date}')

tab1, tab2, tab3 = st.tabs(['Add/Update','Analytics by day','Analytics by month'])

with tab1:
    add_update_tab()
with tab2:
    analytics_tab()
with tab3:
    month_analytics_tab()