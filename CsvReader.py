from Reader import Reader
from config import fields, salary_fields

class CsvReader(Reader):
    """Класс, который читает файлы .csv формата

    Args:
        Reader (_type_): Абстрактный класс
    """
    placement: dict[str, int]
    data: dict[str, str]

    def __init__(self):
        self.placement = fields.copy()
        for salary in salary_fields:
            self.placement[salary] = -1

    def read_file(self, paths: list[str]) -> list[dict[str,str]]:
        """Читает файлы, преобразуя их в список словарей

        Args:
            paths (list[str]): Список путей до файлов с данными

        Returns:
            list[dict[str,str]]: Преобразованный список словарей
        """
        data: list[dict[str,str]] = []
        for file_path in paths:
            try:
                with open(file_path, mode="r", encoding="utf-8") as file:
                    lines: str = file.read().splitlines()

                try:
                    self._read_header(lines.pop(0))
                    for line in lines:
                        data.append(self._read_body(line))
                except IndexError:
                    print(f"Файл {file_path} не содержит данных")

            except FileNotFoundError:
                print(f"Файл {file_path} не существует")
        return data

    def _read_header(self, header: str):
        """Читает заголовок .csv файла и определяет позиции каждого элемента

        Args:
            header (str): Заголовок .csv файла
        """
        titles: list[str] = header.split(',')
        for index, title in enumerate(titles):
            self._set_placement(title, index)
        self._clear_placement()

    def _read_body(self, body: str) -> dict[str,str]:
        """Читает одну строку с данными, возвращает словарь значений

        Args:
            body (str): Строка с данными

        Returns:
            dict[str,str]: Словарь значений из строки
        """
        positions: list[str] = body.split(",")
        item: dict[str,str] = {}
        for key, value in self.placement.items():
            item[key] = positions[value]
        return item

    def _set_placement(self, title: str, index: int):
        """Определяет позицию элемента данных

        Args:
            title (str): Элемент данных
            index (int): Позиция элемента
        """
        if self.placement.get(title) is not None:
            if title in salary_fields:
                title: str = "rate"
            self.placement[title] = index

    def _clear_placement(self):
        """Очищает неиспользуемые элементы
        """
        titles: list[str] = list(self.placement.keys()).copy()
        for title in titles:
            if self.placement[title] == -1:
                del self.placement[title]
