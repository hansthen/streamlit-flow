# streamlit-flow
A recipe to simplify streamlit navigation flow

The package adds an Application object that
can be used to define pages, like Flask.

The application object has methods like
`goto` and `next` to switch between pages.

For example
```
from streamlit_flow import App, initialize

app = initialize("app", App)

@app.route("main")
def main():
    st.write("screen 1")
    if st.button("next")
        app.goto("next")

@app.route("next")
def next():
    st.write("screen 2")
        if st.button("back")
            app.goto("back")

app.show()
```
