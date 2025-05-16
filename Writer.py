from abc import ABC, abstractmethod


class Writer(ABC):
    """Абстрактный класс для записи в файлы, требуется для определения единых интерфейсов
    """
    @abstractmethod
    def write_in_file(self, data: list[dict[str, str]], path: str):
        """Определяет интерфейс для дочерних классов, для записи данных в файл

        Args:
            data (list[dict[str, str]]): Данные, полученные из Reader
            path (str): Путь до выходного файла
        """
