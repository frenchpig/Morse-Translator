import os
os.system('cls')

ejecutarsys = "y"

while ejecutarsys == "y":
    morselist = []
    print("--- Morse Code Translator ---")

    word = input("Enter a word: ")
    if len(word) == 0:
        worderror = True
        while worderror:
            print("Error: You must enter a word")
            word = input("Enter a word: ")
            if len(word)>0:
                worderror = False

    word = word.lower()

    os.system('cls')

    for i in range(len(word)):
        if word[i] == "a":
            morselist.append(".-")
        elif word[i] == "b":
            morselist.append("-...")
        elif word[i] == "c":
            morselist.append("-.-.")
        elif word[i] == "d":
            morselist.append("-..")
        elif word[i] == "e":
            morselist.append(".")
        elif word[i] == "f":
            morselist.append("..-.")
        elif word[i] == "g":
            morselist.append("--.")
        elif word[i] == "h":
            morselist.append("....")
        elif word[i] == "i":
            morselist.append("..")
        elif word[i] == "j":
            morselist.append(".---")
        elif word[i] == "k":
            morselist.append("-.-")
        elif word[i] == "l":
            morselist.append(".-..")
        elif word[i] == "m":
            morselist.append("--")
        elif word[i] == "n":
            morselist.append("-.")
        elif word[i] == "o":
            morselist.append("---")
        elif word[i] == "p":
            morselist.append(".--.")
        elif word[i] == "q":
            morselist.append("--.-")
        elif word[i] == "r":
            morselist.append(".-.")
        elif word[i] == "s":
            morselist.append("...")
        elif word[i] == "t":
            morselist.append("-")
        elif word[i] == "u":
            morselist.append("..-")
        elif word[i] == "v":
            morselist.append("...-")
        elif word[i] == "w":
            morselist.append(".--")
        elif word[i] == "x":
            morselist.append("-..-")
        elif word[i] == "y":
            morselist.append("-.--")
        elif word[i] == "z":
            morselist.append("--..")
        elif word[i] == "1":
            morselist.append(".----")
        elif word[i] == "2":
            morselist.append("..---")
        elif word[i] == "3":
            morselist.append("...--")
        elif word[i] == "4":
            morselist.append("....-")
        elif word[i] == "5":
            morselist.append(".....")
        elif word[i] == "6":
            morselist.append("-....")
        elif word[i] == "7":
            morselist.append("--...")
        elif word[i] == "8":
            morselist.append("---..")
        elif word[i] == "9":
            morselist.append("----.")
        elif word[i] == "0":
            morselist.append("-----")
        elif word[i] == ".":
            morselist.append(".-.-.-")
        elif word[i] == ",":
            morselist.append("--..--")
        elif word[i] == "?":
            morselist.append("..--..")

    translation = ""
    for i in range(len(morselist)):
        if i == 0:
            translation = translation + morselist[i]
        else:
            translation = translation + " / "
            translation = translation + morselist[i]


    print(f"--- Translation Finished ---\nEntered word: {word}\nMorse Translation: {translation}")
    pausa = input("Press Enter to continue...")
    os.system('cls')

    ejecutarsys = input("Do you want to translate something else? y o n\n")
    ejecutarsys = ejecutarsys.lower()
    os.system('cls')

