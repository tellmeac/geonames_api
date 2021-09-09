# Geonames API Task

In this task implemented HTTP server to deliver information about geographical objects.

The data was taken from the link: http://download.geonames.org/export/dump/RU.zip

And the data format was explained on: http://download.geonames.org/export/dump/readme.txt

## Methods implemented:
* **/cities**
* **/cities/{geonameid}**
* **/cities/comparing**
* **/cities/hints**


## /cities

Description:

Returns list of geographical objects.

Query arguments:
* **page**: int (*default = 1*) - argument sets page to be shown, depends on limit argument
* **limit**: int (*default = 10*) - argument sets limit to be show on page

Response example:
<details>
  <summary>Click to expand!</summary>
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

</details>


## /cities/{geonameid}

Description:

Returns full information about geographical object.

Path arguments:
* **geonameid**: int - object id

Response example:
<details>
  <summary>Click to expand!</summary>
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
</details>


## /cities/comparing

Description:

Compares two objects by the timezone and the distance to North.

Query arguments:
* **first_name**: str- first name (can be written in Cyrillic or Latin)
* **second_name**: str - second name (can be written in Cyrillic or Latin)

Response example:
<details>
  <summary>Click to expand!</summary>
    {
    "northest": "Сосенка",
    "is_same_timezone": false
    }
</details>


## /cities/hints

Description:

Additional method.

Show object names that match uncompleted request.

Query arguments:
* **request**: str- part of geographical object name (can be written in Cyrillic or Latin)
* **limit**: int (default=10) - limit of hints to be found

Response example:
<details>
  <summary>Click to expand!</summary>
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
</details>