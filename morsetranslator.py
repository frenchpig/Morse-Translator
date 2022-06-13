import os
os.system('cls')

ejecutarsys = "s"

while ejecutarsys == "s":
    listamorse = []
    print("--- Traductor codigo morse ---")

    palabra = input("Ingrese una palabra: ")
    if len(palabra) == 0:
        errorpalabra = True
        while errorpalabra:
            print("Error: Debe ingresar una palabra")
            palabra = input("Ingrese una palabra: ")
            if len(palabra)>0:
                errorpalabra = False

    palabra = palabra.lower()

    os.system('cls')

    for i in range(len(palabra)):
        if palabra[i] == "a":
            listamorse.append(".-")
        elif palabra[i] == "b":
            listamorse.append("-...")
        elif palabra[i] == "c":
            listamorse.append("-.-.")
        elif palabra[i] == "d":
            listamorse.append("-..")
        elif palabra[i] == "e":
            listamorse.append(".")
        elif palabra[i] == "f":
            listamorse.append("..-.")
        elif palabra[i] == "g":
            listamorse.append("--.")
        elif palabra[i] == "h":
            listamorse.append("....")
        elif palabra[i] == "i":
            listamorse.append("..")
        elif palabra[i] == "j":
            listamorse.append(".---")
        elif palabra[i] == "k":
            listamorse.append("-.-")
        elif palabra[i] == "l":
            listamorse.append(".-..")
        elif palabra[i] == "m":
            listamorse.append("--")
        elif palabra[i] == "n":
            listamorse.append("-.")
        elif palabra[i] == "o":
            listamorse.append("---")
        elif palabra[i] == "p":
            listamorse.append(".--.")
        elif palabra[i] == "q":
            listamorse.append("--.-")
        elif palabra[i] == "r":
            listamorse.append(".-.")
        elif palabra[i] == "s":
            listamorse.append("...")
        elif palabra[i] == "t":
            listamorse.append("-")
        elif palabra[i] == "u":
            listamorse.append("..-")
        elif palabra[i] == "v":
            listamorse.append("...-")
        elif palabra[i] == "w":
            listamorse.append(".--")
        elif palabra[i] == "x":
            listamorse.append("-..-")
        elif palabra[i] == "y":
            listamorse.append("-.--")
        elif palabra[i] == "z":
            listamorse.append("--..")
        elif palabra[i] == "1":
            listamorse.append(".----")
        elif palabra[i] == "2":
            listamorse.append("..---")
        elif palabra[i] == "3":
            listamorse.append("...--")
        elif palabra[i] == "4":
            listamorse.append("....-")
        elif palabra[i] == "5":
            listamorse.append(".....")
        elif palabra[i] == "6":
            listamorse.append("-....")
        elif palabra[i] == "7":
            listamorse.append("--...")
        elif palabra[i] == "8":
            listamorse.append("---..")
        elif palabra[i] == "9":
            listamorse.append("----.")
        elif palabra[i] == "0":
            listamorse.append("-----")
        elif palabra[i] == ".":
            listamorse.append(".-.-.-")
        elif palabra[i] == ",":
            listamorse.append("--..--")
        elif palabra[i] == "?":
            listamorse.append("..--..")

    traduccion = ""
    for i in range(len(listamorse)):
        if i == 0:
            traduccion = traduccion + listamorse[i]
        else:
            traduccion = traduccion + " / "
            traduccion = traduccion + listamorse[i]


    print(f"--- Traduccion Finalizada ---\nPalabra ingresada: {palabra}\nTraduccion a morse: {traduccion}")
    pausa = input("Presione Enter para continuar...")
    os.system('cls')

    ejecutarsys = input("¿Desea traducir algo mas? s o n\n")
    ejecutarsys = ejecutarsys.lower()
    os.system('cls')
