from typing import Protocol, List

from geonames.models.geodata import GeoData


class GeodataRepository(Protocol):
    """
    Base GeoData repository interface
    """
    def get_rows(self, limit: int, offset: int) -> List[GeoData]:
        """
        Gets rows with offset and limit
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

    def search_by_name_part(self, name_part: str) -> List[GeoData]:
        """
        Searches GeoData by its name part
        :param name_part:
        :return: list of geodata models
        """
        pass
