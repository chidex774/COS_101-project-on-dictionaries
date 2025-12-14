words = {
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
    "money": "ego"
}

print("Type an English word to translate to Igbo")
while True:
    w = input("> ").lower()
    print(words.get(w, "Error: word not found"))
