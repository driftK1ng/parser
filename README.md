![Test Status](https://github.com/driftK1ng/parser/actions/workflows/ci.yml/badge.svg)

Для запуска используйте python3 main.py example.csv example_1.csv ... --report output.json

Для того, чтобы добавить еще один выходной формат, требуется: 
  - Определить новый класс от абстрактного класса Writer
  - Добавить строку с форматом файла в функцию select_writer в файле main.py
