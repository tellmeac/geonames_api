from typing import Protocol


class GeodataRepository(Protocol):

    def get_rows(self, limit: int, offset: int) -> list:
        pass

    def search_by_name(self, name: str):
        pass

    def search_by_name_part(self, name_part: str):
        pass
