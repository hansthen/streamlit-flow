import streamlit as st

class App():
    """The streamlit-flow Application object is a recipe to simplify screen flows
        in streamlit.

    Examples
    --------
    >>> app = initialize("app", App)
    >>> @app.route("main")
    >>> def main():
    ...     st.write("screen 1")
    ...     if st.button("next")
    ...        app.goto("next")

    >>> @app.route("next")
    >>> def next():
    ...     st.write("screen 2")
    ...     if st.button("back")
    ...         app.goto("back")

    >>> app.show()

    """
    def __init__(self):
        """Initalize the application router"""
        self._page = "main"
        self._args = []
        self._kwargs = {}
        self._pages = {}
    
    def goto(self, page, *args, **kwargs):
        """Goto a new page"""
        self.next(page, *args, **kwargs)
        st.rerun()

    def next(self, page, *args, **kwargs):
        """Set the next page to be shown"""
        if page not in self._pages:
            raise ValueError(f"Page {page} not known")
        self._page = page
        self._args = args
        self._kwargs = kwargs

    def go(self):
        """Trigger a rerun to display the next page"""
        st.rerun()

    def show(self):
        """Show the current page"""
        page = self._pages[self._page]
        return page(*self._args, **self._kwargs)

    def route(self, name):
        """Register a view function by name""" 
        def wrapper(func):
            self._pages[name] = func
            return func
        return wrapper 
        
def initialize(key, default):
    """Initialize an object in the streamlit session"""
    if key in st.session_state:
        pass
    elif hasattr(default, "__call__"):
        st.session_state[key] = default() 
    else:
        st.session_state[key] = default

    return st.session_state[key]

