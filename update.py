# import datetime

import pandas as pd
import streamlit as st
from database import view_all_data, view_only_patient_names, get_patient, edit_patient_data


def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=["Patient_id", "Patient_name", "Phone_no","organ_req","Location"])
    with st.expander("Current Patients"):
        st.dataframe(df)
    list_of_patients = [i[0] for i in view_only_patient_names()]
    selected_patient = st.selectbox("Patient to Edit", list_of_patients)
    selected_result = get_patient(selected_patient)
    #print(selected_result)
    # st.write(selected_result)
    if selected_result:
        Patient_id = selected_result[0][0]
        Patient_name = selected_result[0][1]
        Phone_no = selected_result[0][2]
        organ_req = selected_result[0][3]
        Location = selected_result[0][4]
        # Org_id = selected_result[0][5]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_patient_id = st.text_input("Patient ID:", Patient_id)
            new_patient_name = st.text_input("Patient Name:", Patient_name)
        with col2:
            new_phone_no = st.text_input("Phone No:",Phone_no)
            new_organ_req = st.text_input("Organ Required", organ_req)
            new_location = st.text_input("Location:",Location )
            # new_org_id = st.text_input("Organisation ID", Org_id)
        if st.button("Update Patient"):
            edit_patient_data(new_patient_id,new_patient_name,new_phone_no,new_organ_req,new_location,Patient_id,Patient_name,Phone_no,organ_req,Location)
            st.success("Successfully updated")

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=["Patient_id", "Patient_name", "Phone_no","Organ_req","Location"])
    with st.expander("Updated data"):
        st.dataframe(df2)
