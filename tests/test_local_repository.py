import pytest

from pathlib import Path
from geonames.repository.local import GeonamesSQLiteRepository

# path to testing table data file
data_path = Path("../RU.txt")

# \t symbol as delimiter
delimiter = '\t'

# path for test database
database_path = Path('../test_database.db')


def test_load():
    """
    Tests load repository content locally.
    :return:
    """
    try:
        _ = GeonamesSQLiteRepository(data_path, delimiter)
    except Exception as e:
        pytest.fail(f"unexpected exception: {e}")


def test_save():
    """
    Tests save local repository database to file.
    :return:
    """
    repository = GeonamesSQLiteRepository(data_path, delimiter)
    try:
        repository.save(database_path)
    except Exception as e:
        pytest.fail(f"unexpected exception: {e}")

