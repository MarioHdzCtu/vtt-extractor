def read_file(filepath: str):
    if not filepath.endswith('.vtt'):
        raise ValueError("Only VTT files are allowed")

    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()
