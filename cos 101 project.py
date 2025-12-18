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
print("Choose 1 Igbo | 2 Hausa | 3 Yoruba | 4 Edo")
while True:
    choice = input("> ").strip().lower()
    lang = dictionaries.get(choice)
    if not lang:
        print("Invalid choice. Try 1,2,3,4")
        continue

    name, words = lang
    print(f"Using {name}. Type a word")
    while True:
        w = input(f"{name}> ").strip().lower()
        print(words.get(w, "Error: word not found"))

