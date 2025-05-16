from abc import ABC, abstractmethod


class Reader(ABC):
    """Абстрактный класс для чтения файлов, требуется для определения единых интерфейсов
    """

    @abstractmethod
    def read_file(self, paths: list[str]) -> list[dict[str, str]]:
        """Метод, который должны содержать все дочерние классы

        Args:
            paths (str): Путь до файла

        Returns:
            list[dict[str, str]]: _description_
        """
