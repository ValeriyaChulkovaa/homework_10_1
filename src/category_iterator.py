from typing import Any

from src.category import Category


class CategoryIterator:
    def __init__(self, category: Category) -> None:
        self.category = category
        self.index = 0

    def __iter__(self) -> Any:
        self.index = 0
        return self

    def __next__(self) -> Any:
        if self.index < len(self.category.products_in_list):
            result = self.category.products_in_list[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
        