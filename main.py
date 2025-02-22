from src.parser import extract_data
from pathlib import Path
import argparse

def main(file):

    _file = Path(file)

    textbox_iterator = extract_data(_file)

    with open(f'{_file.name}.txt','w', encoding='utf-8') as f:
        for item in textbox_iterator:
            if item.speaker == 'JOSE CARLOS RODRIGUEZ REYNA':
                f.write(f' {item.text}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file',type=str)
    args = parser.parse_args()
    main(args.file)