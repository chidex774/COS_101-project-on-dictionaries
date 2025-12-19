dictionaries = { "1": ("huasa",{
    "hello": "sannu",
    "thank you": "na gode",
    "please": "don Allha",
    "yes": "iya",
    "no": "a'a",
    "water": "ruwa",
    "food": "abinci",
    "house": "gida",
    "friend": "aboki",
    "love": "soyayya",
    "mother": "uwa",
    "father": "uba",
    "child": "yaro",
    "school": "mkaranta",
    "book": "lattafi",
    "sun": "rana",
    "moon": "wata",
    "market": "kasuwa",
    "work": "aiki",
    "money": "kudi"}), "2":("igbo",{ "hello": "ndewo",
    "thank you": "daalụ",
    "please": "biko",
    "yes": "ee",
    "no": "mba",
    "water": "mmiri",
    "food": "nri",
    "house": "ụlọ",
    "friend": "enyi",
    "love": "ịhụnanya",
    "mother": "nne",
    "father": "nna",
    "child": "nwa",
    "school": "ụlọ akwụkwọ",
    "book": "akwụkwọ",
    "sun": "anyanwụ",
    "moon": "ọnwa",
    "market": "ahịa",
    "work": "ọrụ",
    "money": "ego"}), "3":("Yoruba",{
    "hello": "báwo",
    "thank you": "ẹ ṣé",
    "please": "jọ̀wọ́",
    "yes": "béẹ̀ni",
    "no": "rárá",
    "water": "omi",
    "food": "oúnjẹ",
    "house": "ilé",
    "friend": "ọ̀rẹ́",
    "love": "ìfẹ́",
    "mother": "ìyá",
    "father": "bàbá",
    "child": "ọmọ",
    "school": "ilé-ẹ̀kọ́",
    "book": "ìwé",
    "sun": "oorun",
    "moon": "oṣùpá",
    "market": "ọjà",
    "work": "iṣẹ́",
    "money": "owó",})
}
print("Choose 1 Hausa | 2 igbo  | 3 Yoruba | q Quit")

while True:
    choice = input("Choose language > ").strip().lower()
    if choice in ("q", "quit"):
        print("Goodbye.")
        break

    lang = dictionaries.get(choice)
    if not lang:
        print("Invalid choice. Try 1, 2, 3, 4 or q.")
        continue

    name, words = lang
    print(f"Using {name}. Type an English word to translate.")
    print("Type 'back' to choose another language, or 'q' to quit.")

    while True:
        w = input(f"{name}> ").strip().lower()
        if w in ("q", "quit"):
            print("Goodbye.")
            exit()
        if w == "back":
            break
        print(words.get(w, "Error: word not found"))




