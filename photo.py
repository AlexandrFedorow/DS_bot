import requests
import config
import jpg_convert


"""тут происходит скачивание пикчи через url ссылку"""

def get_file(url):
    response = requests.get(url, stream=True)
    return response


def save_data(name, file_data):
    file = open(name, 'bw') # Бинарный режим, изображение передається байтами
    for chunk in file_data.iter_content(4096): # Записываем в файл по блочно данные
        file.write(chunk)


def get_name(url):
    name = url.split('/')[-1]
    config.PNAME = 'img/' + name
    return 'img/' + name


def run(name):
    save_data(get_name(name), get_file(name))
    jpg_convert.convert()

