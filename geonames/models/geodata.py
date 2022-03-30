from typing import List

from pydantic import BaseModel


def from_list(data: List[str]) -> 'GeoData':
    """
    Makes GeoData object from list of strings
    :param data: list of strings, order matter
    :return: return new GeoData object
    """
    field_names = list(GeoData.schema()["properties"].keys())

    if len(field_names) != len(data):
        raise ValueError(f"data list length doesn't match fields count (required={len(field_names)}, have={len(data)})")

    result = GeoData()
    for i, field_name in enumerate(field_names):
        result.__setattr__(field_name, data[i])

    return result


class GeoData(BaseModel):
    """
    Model for geographical data point.
    """
    id: str
    name: str
    ascii_name: str
    alternate_names: str

    feature_class: str
    feature_code: str
    country_code: str
    cc2: str

    admin1_code: str
    admin2_code: str
    admin3_code: str
    admin4_code: str

    population: str
    elevation: str
    dem: str
    timezone: str
    modification_date: str
