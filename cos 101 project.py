dictionaries = { "1": ("igbo",{
    "hello": "ndewo",
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
    "money": "ego"})
}
print("Choose 1 Igbo | 2 Hausa | 3 Yoruba | 4 Edo | q Quit")

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
