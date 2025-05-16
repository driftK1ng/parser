import json
from Writer import Writer

class JsonWriter(Writer):
    """Записывает полученные данные, в формате json

    Args:
        Writer (_type_): Абстрактный класс Writer
    """
    def write_in_file(self, data: list[dict[str, str]], path):
        """Форматирует данные и записывает их в файл

        Args:
            data (dict[int, dict[str, str]]): Список словарей данных, полученных из Reader 
            path (_type_): Путь для вывода
        """
        data = self._format_data(data)
        with open(path, mode="w", encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def _format_data(self, data: list[dict[str,str]]) -> dict[str,list[dict[str,str]]]:
        """Форматирует данные, приводя их к требуемому формату

        Args:
            data (list[dict[str,str]]): Список словарей значений

        Returns:
            dict[str,list[dict[str,str]]]: Словарь значений, отсортированный по отделам
        """
        allowed_fields = ['name', 'hours_worked', 'rate']
        formatted_data = {}
        for i in data:
            if formatted_data.get(i['department']) is None:
                formatted_data[i['department']] = []
            temp_data = {}
            for field in allowed_fields:
                temp_data[field] = i[field]
            temp_data['hours'] = temp_data['hours_worked']
            del temp_data['hours_worked']
            temp_data['payout'] = f'${int(temp_data['hours']) * int(temp_data['rate'])}'
            formatted_data[i['department']].append(temp_data)
        print(formatted_data)
        return formatted_data
