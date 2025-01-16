from src.extractor import read_file
from src.models.textblock import TextBox

def extract_data(filepath: str):
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
                textbox_list.append(TextBox(**d))
                d = {}
        else:
            d['subtitle_cue'] = line

    print(textbox_list[0].text)
    print(textbox_list[0].speaker)