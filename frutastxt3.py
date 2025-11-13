frutas = ["Maçã, Banana, Manga"]

frutas.append("Uva e Abacaxi")

with open("frutas.txt" , "r") as arquivo:
        print(arquivo.read())
print(frutas)