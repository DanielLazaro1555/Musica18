import os
from mutagen import File

def obtener_metadatos_flac(ruta_archivo):
    try:
        # Cargar el archivo FLAC
        archivo_flac = File(ruta_archivo)

        # Verificar si el archivo es un archivo FLAC
        if archivo_flac and archivo_flac.mime[0] == "audio/flac":
            # Imprimir metadatos
            print(f"Metadatos del archivo FLAC ({ruta_archivo}):")
            for clave, valor in archivo_flac.items():
                print(f"{clave}: {valor}")
            print("------------------------")
        else:
            print(f"{ruta_archivo} no es un archivo FLAC válido.")
    except Exception as e:
        print(f"Error al obtener metadatos de {ruta_archivo}: {e}")

def extraer_metadatos_en_directorio(directorio):
    try:
        # Verificar si el directorio existe
        if not os.path.exists(directorio):
            print(f"El directorio {directorio} no existe.")
            return

        # Listar archivos en el directorio
        archivos_flac = [archivo for archivo in os.listdir(directorio) if archivo.lower().endswith(".flac")]

        if archivos_flac:
            # Hay archivos FLAC en el directorio
            print(f"Se encontraron archivos FLAC en el directorio {directorio}")
            
            # Iterar sobre los archivos y obtener metadatos
            for archivo in archivos_flac:
                ruta_completa = os.path.join(directorio, archivo)
                obtener_metadatos_flac(ruta_completa)
        else:
            # No hay archivos FLAC en el directorio
            print(f"No se encontraron archivos FLAC en el directorio {directorio}")

    except Exception as e:
        print(f"Error al procesar el directorio {directorio}: {e}")

# Solicitar al usuario el directorio
directorio_ingresado = input("Ingrese el directorio que contiene los archivos FLAC: ")

# Llamar a la función para extraer metadatos en el directorio proporcionado
extraer_metadatos_en_directorio(directorio_ingresado)
