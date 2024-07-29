import pytest


@pytest.fixture
def visa_platinum_card() -> str:
    return "Visa Platinum 7000 7922 8960 6361"


@pytest.fixture
def mask_visa_platinum_card() -> str:
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def maestro_card() -> str:
    return "Maestro 1596 8378 6870 5199"


@pytest.fixture
def mask_maestro_card() -> str:
    return "Maestro 1596 83** **** 5199"


@pytest.fixture
def master_card() -> str:
    return "MasterCard 7158 3007 3472 6758"


@pytest.fixture
def mask_master_card() -> str:
    return "MasterCard 7158 30** **** 6758"


@pytest.fixture
def visa_classic_card() -> str:
    return "Visa Classic 6831 9824 7673 7658"


@pytest.fixture
def mask_visa_classic_card() -> str:
    return "Visa Classic 6831 98** **** 7658"


@pytest.fixture
def account_num() -> str:
    return "Счет 35383033474447895560"


@pytest.fixture
def mask_account_num() -> str:
    return "Счет **5560"


@pytest.fixture()
def list_of_dist_filter_of_state() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture()
def list_of_dist_filter_of_state_result_state_executed() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture()
def list_of_dist_filter_of_state_result_state_canceled() -> list[dict]:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
