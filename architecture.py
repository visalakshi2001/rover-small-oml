import streamlit as st
import pandas as pd

# for making UML diagrams
import graphviz

more_colors = {
    "green": "#4bde9c",
    "red": "#fb8072",
    "amber": "#ffed6f"
}


def sysarcfunc():
    system = pd.read_csv("data/system.csv")

    dot = graphviz.Digraph(comment='Hierarchy', strict=True)
    
    for index, row in system.iterrows():
        sys = row["System"]
        subsys = row["Subsystem"]
        comp = row["Component"]

        if pd.notna(sys):
            dot.node(sys)

        if pd.notna(subsys):
            if subsys not in dot.body:
                dot.node(subsys)
            if pd.notna(sys):
                dot.edge(sys, subsys, label="has subsystem")
        
        if pd.notna(comp):
            if comp not in dot.body:
                dot.node(comp, shape="box")
            if pd.notna(subsys):
                dot.edge(subsys, comp, label="has component")  
    st.graphviz_chart(dot, True)    



def requirements():
    st.subheader("Requirement Analysis", divider="orange")
    breakdown = pd.read_csv("data/requirement.csv")


    st.dataframe(breakdown.set_index("ID").style. \
                 applymap(lambda x: f'background-color: {more_colors["amber"]}' if pd.isna(x) else None, subset=["Verified By"]), 
                 column_config={"ID": st.column_config.NumberColumn("ID", format="%s")},
                 use_container_width=True)
    
    cols = st.columns(2)
    with cols[0]:
        req_choice = st.selectbox("Select Requirement by Name", options=breakdown["Requirement Name"], index=1)
        target_req = breakdown[breakdown["Requirement Name"] == req_choice]

        dot = graphviz.Digraph(comment='Hierarchy', strict=True)
        for _, row in target_req.iterrows():
            req = row["Requirement Name"]
            satisfied = row["Satisfied By"]
            verified = row["Verified By"]

            if pd.notna(req):
                dot.node(req)

            if pd.notna(verified):
                if verified not in dot.body:
                    dot.node(verified)
                dot.edge(req, verified, label="verified by")
            
            if pd.notna(satisfied):
                if satisfied not in dot.body:
                    dot.node(satisfied)
                dot.edge(req, satisfied, label="satisfied by")
        st.graphviz_chart(dot)
                
                

    with cols[1]:
        cont = st.container(border=True)
        cont.subheader("Warnings")
        for _, row in breakdown.iterrows():
            id = row["ID"]
            req = row["Requirement Name"]
            verified = row["Verified By"]
            satisfied = row["Satisfied By"]

            if pd.isna(verified):
                cont.warning(f"Requirement {id} ({req}) is not verified by any activity", icon="⚠️")
            if pd.isna(satisfied):
                cont.warning(f"Requirement {id} ({req}) is not satisfied by any mission element", icon="⚠️")
        


    # cols = st.columns([0.35, 0.5])
    # cols[0].graphviz_chart(dot, True)

    # cols[1].dataframe(target_req.rename({0: "values", 1: "values", 2: "values", 3: "values", 4: "values"}).T, use_container_width=True)


