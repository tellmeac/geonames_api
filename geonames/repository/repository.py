from typing import Protocol, List

from geonames.models.geodata import GeoData


class GeodataRepository(Protocol):
    """
    Base GeoData repository interface
    """
    def get_geodata(self, limit: int, offset: int) -> List[GeoData]:
        """
        Gets geodata list by offset and limit
        :param limit:
        :param offset:
        :return: list of geodata models
        """
        pass

    def search_by_name(self, name: str) -> List[GeoData]:
        """
        Searches GeoData by its name
        :param name:
        :return: list of geodata models
        """
        pass

    def search_by_name_part(self, name_part: str, limit: int) -> List[GeoData]:
        """
        Searches GeoData by its name part
        :param name_part:
        :param limit:
        :return: list of geodata models
        """
        pass
