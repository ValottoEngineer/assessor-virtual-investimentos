from src.app import app

def test_lista_investimentos():
    client = app.test_client()
    response = client.get("/investimentos")
    assert response.status_code == 200

def test_secure_data_sem_token():
    client = app.test_client()
    response = client.get("/secure-data")
    assert response.status_code == 403
