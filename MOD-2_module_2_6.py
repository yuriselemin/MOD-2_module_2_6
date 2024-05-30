

# Домашняя работа по уроку "Пространство имен и способы вызова функции"




def single_root_words(root_word, *other_words):

    same_words = []

    for word in other_words:

        if word.lower().count(root_word.lower()) > 0:
            same_words.append(word)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)


'''
______________________________________________________________________________________________________________
в данной задаче вторым ркзультатом выходит пустой список
предполагаю что параметр root_word должен быть короче параметров other_words
так как является вложенной строкой.
ниже проводил проверку предположения котрая дала положительный результат.
ВОПРОС: как в решении задачи должно получиться ['Able', 'Disable']  и почему 'Mable' не вошло в этот список,
хотя имеет тот же корень  -Able- ?
______________________________________________________________________________________________________________
'''


def single_root_words(root_word, *other_words):

    same_words = []

    for word in other_words:
    
        if word.lower().count(root_word.lower()) > 0:
            same_words.append(word)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)
result3 = single_root_words('Able', 'Disablement', 'Mable', 'Disable', 'Bagel')
print(result3)
result4 = single_root_words("Молот", "Молоточек", "Молоток", "Лимон", "Апельсин", "Грейпфрут")
print(result4)
result5 = single_root_words("молот", "Молоточек", "молоток", "Лимон", "Апельсин", "Грейпфрут")
print(result5)


















