import streamlit as st
from todos_db import LocalDb
import datetime
import pandas as pd
st.title("Todos")
localdb = LocalDb("test1.db","test_table")

add_tab,edit_tab,delete_tab = st.tabs(["Add Todos","Edit Todos","Delete Todos"])


todo = add_tab.text_input("Enter todo")
descr = add_tab.text_input("Enter description")


btn = add_tab.button("Add todo")
show_btn = st.button("Show todos")

all_data = localdb.get_all_data()
def show_todos():
    df = pd.DataFrame(all_data)
    st.dataframe(df)
if show_btn:
    show_todos()

if btn:
    localdb.insert_data(todo,descr,datetime.datetime.now())
    st.info(f"{todo} added successfully!")
    
# edit
task_titles = []
task_descr = []

for task in all_data:
    task_titles.append(task['task'])
    task_descr.append(task['description'])
edit_item = edit_tab.selectbox("Select an item to edit",task_titles)

if edit_item:
    edit_task_input = edit_tab.text_input("Task Name",value=edit_item)
    index = task_titles.index(edit_item)
    edit_descr_input = edit_tab.text_input("Task Description",value=task_descr[index])
    edit_btn = edit_tab.button("Edit task")
    if edit_btn and len(edit_task_input.strip()) > 0 and len(edit_descr_input.strip()) > 0:
        localdb.update_data(edit_item,edit_task_input,edit_descr_input)
        st.info("Edited successfully!")
    elif len(edit_task_input.strip()) == 0 or len(edit_descr_input.strip()) == 0:
        st.warning("Invalid input")
        
# DELETE

item_to_delete = delete_tab.selectbox("Select an item to delete",task_titles)
delete_btn = delete_tab.button("Delete task")
if item_to_delete and delete_btn:
    localdb.delete_data(item_to_delete)
    st.info(f"{item_to_delete} deleted successfully!")
    