from unittest.mock import patch

from src.external_api import return_amount_trans

transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
        "amount": "8221.37",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    }
}


@patch('requests.get')
def test_return_amount_trans(mock_get):
    mock_get.return_value.json.return_value = {
        'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37},
        'info': {'timestamp': 1720386006, 'rate': 88.308803},
        'date': '2019-07-03', 'result': 725213.772781
    }
    assert return_amount_trans(transaction) == 725213.772781
    mock_get.assert_called_once()
    mock_get.assert_called_with('https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37',
                                headers={'apikey': 'AJ57MO1ENPdazTOcBs3DFXxSxN2kegOK'})
    