# importing Path class from pathlib module
from pathlib import Path

path = Path("packagedemo/subpackagedemo/__init__.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

path = path.with_name("file.txt")
print(path.absolute())