from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_empty() -> None:
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions(transactions: list) -> None:
    result = transaction_descriptions(transactions)

    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод со счета на счет"


def test_transaction_descriptions_empty() -> None:
    result = list(transaction_descriptions([]))
    assert result == []


def test_card_number_generator() -> None:
    result = card_number_generator(4523121464576, 4523121464574)
    assert next(result) == "0004 5231 2146 4574"
    assert next(result) == "0004 5231 2146 4575"
    assert next(result) == "0004 5231 2146 4576"


def test_card_number_generator_reverse() -> None:
    result = card_number_generator(5436334, 5436330)
    assert next(result) == "0000 0000 0543 6330"
    assert next(result) == "0000 0000 0543 6331"
    assert next(result) == "0000 0000 0543 6332"


def test_card_number_generator_full() -> None:
    result = card_number_generator(1257623415110000, 1257623415110003)
    assert next(result) == "1257 6234 1511 0000"
    assert next(result) == "1257 6234 1511 0001"
    assert next(result) == "1257 6234 1511 0002"
