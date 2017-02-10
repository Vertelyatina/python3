'''
Курс "Информатика на Python 3" на ФБМФ.
Работа №16, задача 4, шифр Виженера.
'''

class Vigenere:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, keyword):
        # Каждой букве ставим в соответствие её порядковый номер в алфавите
        self.alphaindex = {ch: index for index, ch in enumerate(self.alphabet)}
        # Шифруем кодовое слово с помощью этих индексов
        self.key = [self.alphaindex[letter] for letter in keyword.lower()]

    def caesar(self, letter, shift):
        if letter in self.alphaindex:  # Строчная буква
            index = (self.alphaindex[letter] + shift)%len(self.alphabet)
            cipherletter = self.alphabet[index]
        elif letter.lower() in self.alphaindex:  # Заглавная буква
            cipherletter = self.caesar(letter.lower(), shift).upper()
        else:
            cipherletter = letter
        return cipherletter

    def encode(self, line):
        ciphertext = []
        for i, letter in enumerate(line):
            shift = self.key[i % len(self.key)]
            cipherletter = self.caesar(letter, shift)
            ciphertext.append(cipherletter)
        return ''.join(ciphertext)

    def decode(self, line):
        # От энкодинга отличается только вычитанием шага
        text = []
        for i, letter in enumerate(line):
            shift = self.key[i % len(self.key)]
            original_letter = self.caesar(letter, len(self.alphabet)-shift)
            text.append(original_letter)
        return ''.join(text)

if __name__ == '__main__':

    

    keyword = input('keyword=')
    cipher = Vigenere(keyword)

    # line = input()
    # while line != '.':
    #     print(cipher.decode(line))
    #     line = input()

    with open('Vigenere.txt', 'r') as input_file:
        data = input_file.readlines()

    with open('Vigenere_output.txt', 'a') as output_file:
        for line in data:
            output_file.write(cipher.decode(line))
