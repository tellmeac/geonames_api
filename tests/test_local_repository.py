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

test_database_conn = file_database_conn


def test_load():
    """
    Tests load repository content locally.
    :return:
    """
    try:
        _ = GeonamesSQLiteRepository(test_database_conn, data_path, delimiter)
    except Exception as e:
        pytest.fail(f"unexpected exception: {e}")


def test_get_unfiltered():
    """
    Tests get geodata with limit and offset.
    :return:
    """
    repository = GeonamesSQLiteRepository(test_database_conn, data_path, delimiter)

    required_limit = 100
    required_offset = 0
    models = repository.get_geodata(required_limit, required_offset)

    # checking length
    assert len(models) == required_limit

    # checking that offset is correct
    assert models[0].id == '451747'


def test_get_by_name():
    """
    Tests get geodata by name.
    :return:
    """
    repository = GeonamesSQLiteRepository(test_database_conn, data_path, delimiter)

    name = "Smorodinka"
    models = repository.search_by_name(name)

    assert len(models) > 0


def test_get_by_name_part():
    """
    Tests get geodata by name part.
    :return:
    """
    repository = GeonamesSQLiteRepository(test_database_conn, data_path, delimiter)

    name_part = "Smor"
    limit = 5
    models = repository.search_by_name_part(name_part, limit)

    assert limit == len(models)
