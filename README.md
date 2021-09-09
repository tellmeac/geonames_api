# Geonames API Task

Repository link: https://gitlab.com/b605/geonames_api

In this task was implemented HTTP server to deliver information about geographical objects using FastAPI.

The data was taken from the link: http://download.geonames.org/export/dump/RU.zip

And the data format was explained on: http://download.geonames.org/export/dump/readme.txt

## Methods implemented:
* GET **/cities**
* GET **/cities/{geonameid}**
* GET **/cities/comparing**
* GET **/cities/hints**

## GET /cities

### Description:

Returns list of geographical objects.

### Query arguments:

* **page**: int (*default = 1*) - argument sets page to be shown, depends on limit argument
* **limit**: int (*default = 10*) - argument sets limit to be show on page

### Response example:
~~~json
{
"result": [
        {
        "geonameid": 451749,
        "name": "Zhukovo",
        "asciiname": "Zhukovo",
        "alternatenames": null,
        "latitude": "57.26429",
        "longitude": "34.20956",
        "feature_class": "P",
        "feature_code": "PPL",
        "country_code": "RU",
        "cc2": null,
        "admin1_code": "77",
        "admin2_code": null,
        "admin3_code": null,
        "admin4_code": null,
        "population": "0",
        "elevation": null,
        "dem": "237",
        "timezone": "Europe/Moscow",
        "modification_date": "2011-07-09"
        },
        {
        "geonameid": 451750,
        "name": "Zhitovo",
        "asciiname": "Zhitovo",
        "alternatenames": null,
        "latitude": "57.29693",
        "longitude": "34.41848",
        "feature_class": "P",
        "feature_code": "PPL",
        "country_code": "RU",
        "cc2": null,
        "admin1_code": "77",
        "admin2_code": null,
        "admin3_code": null,
        "admin4_code": null,
        "population": "0",
        "elevation": null,
        "dem": "247",
        "timezone": "Europe/Moscow",
        "modification_date": "2011-07-09"
        }
    ]
}
~~~

## GET /cities/{geonameid}

### Description:

Returns full information about geographical object.

### Path arguments:
* **geonameid**: int - object id

Response example:
```json
    {
    "geonameid": 451749,
    "name": "Zhukovo",
    "asciiname": "Zhukovo",
    "alternatenames": null,
    "latitude": "57.26429",
    "longitude": "34.20956",
    "feature_class": "P",
    "feature_code": "PPL",
    "country_code": "RU",
    "cc2": null,
    "admin1_code": "77",
    "admin2_code": null,
    "admin3_code": null,
    "admin4_code": null,
    "population": "0",
    "elevation": null,
    "dem": "237",
    "timezone": "Europe/Moscow",
    "modification_date": "2011-07-09"
    }
```


## GET /cities/comparing

### Description:

Compares two objects by the timezone and the distance to North.

### Query arguments:

* **first_name**: str- first name (can be written in Cyrillic or Latin)
* **second_name**: str - second name (can be written in Cyrillic or Latin)

Response example:
```json
    {
    "northest": "Сосенка",
    "is_same_timezone": false
    }
```

## GET /cities/hints

### Description:

*Additional method*

Show object names that match uncompleted request.

### Query arguments:
* **request**: str- part of geographical object name (can be written in Cyrillic or Latin)
* **limit**: int (default=10) - limit of hints to be found

### Response example:
```json
{
"hints": [
    "Sosenka",
    "Ozero Sosnishchi",
    "Pristan’ Sosnitsa",
    "Sosnovka",
    "Vostochnyy Sosyk",
    "Verkhnyaya Sosnovka",
    "Verkhnyaya Sosnovka",
    "Vadovo-Sosnovka",
    "Tikhaya Sosna",
    "Staryye Sosny",
    "Staroye Sosno"
    ]
}
```