import pdfplumber
from gtts import gTTS
from art import tprint
from pathlib import Path


def converter(file_path, language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'Done! mp3 file saved.'

    else:
        return 'Couldn\'t find the file!'


def main():
    tprint('PDF TO MP3', font='bulbhead')
    file_path = input("\nEnter a file's path: ")
    language = input("Choose language('en' or 'ru'): ")
    print(converter(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
