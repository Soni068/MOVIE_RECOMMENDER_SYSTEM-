import streamlit as st
import app as ap
import login as log
import register as reg
import subprocess

# Navigation sidebar
def navigation_sidebar():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Registration", "Login","Search Movie"])
    if page == "Home":
        div_with_background = """
            <div style=" 
            padding: 15px;
            border-radius: 20px;
            margin-top: 10px;
            margin-bottom: 20px;
            margin-right: 30px;
            margin-left: 30px;
            letter-spacing: -2px;">
                <h1 style="color:red;text-align:center;text-shadow: 0 0 3px #ff0000, 0 0 5px #0000ff;">Welcome Unlocking Movie Magic</h1>
            </div>
            """
        st.write(div_with_background, unsafe_allow_html=True)
        st.image("https://editor.analyticsvidhya.com/uploads/76889recommender-system-for-movie-recommendation.jpg")
        st.balloons()
        st.session_state['loggedIn'] = False;
    elif page == "Registration":
        reg.register_form()
    elif page == "Login":
         log.login_form()
    elif page == "Search Movie":
        search_mov()

def search_mov():
    if st.session_state['loggedIn']:
        ap.app()
    else:
        st.title("login first")
        val = log.login_form()
        if val:  # Assuming login_form() returns True upon successful login
            search_mov()  # Recursively call search_mov until logged in




# Main function
def main():
    navigation_sidebar()
    if "page" not in st.session_state:
         st.session_state.page = "Home"
    if st.session_state.page == "Login":
        log.login_form()
    elif st.session_state.page == "app":
          ap.app()



if __name__ == "__main__":
    main()
