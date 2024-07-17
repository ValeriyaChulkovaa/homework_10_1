from src.ppp import filter_by_state, sort_by_date
from src.fd import get_data, mask_account_card

if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000 7922 8960 6361"))
    print(mask_account_card("Maestro 1596 8378 6870 5199"))
    print(mask_account_card("MasterCard 7158 3007 3472 6758"))
    print(mask_account_card("Visa Classic 6831 9824 7673 7658"))
    print(mask_account_card("Счет 35383033474447895560"))

    print(get_data("2018-07-11T02:26:18.671407"))

    operations_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(filter_by_state(operations_list))
    print(filter_by_state(operations_list, "CANCELED"))

    print(sort_by_date(operations_list))
    print(sort_by_date(operations_list, False))
