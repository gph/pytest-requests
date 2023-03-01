import main

url = 'http://example.com'


def test_get_data_return_when_status_code_200(mocker):
    mock_requests = mocker.patch('main.requests.get')
    mock_json = {'data': 123}
    mock_requests.return_value.status_code = 200
    mock_requests.return_value.json.return_value = mock_json

    result = main.get_data(url)

    assert result == mock_json


def test_get_data_return_when_status_code_not_200(mocker):
    mock_requests = mocker.patch('main.requests.get')
    mock_json = {'data': 123}
    mock_requests.return_value.status_code = 500
    mock_requests.return_value.json.return_value = mock_json

    result = main.get_data(url)

    assert result is None


def test_get_data_return_when_exception_occurs(mocker):
    mocker.patch('main.requests.get', side_effect=Exception('Timeout Error Example'))

    result = main.get_data(url)

    assert result is None
