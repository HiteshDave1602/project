from fastapi.testclient import TestClient

import sys
sys.path.append("/home/hitesh/Documents/practice/user/project/")
from app import app

client = TestClient(app)

data={
    "id":1,
    "username":"string",
    "email":"string",
    "password":"string"
    }
def test_user_insert():
    headers = {'Content-type': 'application/json'}
    response = client.post("/user/insert",json=data, headers=headers)
    assert response.status_code == 200


def test_get_user():
    id=[6,7,9,10]
    for user_id in id:
        response = client.get(f"/user/show/{user_id}")
        assert response.status_code == 200
    
updated_data = {
    "id": 8,
     "username": "stridrgdfgbng",
      "email": "strirdgdng",
       "password":"strisrtgng"
    }
def test_update_data():
    headers = {'Content-type': 'application/json'}
    response = client.put("/user/update", json=updated_data, headers=headers)
    assert response.status_code == 200


def test_delete_data():
    id=[21,22,23]
    for user_id in id:
        response = client.delete(f"/user/delete/{user_id}")
        assert response.status_code == 200