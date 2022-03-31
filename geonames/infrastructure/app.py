from fastapi import FastAPI


class Application:
    """
    Application entrypoint class.
    """
    def __init__(self):
        self._app = FastAPI()
