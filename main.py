import re

def custom_sort_key(word):
    """Функція ключа для сортування: українські слова перші, англійські - другі."""
    if re.match(r'^[а-яА-ЯёЄєІіЇїҐґ]+$', word):
        return (0, word.lower())
    elif re.match(r'^[a-zA-Z]+$', word):
        return (1, word.lower())
    else:
        return (2, word.lower())

def extract_and_sort_words_from_first_sentence(filename):
    """Витягує перше речення з файлу, розбиває на слова і сортує їх за мовами."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

            first_sentence_match = re.match(r'(.+?[.!?])', text)
            if first_sentence_match:
                first_sentence = first_sentence_match.group(1)
                print(f"Перше речення: {first_sentence}")

                # Розбиваємо речення на слова
                words = re.findall(r'\b\w+\b', first_sentence)

                # Сортуємо всі слова за кастомним ключем (укр - англ)
                sorted_words = sorted(words, key=custom_sort_key)
                return sorted_words
            else:
                print("Не вдалося знайти жодне речення.")
                return []

    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []

def main():
    filename = 'text.txt'
    sorted_words = extract_and_sort_words_from_first_sentence(filename)

    if sorted_words:
        print("Слова в алфавітному порядку:", sorted_words)
        print("Кількість слів:", len(sorted_words))

if __name__ == "__main__":
    main()
