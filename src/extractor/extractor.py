import pathlib
def read_file(filepath: pathlib.Path):
    if not filepath.name.endswith('.vtt'):
        raise ValueError("Only VTT files are allowed")

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()
