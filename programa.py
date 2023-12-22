import os
from mutagen import File

def obtener_metadatos_flac(ruta_archivo, numero_descripcion, numero_pista, total_archivos):
    try:
        # Cargar el archivo FLAC
        archivo_flac = File(ruta_archivo)

        # Verificar si el archivo es un archivo FLAC
        if archivo_flac and archivo_flac.mime[0] == "audio/flac":
            # Construir el número de pista con el total de archivos
            numero_pista_total = f"{numero_pista}/{total_archivos}"

            # Construir la ruta de la imagen
            ruta_imagen = os.path.join("Albums", f"{numero_descripcion}.jpg")

            # Crear un diccionario con los metadatos
            metadatos = {
                "archivo_musica": os.path.basename(ruta_archivo),
                "descripcion": numero_descripcion,
                "imagen": ruta_imagen,
                "genero": archivo_flac.get("genre", [""])[0],
                "titulo": archivo_flac.get("title", [""])[0],
                "artista": archivo_flac.get("artist", [""])[0],
                "album": archivo_flac.get("album", [""])[0],
                "numero_de_pista": numero_pista_total,
                "Año": archivo_flac.get("date", [""])[0][:4],
            }

            # Imprimir el diccionario en el formato deseado
            print("{")
            for clave, valor in metadatos.items():
                print(f'    "{clave}": "{valor}",')
            print("},")
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

        # Listar archivos en el directorio y ordenarlos por número de pista
        archivos_flac = sorted(
            [archivo for archivo in os.listdir(directorio) if archivo.lower().endswith(".flac")],
            key=lambda x: int(os.path.splitext(x)[0].split('_')[-1]) if '_' in os.path.splitext(x)[0] else float('inf')
        )

        if archivos_flac:
            # Hay archivos FLAC en el directorio
            print(f"Se encontraron archivos FLAC en el directorio {directorio}")
            
            # Iterar sobre los archivos y obtener metadatos
            for archivo in archivos_flac:
                ruta_completa = os.path.join(directorio, archivo)
                
                # Analizar el nombre del archivo para extraer información
                partes_nombre = os.path.splitext(archivo)[0].split('_')
                numero_descripcion = partes_nombre[0] if len(partes_nombre) >= 1 else ""
                numero_pista = partes_nombre[-1] if len(partes_nombre) >= 2 else ""
                
                # Obtener el total de archivos de la descripción
                total_archivos_descripcion = sum(1 for archivo in archivos_flac if numero_descripcion in archivo)

                obtener_metadatos_flac(ruta_completa, numero_descripcion, numero_pista, total_archivos_descripcion)
        else:
            # No hay archivos FLAC en el directorio
            print(f"No se encontraron archivos FLAC en el directorio {directorio}")

    except Exception as e:
        print(f"Error al procesar el directorio {directorio}: {e}")

# Ruta predefinida
directorio_predefinido = "/home/andrea/Documentos/GitHub/Musica18/public/Albums"

# Llamar a la función para extraer metadatos en el directorio predefinido
extraer_metadatos_en_directorio(directorio_predefinido)
