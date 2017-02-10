'''
Курс "Информатика на Python 3" на ФБМФ.
Работа №16, задача 2, шифр Цезаря.
'''

class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        self._encode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
        self._decode = {}
        self._decode = {v:k for k, v in self._encode.items()}

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        return ''.join([self._decode.get(char, char) for char in line])


if __name__ == '__main__':
    with open('ex_2.txt', 'r') as input_file:
        lines = input_file.readlines()

    # Подбираем ключ просмотром первой строки
    for key in range(len(Caesar.alphabet)):
        cipher = Caesar(key)
        print(key, cipher.decode(lines[0]))

    # Определив верный ключ, прочитав первую строку, дешифруем весь текст
    cipher = Caesar(14)

    with open('ex_2_output.txt', 'w') as output_file:
        output_file.write('\n'.join([cipher.decode(line) for line in lines]))
