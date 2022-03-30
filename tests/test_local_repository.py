import pytest

from pathlib import Path
from geonames.repository.local import GeonamesSQLiteRepository

# path to testing table data file
data_path = Path("../RU.txt")

# \t symbol as delimiter
delimiter = '\t'


def test_load():
    try:
        _ = GeonamesSQLiteRepository(data_path, delimiter)
    except Exception as e:
        pytest.fail(f"unexpected exception: {e}")

# def test_reload():
#     pass
