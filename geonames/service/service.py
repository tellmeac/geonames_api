from fastapi import APIRouter
from fastapi.openapi.models import Response

_router = APIRouter()


class GeoNamesService:
    """
    GeoData service
    """
    def __init__(self):
        self.router = _router

    @_router.get("/cities")
    def get_page(self, response: Response, page: int = 1, limit: int = 40):
        """
        Returns GeoData models with required limit and page
        :param response:
        :param page:
        :param limit:
        :return:
        """
        pass

    @_router.get("/cities/comparing")
    def compare(self, response: Response, name_part: str, limit: int = 10):
        """
        Returns hints to complete name by part
        :param response:
        :param name_part:
        :param limit:
        :return:
        """
        pass

    @_router.get("/cities/hints")
    def get_hints(self, first: str, second: str):
        """
        Returns comparing results of two geographical points
        :param first:
        :param second:
        :return:
        """
        pass
