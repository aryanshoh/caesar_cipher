en_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
list(map(chr, range(ord('А'), ord('я')+1)))


def greeting():
    print("Привет! Это программа для шифрования и дешифрования шрифта Цезаря!")


def is_coding():
    answer = input('Вы хотите шифровать или дешифровать?\nДля шифрования введите "1", а для дешифрования - "0":\n')

    while True:
        if answer not in ('0', '1'):
            answer = input('Введите цифру 1 для выбора шифрования или 0 - для выбора дешифрования.\n')
        else:
            return True if answer == '1' else False


def choose_language():
    answer = input('В зависимости от языка алфавита, '
                   'введите "ru" для алфавита русского языка, или "en" для алфавита английского языка.\n')

    while True:
        if answer.strip() not in ('ru', 'en'):
            answer = input('Введите "ru" для алфавита русского языка, или "en" для алфавита английского языка.\n')
        else:
            return 'ru' if answer.strip() == 'ru' else 'en'


def chose_key(lang):
    if lang == 'ru':
        answer = input('Введите натурально число - величину шага сдвига (со сдвигом справа), - от 1 до 32.\n')

        while True:
            if answer.strip().isdigit() and int(answer) in range(1, 33):
                return int(answer.strip())
            else:
                answer = input('Неверный формат вводных данных. '
                               'Введите натурально число - величину шага сдвига (со сдвигом справа), - от 1 до 32.\n')

    else:
        answer = input('Введите натурально число - величину шага сдвига (со сдвигом справа), - от 1 до 26.\n')

        while True:
            if answer.strip().isdigit() and int(answer) in range(1, 27):
                return int(answer.strip())
            else:
                answer = input('Неверный формат вводных данных. '
                               'Введите натурально число - величину шага сдвига (со сдвигом справа), - от 1 до 26\n')


def get_text():
    return input('Введите текст, который нужно обработать.\n')


def coding_text(text, lang, key):
    n = 32 if lang == 'ru' else 26
    text = list(text)
    res = ''

    if lang == 'ru':
        for i in range(len(text)):
            if text[i] in (ru_alphabet[:32]):
                res += chr(ord("А") + (ord(text[i]) - ord("А") + n + key) % n)
            elif text[i] in (ru_alphabet[32:]):
                res += chr(ord("а") + (ord(text[i]) - ord("а") + n + key) % n)
            else:
                res += text[i]
    else:
        for i in range(len(text)):
            if text[i] in (en_alphabet[:26]):
                res += chr(ord("a") + (ord(text[i]) - ord("a") + n + key) % n)
            elif text[i] in (en_alphabet[26:]):
                res += chr(ord("A") + (ord(text[i]) - ord("A") + n + key) % n)
            else:
                res += text[i]

    return res

def decoding_text(text, lang, key):
    n = 32 if lang == 'ru' else 26
    text = list(text)
    res = ''

    if lang == 'ru':
        for i in range(len(text)):
            if text[i] in (ru_alphabet[:32]):
                res += chr(ord("А") + (ord(text[i]) - ord("А") + n - key) % n)
            elif text[i] in (ru_alphabet[32:]):
                res += chr(ord("а") + (ord(text[i]) - ord("а") + n - key) % n)
            else:
                res += text[i]
    else:
        for i in range(len(text)):
            if text[i] in (en_alphabet[:26]):
                res += chr(ord("a") + (ord(text[i]) - ord("a") + n - key) % n)
            elif text[i] in (en_alphabet[26:]):
                res += chr(ord("A") + (ord(text[i]) - ord("A") + n - key) % n)
            else:
                res += text[i]

    return res
