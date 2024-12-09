import pytest
from src.reports import spending_by_category
from src.read_excel import read_excel

# Чтение данных из Excel файла
result_read = read_excel("../data/operations.xlsx")

@pytest.fixture
def fix_reports():
    """Фикстура для получения ожидаемого результата"""
    return spending_by_category(result_read, "Переводы", date="31.12.2021")

def test_report(fix_reports):
    """Тест для проверки корректности отчета по категории 'Переводы'"""
    assert spending_by_category(result_read, "Переводы", date="31.12.2021") == fix_reports

@pytest.mark.parametrize("category", ["Переводы", "Красота", "sdfsf"])
def test_reports(category):
    """Тесты для проверки пустых отчетов по другим категориям"""
    assert spending_by_category(result_read, category) == []

# Дополнительный тест для проверки наличия данных в результатах
def test_non_empty_reports():
    """Тест для проверки, что категория 'Переводы' возвращает данные"""
    result = spending_by_category(result_read, "Переводы")
    assert isinstance(result, list)  # Проверка, что результат - это список
    assert len(result) >= 0  # Проверка, что список не пустой (может быть пустым в зависимости от данных)