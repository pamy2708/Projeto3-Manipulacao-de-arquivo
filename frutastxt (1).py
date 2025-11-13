frutas = input("Maçã, Banana, Manga")

with open("frutas.txt", "a") as arquivo:
    arquivo.write(frutas)




