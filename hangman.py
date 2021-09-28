import os
import random 

def run():

    data = []
    palabra = []
    # Importar la lista
    with open("/home/vivianamg/dataScience/pythonIntermedio/HangmanGame/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append(line.strip("\n"))

    # Seleccionar una palabra de la lista
    random_word = random.choice(data)

    # Eliminar caracteres especiales
    table = random_word.maketrans("áéíóú", "aeiou")
    palabra = random_word.translate(table)

    print("Bienvenido al juego del ahorcado!")
   
    # Dividir la palabra en letras
    word = list(enumerate(palabra))
    
    dict_long = {i: " _ " for i in range(len(word))}
    print("".join(dict_long.values()))
    #print(dict_long)

    #Comparar la letra que ingresó el usuario "letra" con la palabra "word"
    
    while " _ " in dict_long.values():
        try:
        
            letra = input("Escoge una letra! ")
            if len(letra) > 1 or len(letra) == 0:
                raise ValueError ("Ingresa una (1) letra")
            assert letra.isalpha(), "Debes ingresar una letra"
            letra = letra.lower()

            for i in word:
                indice = i[0]
                letter = i[1]

                if letra == letter:
                    for key in dict_long:
                        if key == indice:
                            dict_long[key] = letter
                os.system("clear")
            print("".join(dict_long.values()))
            
        except ValueError as ve: 
            print(ve)
   
    print(" ")    
    print("Ganasate! ○( ＾皿＾)っ")        
if __name__ == "__main__":
    run()
