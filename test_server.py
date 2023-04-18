"""code to test server"""

# import pytest
# from sanic import Sanic
# from sanic import response
# from sync_test import test_basic_test_client

from server import app




def test_get_req():
    """testing GET requests"""
    request, response = app.test_client.get("/")
    assert response.status == 200
    assert response.text == "Hello, world."




def test_post_req():
    """testing POST requests"""

    payload = {'key': 'value'}
    headers = {'content-type': 'application/json'}
    _, response = app.test_client.post('/test', json=payload, headers=headers)

    assert response.status == 200
    assert response.json == {'status': 'success'}


def test_put_req():
    """testing PUT requests"""
    payload = {'key': 'value'}
    headers = {'content-type': 'application/json'}
    _, response = app.test_client.post('/test', json=payload, headers=headers)

    assert response.status == 200
    assert response.json == {'status': 'success'}



def test_patch_req():
    """testing PATCH requests"""
    payload = {'key': 'value'}
    headers = {'content-type': 'application/json'}
    _, response = app.test_client.post('/test', json=payload, headers=headers)

    assert response.status == 200
    assert response.json == {'status': 'success'}





def test_del_req():
    """testing DELETE requests"""
    _, response = app.test_client.delete('/test')

    assert response.status == 200
    assert response.json == {'status': 'success'}
