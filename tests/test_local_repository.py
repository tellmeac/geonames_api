import pytest

from pathlib import Path
from geonames.repository.local import GeonamesSQLiteRepository

# path to testing table data file
data_path = Path("../RU.txt")

# \t symbol as delimiter
delimiter = '\t'

# conn strings for test database
file_database_conn = "../test_database.db"
memory_database_conn = ":memory:"


def test_load():
    """
    Tests load repository content locally.
    :return:
    """
    try:
        _ = GeonamesSQLiteRepository(memory_database_conn, data_path, delimiter)
    except Exception as e:
        pytest.fail(f"unexpected exception: {e}")


