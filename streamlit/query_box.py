import pandas as pd
import streamlit as st
from database import view_all_data,show_tables,view_table,get_attributes,query_executor
#execute_query



def QueryBox():
    col1, col2 = st.columns(2)

    with col1:
        with st.form(key='query_form'):
            raw_code = st.text_area("SQL Code Here")
            submit_code = st.form_submit_button("Execute")

    with col2:
        if submit_code:
            st.info("Query Submitted")
            st.code(raw_code)

    if submit_code:
        query_results = query_executor(raw_code)
        # with st.beta_expander("Results"):
        #     st.write(query_results)

        with st.expander("Result Table"):
            query_df = pd.DataFrame(query_results)
            st.dataframe(query_df)






# can be expander also 
# def QueryBox():

#     # result = view_all_data()
#     # df = pd.DataFrame(result, columns=['Dealer ID', 'Dealer Name', 'Dealer City', 'Dealer Pin', 'Dealer Street'])
#     # with st.expander("View all Dealers"):
#     #     st.dataframe(df)
#     tables_list = show_tables()
#     table = st.selectbox("Select table to view", tables_list)
#     result = view_table(table)
#     attributes = get_attributes(table)
#     if st.button("view table"):
#         df = pd.DataFrame(result, columns=attributes)
#         st.dataframe(df)
#     query = st.text_input("Query:")# if possible increase breadth 
#     st.warning("Changes Made to DataBase via QueryBox will be commited")
    
#     if st.button("Execute"):
#         data = execute_query(query)
#         # print(data)
#         if data not in [0,1]:
#             df = pd.DataFrame(data[0],columns=data[1])
#             st.dataframe(df)
