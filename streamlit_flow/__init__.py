import streamlit as st
import logging
import os


class App:
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

    def __init__(self, name="main", start="main"):
        """Initalize the application router"""
        self._page = start
        self._args = []
        self._kwargs = {}
        self._pages = {}
        self.name = name
        self.logger = logging.getLogger(name)

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


def initialize(key, default, *args, **kwargs):
    """Initialize an object in the streamlit session"""
    if key in st.session_state:
        pass
    elif hasattr(default, "__call__"):
        st.session_state[key] = default(*args, **kwargs)
    else:
        st.session_state[key] = default

    return st.session_state[key]


def set_log_levels():
    """Read and initialize log levels from the environment

    Two environment variables are used:
    LOGLEVEL for the root logger
    ST_FLOW_LOGLEVELS to set individual loggers, using a PATH style syntax.

    Examples
    --------

    EXPORT ST_FLOW_LOGLEVELS=root=FATAL:app=DEBUG
    """

    root_log_level = os.environ.get("LOGLEVEL", "INFO")
    root_logger = logging.getLogger()
    root_logger.setLevel(root_log_level)

    log_levels = os.environ.get("ST_FLOW_LOGLEVELS", "").split(":")
    for log_level in log_levels:
        try:
            name, level = log_level.split("=")
            logging.getLogger(name).setLevel(level)
        except:
            logging.exception("Invalid log level specification `%s`", log_level)
