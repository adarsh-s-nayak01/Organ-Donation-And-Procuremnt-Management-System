# Importing pakages
import streamlit as st
import mysql.connector

from create import create
#from database import create_table
from delete import delete
from read import read
from update import update
from query_box import QueryBox


def main():
    st.title("ORGAN DONATION AND PROCUREMENT MANAGAMENT SYSTEM")
    menu = ["Add", "View", "Edit", "Remove","Query Box"]
    choice = st.sidebar.selectbox("Menu", menu)

    #create_table()
    if choice == "Add":
        st.subheader("Enter Details:")
        create()

    elif choice == "View":
        st.subheader("View created tasks")
        read()

    elif choice == "Edit":
        st.subheader("Update created tasks")
        update()

    elif choice == "Remove":
        st.subheader("Delete created tasks")
        delete()

    elif choice == "Query Box":
        st.subheader("Query Window")
        QueryBox()

    else:
        st.subheader("About tasks")
       


if __name__ == '__main__':
    main()

#constraints
#errors
#exceptions
#peer review
#UI
#any other creative thing to be added
#statstical analysis if time permits
#login and grant permissions
