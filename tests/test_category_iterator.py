import pytest


def test_iteration(category_iter):
    iter(category_iter)
    assert str(category_iter.category) == "Fruits, количество продуктов: 40 шт."
    assert category_iter.index == 0
    assert next(category_iter).name == "Green apple"
    assert next(category_iter).name == "Pineapple"
    with pytest.raises(StopIteration):
        next(category_iter)
        