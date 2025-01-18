from src.extractor import read_file
from src.models.textblock import TextBox
from typing import Iterator

def extract_data(filepath: str) -> Iterator[TextBox]:
    file_content = read_file(filepath)
    title = next(file_content)
    textbox_list = []
    d = {}
    for line in file_content:
        if line.startswith('<v'):
            d['content'] = line
        elif '-->' in line:
            d['timestamp_str'] = line
        elif line == '':
            if d:
                yield TextBox(**d)
                # textbox_list.append()
                d = {}
        else:
            d['subtitle_cue'] = line
