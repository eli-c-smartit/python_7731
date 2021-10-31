from pathlib import Path

my_directory = Path("db")
my_directory.mkdir()
print(my_directory.absolute())

