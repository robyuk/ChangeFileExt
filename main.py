from pathlib import Path

root=Path('files')

# Changes the suffix of all files in a directory
# Use glob or rglob instead of iterdir to recursively # change all files in a directory tree

for path in root.iterdir():
  if path.is_file:
    newname=path.stem + '.csv'
    path.rename(path.with_name(newname))