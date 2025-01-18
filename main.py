from src.parser import extract_data

textbox_iterator = extract_data(r"F:\Descargas\Physical Security Class 01T.vtt")

for item in textbox_iterator:
    print(item)