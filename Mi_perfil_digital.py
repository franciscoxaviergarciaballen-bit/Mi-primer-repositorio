#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Francisco xavier García Ballen"
edad = 15
estatura = 1.65
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("10__francisco")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "real love ", "artista": "gotay ", "duracion": "3:50"},
{"titulo": "en las noches frías", "artista": "Ñengo flow", "duracion": "4:15"},
{"titulo": "Una", "artista": "Bless", "duracion": "3:17"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
print(f"{cancion["titulo"]} - {cancion["artista"]})({cancion["duracion"]})min")
print ("----------------------------------")
