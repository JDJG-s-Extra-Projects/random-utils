import pathlib

current_directory = pathlib.Path(__file__).parent
files = current_directory.rglob("*")

biggest_files = {}
for file in files:
    if file.is_file():
        biggest_files.setdefault(file.suffix, []).append(file)

for file_type, file_list in biggest_files.items():
    file_list.sort(key=lambda path: path.stat().st_size, reverse=True)
    print(f"{file_type} files:")
    for file in file_list[:3]:
        print(f"{file}: {file.stat().st_size} bytes")
    print()

