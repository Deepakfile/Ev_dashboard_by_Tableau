import streamlit as st
import base64

st.set_page_config(page_title="EV Dashboard", layout="wide")

# ---------- Background Image ----------
def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_base64("ev_bg.png")

page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
background-position: center;
background-attachment: fixed;
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---------- Login ----------
if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Invalid login")

else:
    st.title("Electric Vehicle Dashboard")

    option = st.selectbox(
        "Select Dashboard",
        ["Dashboard 1", "Dashboard 2", "Dashboard 3"]
    )

    if option == "Dashboard 1":
        st.image("dashboard1.png", use_container_width=True)

    elif option == "Dashboard 2":
        st.image("dashboard2.png", use_container_width=True)

    elif option == "Dashboard 3":
        st.image("dashboard3.png", use_container_width=True)