from argparse import ArgumentParser, Namespace
from CsvReader import CsvReader
from Reader import Reader
from Writer import Writer
from JsonWriter import JsonWriter


def get_args() -> Namespace:
    """Обрабатывает входящие аргументы и возвращает Namespace аргументов

    Returns:
        Namespace: Namespace с аргументами
    """
    parser = ArgumentParser()
    parser.add_argument('paths', nargs='+')
    parser.add_argument('--report', type=str)
    return parser.parse_args()

def select_writer(path: str) -> Writer:
    """ В зависимости от разрешения вывода, определяет класс, который будет записывать данные

    Args:
        path (str): Путь до файла

    Returns:
        Writer: Записывающий данные класс от интерфейса Writer
    """
    if len(path.split("/")) > 1:
        formats = path.split("/")[0].split(".")[1]
    else:
        formats = path.split(".")[1]
    match (formats):
        case "json": return JsonWriter()


if __name__ == "__main__":
    args: Namespace = get_args()
    reader: Reader = CsvReader()
    writer: Writer = select_writer(args.report)
    data = reader.read_file(args.paths)
    writer.write_in_file(data, args.report)
