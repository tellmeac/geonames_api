import csv
import logging
from pathlib import Path
from pydantic_sqlite import DataBase
from io import StringIO
from charset_normalizer import from_fp

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
        self._db = DataBase()
        self._records_count = 0

        self._load()

    def reload(self) -> None:
        pass

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
            reader = csv.reader(file, delimiter=self._delimiter)
            for row in reader:
                logger.debug(', '.join(row))
                self._records_count += 1

        logger.info(f"data load has been finished: with {self._records_count} records")
        # self._db.add(self._table_name, sample)
