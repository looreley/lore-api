import requests
import json

if __name__ == "__main__":
    request = requests.get(
        "https://api.datos.gob.mx/v1/condiciones-atmosfericas"
        )

    if request.status_code == 200:
        print(request.json())
        for i in request.json()["results"]:
             print("------------------------------ ")
             print("nombre de ciudad: ", i["name"] )
             print("La temperatura: ", i["tempc"] )
             print("Longitud es : ", i["longitude"] )
             print("velocidad del viento  es : ", i["windspeedkm"] )
             print("La descripcion del cielo larga es: ", i["skydescriptionlong"] )
             print("------------------------------ ")
       
    
        with open('datos.json', 'w') as file:
            json.dump(request.json()["results"], file)
            