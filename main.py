from src.parser import extract_data

def main():

    textbox_iterator = extract_data(r"F:\Descargas\Physical Security Class 01T.vtt")

    with open('all_text.txt','w') as f:
        for item in textbox_iterator:
            if item.speaker == 'JOSE CARLOS RODRIGUEZ REYNA':
                content = item.text
                speaker = item.speaker
                f.write(item.text)

if __name__ == '__main__':
    main()