import random
import glob

def load_stages():
    files = sorted(glob.glob("hm*.txt"))
    stages = []
    for file in files:
        with open(file, encoding="utf-8") as f:
            stages.append(f.read())
    return stages

def load_words(filename="slova.txt"):
    with open(filename, encoding="utf-8") as f:
        return [w.strip().lower() for w in f if w.strip()]


def display_word(word, guessed):
    result = []
    for c in word:
        if c in guessed:
            result.append(c)
        else:
            result.append("_")

    return " ".join(result)

def play():
    words = load_words()
    stages = load_stages()

    word = random.choice(words)
    guessed_letters = set()
    wrong = 0
    max_wrong = len(stages) - 1

    print("Виселица")

    while wrong < max_wrong:
        print(stages[wrong])
        print(display_word(word, guessed_letters))

        letter = input("Введите букву: ").lower()

        if not letter.isalpha() or len(letter) != 1:
            print("Введите ОДНУ БУКВУ пж")
            continue

        if letter in guessed_letters:
            print("Уже была")
            continue

        guessed_letters.add(letter)

        if letter not in word:
            wrong += 1
        else:
            if all(c in guessed_letters for c in word):
                print("Победа")
                print("Слово:", word)
                return

    print(stages[wrong])
    print("Вас повесили :(")
    print("Слово было:", word)

play()
