# test_my_calls.py
import httpx

def test_server_response():
    url = "http://127.0.0.1:5000/hello?name=Phil"
    response = httpx.get(url)
    assert response.status_code == 200
    assert "Hello, Phil!" in response.text
