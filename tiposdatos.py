print("Clases V2 Kaylee Luevano")
# Zona de clase 
class Datos :
    #El constructor funcion
    def __init__(self,estatura, peso):
        self.estatura= estatura
        self.peso= peso
    def mostrarDatos(self):
        print(f"estatura: {self.estatura}  mts,  peso  {self.peso}kg: ")
    def mi_lista(self):
        celulares= ["Samsung", "ipod", "chafa"]
        print(celulares)
        for cel in celulares:
            print(cel)
    #tuplas
    def salones_tupla(self):
        compañeros = ("Jireh", "Daniel", "Mota")
        print(compañeros)
        for uncom in compañeros:
            print(uncom) 
    #Conjuntos
    def music_conjunto(self):
        guitarras = {"Acustica", "Electrica", "Electroacustica"}
        print(guitarras)
        for guitarra in guitarras:
            print(guitarra)
    #Diccionarios
    def comida_diccionario(self):
        papas =	{
        "Takis": "papitas",
        "Barcel": "Galletas",
        "vence": 2026
        }
        print(papas)
        for taki in papas:
            print(taki)

#Creacion de objeto info
info= Datos(1.60, 60.1)

#Utilizando el objeto
info.mostrarDatos()
print("lista de marcas de celulares Kaylee Luevano")
info.mi_lista()
info.salones_tupla()
info.music_conjunto()
info.comida_diccionario()