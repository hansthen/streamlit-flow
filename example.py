import streamlit as st
from streamlit_flow import initialize, App

app = initialize("app", App)


@app.route("main")
def main():
    st.write("page 1")
    if st.button("page 2"):
        app.goto("2")


@app.route("2")
def page2():
    st.write("page 2")
    if st.button("back"):
        app.goto("main")


app.show()
