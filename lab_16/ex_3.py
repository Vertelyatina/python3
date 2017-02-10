'''
Курс "Информатика на Python 3" на ФБМФ.
Работа №16, задача 3, частотный анализ текста.
'''

class FrequentAnalysis:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, text, correct_order):

        # Считаем вхождения русских букв в текст независимо от регистра
        counter = [text.lower().count(letter) for letter in self.alphabet]
        total_length = sum(counter)

        # Делаем из количества букв частоту встречаемости с округлением до 5 знаков
        values = [round(number/total_length, 5) for number in counter]

        # Создаем список букв, встречающихся в тексте, в порядке убывания встречаемости
        frequencies = list(zip(values, list(self.alphabet)))
        self.frequencies = sorted(frequencies, reverse=True)
        sorted_alphabet = [item[1] for item in self.frequencies]
        self.sorted_alphabet = sorted_alphabet + [letter.upper() for letter in sorted_alphabet]

        # Создаем словарь для замены, учитывая верхний регистр
        self.correct_order = correct_order + [letter.upper() for letter in correct_order]
        self.substitution_dictionary = dict(zip(self.sorted_alphabet, self.correct_order))

    def decode(self, text):
        output = []
        for letter in text:
            if letter in self.substitution_dictionary.keys():
                output.append(self.substitution_dictionary[letter])
            else:
                output.append(letter)
        return ''.join(output)

if __name__ == '__main__':

    with open('ex_3.txt', 'r') as input_file:
        lines = input_file.readlines()
    data = ''.join(lines)

    '''with open('table.txt', 'r') as table:
        frequency_default = []
        table = table.readlines()
        for line in table:
            line = tuple(line.split())
            frequency_default.append(line[1])'''

    # К сожалению, порядок полусинтетический: таблица из Википедии хороша, но разница в
    # сотые доли процента сказывается на порядке букв и сильно снижает понятность текста.
    # Также подпортили картину специальные слова, такие как "шиФр" и "алФавит", например
    frequency_default = ['а', 'о', 'и', 'е', 'т', 'в', 'н', 'р', 'л', 'с',
                         'м', 'к', 'п', 'ы', 'з', 'ф', 'д', 'я', 'ш', 'б',
                         'ь', 'у', 'г', 'ч', 'ж', 'й', 'х', 'ц', 'ю', 'э',
                         'ё', 'щ', 'ъ']

    cipher = FrequentAnalysis(data, frequency_default)
    print(cipher.decode(data))

    with open('ex_3_output.txt', 'w') as output_file:
         output_file.write(cipher.decode(data))
