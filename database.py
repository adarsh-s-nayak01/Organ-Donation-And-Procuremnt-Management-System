# pip install mysql-connector-python
import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="organ_donation"
)
c = mydb.cursor()


#def create_table():
    #c.execute('CREATE TABLE IF NOT EXISTS Organisation(org_id TEXT,  TEXT, dealer_city TEXT, dealer_pin TEXT, '
              #'dealer_street TEXT)')


def add_data(table,new_val):
    new_val = tuple(new_val)
    tot_values = '%s,'*len(new_val)
    tot_values = tot_values[:-1]
    c.execute(f"INSERT INTO {table} VALUES ({tot_values})",new_val)
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM Patient')
    data = c.fetchall()
    return data


def view_only_patient_names():
    c.execute('SELECT Patient_name FROM Patient')
    data = c.fetchall()
    return data


def get_patient(Patient_name):
    c.execute('SELECT * FROM Patient WHERE Patient_name="{}"'.format(Patient_name))
    data = c.fetchall()
    return data


# def edit_patient_data(new_patient_id, new_patient_name, new_phone_no,new_organ_req,new_location,new_org_id,patient_id, patient_name, phone_no,organ_req,location,org_id):
def edit_patient_data(new_patient_id,new_patient_name,new_phone_no,new_organ_req,new_location,Patient_id,Patient_name,Phone_no,organ_req,Location):
    c.execute("UPDATE Patient SET Patient_id=%s, Patient_name=%s, Phone_no=%s,organ_req=%s,Location=%s WHERE Patient_id=%s and Patient_name=%s and Phone_no=%s and organ_req=%s and Location=%s", (new_patient_id,new_patient_name,new_phone_no,new_organ_req,new_location,Patient_id,Patient_name,Phone_no,organ_req,Location))
    mydb.commit()
    # data = c.fetchall()
    # return data


def delete_data(patient_name):
    c.execute('DELETE FROM patient WHERE patient_name="{}"'.format(patient_name))
    mydb.commit()


def execute_query(query):
    try:
        c.execute(query)
        if query.split()[0].lower() not in ['select','show']:
            mydb.commit()
        data = c.fetchall()
        return [data,c.column_names]
    except BaseException as e:
        if str(e)=='No result set to fetch from.':
            st.success('querry successful')
            return 1
        st.error(e)
        return 0
# alter  select * from table
# update select * from table
# delete show tables
# create show tables

def show_tables():
    c.execute('show tables')
    res = c.fetchall()
    tables = [i[0]  for i in res ]
    return tables

def get_attributes(table):
    c.execute(f'select * from {table}')
    res = c.fetchall()
    attributes = c.column_names
    return attributes

def view_table(table):
    c.execute(f'select * from {table}')
    res = c.fetchall()
    return res

def get_all_values(table):
    c.execute(f"show keys from {table} where key_name = 'primary'")
    res = c.fetchall()
    P_key = res[0][4]
    c.execute(f"select {P_key} from {table} ")
    attri_list = c.fetchall()
    attri_list = [i[0] for i in attri_list]
    return [sorted(attri_list),P_key]

def delete_val(value,table,attribute):
    try:
        # que to get datatype if needed select data_type from information_schema.columns where table_name = 'ticket' and column_name = 'pnr'
        c.execute(f"delete from {table} where {attribute}='{value}'")
        mydb.commit()
        st.success("Deletion successful")
    except Exception as e:
        st.error(e)

def delete_table(table):
    try:
        c.execute(f"drop table {table}")
        mydb.commit()
        st.success("Deletion successful")
    except Exception as e:
        st.error(e)

