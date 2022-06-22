from pathlib import Path

root=Path('files')

for path in root.iterdir():
  if path.is_file:
    newname=path.stem + '.csv'
    path.rename(path.with_name(newname))