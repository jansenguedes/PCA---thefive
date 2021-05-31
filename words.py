import random

def sortWords():
    global word
    global typeWord
    # game variables
    words = [
        ["LASANHA", "COMIDA"],
        ["PATO", "ANIMAL"],
        ["OVELHA", "ANIMAL"],
        ["GALO", "ANIMAL"],
        ["UVA", "FRUTA"],
        ["SORVETE", "DOCE"],
    ]

    selectedOption = random.choice(words)
    return selectedOption
