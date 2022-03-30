from typing import List

from pydantic import BaseModel


class GeoData(BaseModel):
    """
    Model for geographical data point.
    """
    id: str
    name: str
    ascii_name: str
    alternate_names: List[str]

    feature_class: str
    feature_code: str
    country_code: str
    cc2: str

    admin1_code: int
    admin2_code: int
    admin3_code: int
    admin4_code: int

    population: int
    elevation: str
    dem: str
    timezone: str
    modification_date: str

    def __init__(self, data: List[str]) -> None:
        super.__init__()

