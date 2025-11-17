import requests

# URL de la imagen (puedes cambiarla por cualquier enlace válido)
url = "https://collectionapi.metmuseum.org/api/collection/v1/iiif/45434/134438/main-image"

# Nombre del archivo local que se va a crear
file_name = "1.jpeg"

try:
    # Descargar el contenido de la imagen
    response = requests.get(url)
    response.raise_for_status()  # Lanza error si la descarga falla

    # Guardar el contenido como archivo local
    with open(file_name, "wb") as f:
        f.write(response.content)

    print(f"Saved '{file_name}'")
except Exception as e:
    print("Error downloading:", e)
