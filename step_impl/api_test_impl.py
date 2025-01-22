import requests
from getgauge.python import step, data_store

@step('Send GET request to <https://httpbin.org/get> with parameters: <table>')
def send_get_request(url, table):
    params = {}
    for row in table:
        params[row[0]] = row[1]
    response = requests.get('https://httpbin.org/get', params=params)
    data_store.scenario.response = response

@step('Send POST request to <https://httpbin.org/post> with JSON body: <table>')
def send_post_request(url, table):
    payload = {}
    for row in table:
        payload[row[0]] = row[1]
    response = requests.post('https://httpbin.org/post', json=payload)
    data_store.scenario.response = response

@step('Verify response status code is <status_code>')
def verify_status_code(status_code):
    assert str(data_store.scenario.response.status_code) == status_code, \
        f"Expected status code {status_code}, but got {data_store.scenario.response.status_code}"

@step('Verify response contains correct parameters')
def verify_response_parameters():
    response_json = data_store.scenario.response.json()
    assert 'args' in response_json, "Response does not contain args"
    args = response_json['args']
    assert args.get('name') == 'test', "Parameter 'name' is incorrect"
    assert args.get('id') == '123', "Parameter 'id' is incorrect"

@step('Verify response body contains submitted data')
def verify_response_body():
    response_json = data_store.scenario.response.json()
    assert 'json' in response_json, "Response does not contain json data"
    json_data = response_json['json']
    assert json_data.get('username') == 'testuser', "Username in response is incorrect"
    assert json_data.get('password') == 'test123', "Password in response is incorrect"