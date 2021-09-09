from typing import Optional
from fastapi import FastAPI, Response
from charset_normalizer import from_path
from io import StringIO
from functools import lru_cache
import uvicorn
import sys
import logging
import pandas

app = FastAPI()

logging.basicConfig(filename="messages.log",
                    level=logging.DEBUG,
                    format= '%(asctime)s: '
                            '%(filename)s: '    
                            '%(levelname)s: '
                            '%(funcName)s(): '
                            '%(lineno)d:\t'
                            '%(message)s')

logger = logging.getLogger(__name__)

DATA_FILE_PATH = "RU.txt"
global data

@app.on_event('startup')
def init_data():
    global data
    logger.info("Init data on startup")
    try:
        file = StringIO(str(from_path(DATA_FILE_PATH).best()))
    except IOError as e:
        logger.fatal(f"IOError: {e}")
        sys.exit(1)

    data = pandas.read_csv(file, delimiter='\t', header=None, low_memory=False)
    del file
    data.set_index(0, drop=True, inplace=True)

CITY_KEYWORDS =  ['geonameid', 'name', 'asciiname',
                  'alternatenames', 'latitude', 'longitude',
                  'feature_class','feature_code', 'country_code',
                  'cc2', 'admin1_code', 'admin2_code',
                  'admin3_code', 'admin4_code', 'population',
                  'elevation', 'dem', 'timezone', 'modification_date']

global tr
@app.on_event("startup")
def init_transliter():
    
    logger.info("Init transliter on startup")

    global tr
    symbols = (u"абвгдеёжзийклмнопрстуфшъыьэюАБВГДЕЁЖЗИЙКЛМНОПРСТУФШЪЫЬЭЮ",
               u"abvgdeejzijklmnoprstufs’y’euABVGDEEJZIJKLMNOPRSTUFS’Y’EU")
    tr = {ord(a):ord(b) for a, b in zip(*symbols)}

    tr[ord('я')] = 'ya'
    tr[ord('Я')] = 'Ya'
    tr[ord('й')] = 'y'
    tr[ord('Й')] = 'Y'
    tr[ord('ч')] = 'ch'
    tr[ord('Ч')] = 'Ch'
    tr[ord('щ')] = 'shch'
    tr[ord('Щ')] = 'Shch'
    tr[ord('ш')] = 'sh'
    tr[ord('Щ')] = 'Sh'
    tr[ord('ц')] = 'ts'
    tr[ord('Ц')] = 'Ts'
    tr[ord('х')] = 'kh'
    tr[ord('Х')] = 'Kh'


def ru_translit(text: str) -> str:
    return text.translate(tr)


@lru_cache(maxsize=256)
def row_to_dict(geonameid: int) -> Optional[dict]:
    try:
        s = data.loc[geonameid]
    except KeyError as er:
        logger.error(f"Not existing geonameid={geonameid}")
        return None

    answer = {"geonameid": geonameid}
    for i, kword in enumerate(CITY_KEYWORDS[1:]):
        answer[kword] = str(s.iloc[i]) if 'nan' not in str(s.iloc[i]) else None

    return answer


def search_to_hints(part: str, limit: int):
    result = []
    i = 0
    if len(part) > 2:
        for row in data.itertuples():
            if part in row._1:
                result.append(row._1)
                i+=1

            if i > limit:
                break

    return result


@lru_cache(maxsize=1024)
def search_to_compare(name_1: str, name_2: str):
    r1 = r2 = None
    fp = sp = -1000
    for row in data.itertuples():
        population = int(row._4) 
        if row._1 == name_1:
            if population > fp:
                fp = population
                r1 = row.Index

        if row._1 == name_2:
            if population > sp:
                sp = population
                r2 = row.Index
    return r1, r2



@app.get("/cities")
def show_page(response: Response, page: int = 1, limit: int=10):
    MAX_LIMIT = 300
    if limit > MAX_LIMIT:
        limit = MAX_LIMIT

    total_records = len(data)
    to_skip = page * limit

    if to_skip + 1 > total_records:
        response.status_code = 400
        return "Bad Request. No results on page={page} with limit={limit}"

    d = data[to_skip:to_skip+limit] 
    answer = []
    # Slow iterrows method on DataFrame with Length <= 300
    for id, _ in d.iterrows():
        answer.append(row_to_dict(id))

    return {"result": answer}


@app.get("/cities/hints")
def show_hints(request: str, limit=10):
    MAX_LIMIT = 64

    limit = MAX_LIMIT if limit > MAX_LIMIT else limit

    request = ru_translit(request)
    answer = {}
    answer['hints'] = search_to_hints(request, limit)

    return answer


@app.get("/cities/comparing")
def compare_by_names(response: Response, first_name: str, second_name: str):
    
    fcity = ru_translit(first_name)
    scity = ru_translit(second_name)

    r1, r2 = search_to_compare(fcity, scity)

    if not r1:
        response.status_code = 404
        return f"Not found {first_name}"
    if not r2:
        response.status_code = 404
        return f"Not found {second_name}"

    first, second = row_to_dict(r1), row_to_dict(r2)
    
    return {
        "northest": first_name if float(first['latitude']) > float(second['latitude']) else second_name,
        "is_same_timezone": True if first['timezone'] == second['timezone'] else False
    }


@app.get("/cities/{geonameid}")
def get_city(response: Response, geonameid: int):

    answer = row_to_dict(geonameid)

    if not answer:
        response.status_code = 404
        return f"Not existing geonameid={geonameid}"

    return answer

if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, debug=False)
