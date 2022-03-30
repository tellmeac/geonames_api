import csv
import logging
import sqlite3
from pathlib import Path
from typing import List

from io import StringIO
from charset_normalizer import from_fp

from geonames.models.geodata import from_list, GeoData
from geonames.repository.repository import GeodataRepository

logger = logging.getLogger(__name__)


class GeonamesSQLiteRepository(GeodataRepository):
    """
    In-Memory sqlite repository implementation
    """
    def __init__(self, conn: str, filepath: Path, delimiter: str) -> None:
        """
        Accepts table like csv, but with specific delimiter
        :param conn: sqlite connection string
        :param filepath: path to csv-like file
        :param delimiter: delimiter in csv-like file
        """
        self._table_name = "geonames"
        self._filepath = filepath
        self._delimiter = delimiter
        self._records_count = 0

        self._conn_address = conn
        self._conn = sqlite3.connect(conn)
        self._field_names = GeoData.schema()["properties"].keys()
        self._conn.execute(f"create table {self._table_name} ({','.join(self._field_names)});")

        self._load()

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

    def search_by_name_part(self, name_part: str) -> List[GeoData]:
        """
        Searches GeoData by its name part
        :param name_part:
        :return: list of geodata models
        """
        pass

    def reload(self) -> None:
        """
        Reloads data to database.
        :return:
        """
        self._conn = sqlite3.connect(self._conn_address)
        self._conn(f"create table {self._table_name} ({','.join(self._field_names)});")
        self._load()

    def _load(self) -> None:
        """
        Loads geonames content in in-memory sqlite.
        :return:
        """
        if not self._filepath.exists():
            raise FileNotFoundError(f"table file with geonames not found: {self._filepath}")

        with open(self._filepath, "rb") as fp:
            # file has been normalized.
            file = StringIO(str(from_fp(fp).best()))

            # init csv file reader to read content by row
            reader = csv.reader(file, delimiter=self._delimiter)
            for row in reader:
                # add new record to database
                self._insert_row(row)
                self._records_count += 1

        logger.info(f"Data load has been finished: with {self._records_count} records")

    def _insert_row(self, row: List[str]) -> None:
        """
        Inserts row in sqlite database
        :param row:
        :return:
        """
        if len(self._field_names) != len(row):
            raise ValueError(f"data list length doesn't match fields count "
                             f"(required={len(self._field_names)}, have={len(row)})")

        insert_statement = f"insert into {self._table_name} values ({','.join(['?']*len(row))});"
        self._conn.execute(insert_statement, row)
