import random 

def run():

    data = []
    palabra = []
    # Import the list
    with open("/home/vivianamg/dataScience/pythonIntermedio/HangmanGame/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append(line.strip("\n"))

    # Select a word from the list
    random_word = random.choice(data)

    # Eliminar caracteres especiales
    table = random_word.maketrans("áéíóú", "aeiou")
    palabra = random_word.translate(table)

    # Bienvenida al usuario
    print("Bienvenido al juego del ahorcado!")
   
    # Dividir la palabra en letras
    word = list(enumerate(palabra))
    print(word)
    dict_long = {i: " _ " for i in range(len(word))}
    print("".join(dict_long.values()))
    print(dict_long)

    letra = input("Escoge una letra! ")
    

if __name__ == "__main__":
    run()
