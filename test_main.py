from fastapi import responses
from fastapi.testclient import TestClient
from main import app, CITY_KEYWORDS

import pytest


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_get_by_id(client):

    correct_id = 451749 
    response = client.get(f'/cities/{correct_id}')

    assert response.status_code == 200

    response_json = response.json()
    print(response_json)
    for kword in CITY_KEYWORDS:
        assert kword in response_json

    incorrect_id = 1
    response = client.get(f'/cities/{incorrect_id}')

    assert response.status_code == 404


def test_get_page(client):

    page = 10
    limit = 200

    response = client.get(f'/cities?page={page}&limit={limit}')

    assert response.status_code == 200

    page = 999999
    limit = 1000

    response = client.get(f'/cities?page={page}&limit={limit}')

    assert response.status_code == 400



def test_compare_cities(client):
    
    first_name = "Сосенка"
    second_name = "Воронино"

    response = client.get(f'/cities/comparing?first_name={first_name}&second_name={second_name}')

    assert response.status_code == 200

    assert 'northest' in response.json()
    assert 'is_same_timezone' in response.json()

    first_name = "Город богов машиностроения"
    second_name = "Воронино"

    response = client.get(f'/cities/comparing?first_name={first_name}&second_name={second_name}')

    assert response.status_code == 404


def test_show_hints(client):

    request = "Vor"

    response = client.get(f'/cities/hints?request={request}')

    assert response.status_code == 200

    assert len(response.json()['hints']) > 0