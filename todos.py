import streamlit as st
from todos_db import LocalDb
import datetime
import pandas as pd
st.title("Todos")
todo = st.text_input("Enter todo")
descr = st.text_input("Enter description")
btn = st.button("Add todo")

localdb = LocalDb("test1.db","test_table")
if btn:
    localdb.insert_data(todo,descr,datetime.datetime.now())
    all_data = localdb.get_all_data()
    df = pd.DataFrame(all_data)
    st.dataframe(df)
    

