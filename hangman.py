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
    #print(word)
    dict_long = {i: " _ " for i in range(len(word))}
    print("".join(dict_long.values()))
    #print(dict_long)

    #Comparar la letra que ingresó el usuario "letra" con la palabra "word"
    
    while " _ " in dict_long.values():
        letra = input("Escoge una letra! ")

        for i in word:
            indice = i[0]
            letter = i[1]

            if letra == letter:
                for key in dict_long:
                    if key == indice:
                        dict_long[key] = letter
        print("".join(dict_long.values()))
   
    print(" ")    
    print("Ganasate! ○( ＾皿＾)っ")        
if __name__ == "__main__":
    run()
