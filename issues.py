import streamlit as st
import pandas as pd


def sysissues():
    requirement = pd.read_csv("data/requirement.csv")
    cols = st.columns(2)

    with cols[0]:
        cont=st.container(border=True)
        cont.markdown("#### Requirement Satisfaction Status")
        for i,row in requirement.iterrows():
            id = row["ID"]
            req = row["Requirement Name"]
            satisfied = row["Satisfied By"]

            if pd.notna(req) and pd.isna(satisfied):
                exp = cont.expander(f"⚠️ Requirement {id} ({req} is not satisfied by anything)")
                exp.markdown(f"**Requirement ID:** {id}", True)
                exp.markdown(f"**Requirement Name:** {req}", True)
                exp.markdown(f"**Requirement Description:** {row['Requirement Description']}", True)
                if pd.notna(row["Verified By"]):
                    exp.markdown(f"**Verified By:** {row['Verified By']}", True)


    
    with cols[1]:
        cont=st.container(border=True)
        cont.markdown("#### Requirement Verification Status")
        for i,row in requirement.iterrows():
            id = row["ID"]
            req = row["Requirement Name"]
            verified = row["Verified By"]

            if pd.notna(req) and pd.isna(satisfied):
                exp = cont.expander(f"⚠️ Requirement {id} ({req} is not verified by any activity)")
                exp.markdown(f"**Requirement ID:** {id}", True)
                exp.markdown(f"**Requirement Name:** {req}", True)
                exp.markdown(f"**Requirement Description:** {row['Requirement Description']}", True)
                if pd.notna(row["Satisfied By"]):
                    exp.markdown(f"**Satisfied By:** {row['Satisfied By']}", True)