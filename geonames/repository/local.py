import csv
import logging
from pathlib import Path
from pydantic_sqlite import DataBase
from io import StringIO
from charset_normalizer import from_fp

from geonames.models.geodata import from_list

logger = logging.getLogger(__name__)


class GeonamesSQLiteRepository:
    """
    In-Memory sqlite repository implementation
    """
    def __init__(self, filepath: Path, delimiter: str) -> None:
        """
        Accepts table like csv, but with specific delimiter
        :param filepath: path to csv-like file
        :param delimiter: delimiter in csv-like file
        """
        self._table_name = "geonames"
        self._filepath = filepath
        self._delimiter = delimiter
        self._records_count = 0
        self._db = DataBase()

        self._load()

    def reload(self) -> None:
        """
        Reloads data to database.
        :return:
        """
        pass

    def save(self, filepath: Path) -> None:
        """
        Saves sqlite database to file
        :param filepath: path to save database file
        :return:
        """
        self._db.save(str(filepath))

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
                # logger.debug(', '.join(row))
                try:
                    geodata = from_list(row)
                except ValueError as e:
                    logger.warning(f"geodata row couldn't be parsed into model: {str(e)}")
                    continue

                # add new record to database
                self._db.add(self._table_name, geodata)
                self._records_count += 1

        logger.info(f"data load has been finished: with {self._records_count} records")

