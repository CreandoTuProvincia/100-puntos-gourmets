import random
import hashlib

# Lista de vinos
vinos = [
    "Cirsion 2021",
    "L'Ermita 2022",
    "La Faraona 2022",
    "Pazo Señorans Selección de Añada 2014",
    "Poley Amontillado Convento Selección 1952",
    "Recaredo Homenatge a Josep Mata Capellades 2004",
    "Sorte O Soro 2023",
    "Tradición Oloroso VORS",
    "Vega Sicilia Único 2015"
]

# Fijar semilla
random.seed(20250610)

# Selección aleatoria
seleccion = random.sample(vinos, 8)

# Mostrar selección
print("Selección aleatoria:")
for i, vino in enumerate(seleccion, start=1):
    print(f"{i}. {vino}")

# Crear hash SHA-256
resultado = ",".join(seleccion).encode()
hash_verificacion = hashlib.sha256(resultado).hexdigest()

print("\nHash SHA-256 del resultado:")
print(hash_verificacion)
