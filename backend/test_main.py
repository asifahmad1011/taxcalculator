from fastapi.testclient import TestClient
from products import allProducts
from test_cases import input1, input2, input3, input4, output1, output2, output3, output4


from main import app

client = TestClient(app)


def test_all_products():
    response = client.get("/getAllProducts", json = allProducts)
    assert response.status_code == 200
    assert response.json() == allProducts



def test_case1():
    response = client.post("/calculateTax", json = input1)
    assert response.status_code == 200
    assert response.json() == output1

def test_case2():
    response = client.post("/calculateTax", json = input2)
    assert response.status_code == 200
    assert response.json() == output2

def test_case3():
    response = client.post("/calculateTax", json = input3)
    assert response.status_code == 200
    assert response.json() == output3


def test_case4():
    response = client.post("/calculateTax", json = input4)
    assert response.status_code == 200
    assert response.json() == output4