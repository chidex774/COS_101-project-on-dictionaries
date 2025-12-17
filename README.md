words = {  
    "hello": "sannu",
    "thank you": "na gode",
    "please": "Don Allah",
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
    "school": "makaranta",
    "book": "littafi",
    "sun": "rana",
    "moon": "wata",
    "market": "kasuwa ",
    "work": "aiki",
    "money": "kudi"
}

print("Type an English word to translate to hausa")
while True:
    w = input("> ").lower()
    print(words.get(w, "Error: word not found"))# COS_101-project-on-dictionaries
