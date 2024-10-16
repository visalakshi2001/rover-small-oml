# Import streamlit to make frontend components
import streamlit as st

# Import functions from other files, where the View is created
from dashboard import dashschedule, dashresults
from architecture import sysarcfunc, requirements
from issues import sysissues

# Set page configuration, page title is the titlebar content, icon also appears on title bar
st.set_page_config(page_title="Rover Dashboard", page_icon="📡", layout="wide")

# main entrypoint of the application, gets called when the app runs
def main():

    # For the heading on the page
    st.header("📡 Rover System Dashboard", divider="red")

    # create the list of tabs in a list
    TABS = ["Requirements", "Architecture", "Test Schedule", "Test Results", "Warnings/Issues"]
    # pass the list to make a tab component
    tabs = st.tabs(TABS)

    # call each tab and call the function that containes the Page view under the tab section
    with tabs[0]:
        requirements()
    with tabs[1]:
        sysarcfunc()
    with tabs[2]:
        # Test schedule tab view
        # dashschedule()
        pass
    with tabs[3]:
        # Test result tab view
        # dashresults()
        pass
    with tabs[4]:
        sysissues()


if __name__ == "__main__":
    main()