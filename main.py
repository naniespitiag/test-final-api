# Importamos requests para conectarnos a la API
import requests
import json

# Función que recibe un número y devuelve el plato correspondiente
def dish_fetch(num):
    # URL de la API de platos típicos
    url = "https://api-colombia.com/api/v1/TypicalDish"
    
    # Hacemos la petición GET a la API
    response = requests.get(url)
    
    # Convertimos la respuesta JSON en una lista de diccionarios
    dishes = json.loads(response.content)
    
    # Devolvemos el plato según el número ingresado, o un error si el número es inválido
    if 0 <= num < len(dishes):
        return dishes[num]
    else:
        return {"error": "Número fuera de rango"}

# Función principal del programa
def main():
    print("¡Hola! Vamos a ver un plato típico de Colombia.")
    
    # Pedimos al usuario que ingrese un número
    num = int(input("Ingrese un número de plato: "))
    
    # Obtenemos el plato con dish_fetch
    plato = dish_fetch(num)
    
    # Mostramos el plato
    print(plato)

# Esto asegura que main() solo se ejecute si corremos este archivo directamente
if __name__ == "__main__":
    main()
