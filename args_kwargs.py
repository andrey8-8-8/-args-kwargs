def single_root_words(root_word, *other_words):
    # Приводим root_word к нижнему регистру
    root_word = root_word.lower()

    # Создаем пустой список
    same_words = []

    # Перебираем слова из other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()

        # Проверяем условие: взаимное вхождение root_word и word_lower
        if root_word in word_lower or word_lower in root_word:
            same_words.append(word)  # Добавляем оригинальное слово в список

    # Возвращаем список same_words
    return same_words


# Вызов функции и вывод результата
result = single_root_words("синхрофазатрон", "Фаза", "трон", "Синх", "snow", "синтезатор")
print(result)
# Вывод:# Вывод: ['Фаза', 'трон', 'Синх']
