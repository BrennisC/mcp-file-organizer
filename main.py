from mcp.server.fastmcp import FastMCP
import os
import shutil
from datetime import datetime
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("organizador_archivos.log"), logging.StreamHandler()],
)
logger = logging.getLogger("OrganizadorArchivos")

mcp = FastMCP()


@mcp.tool("Ordenar Archivos por Formato")
def ordenar_archivos(ruta_carpeta: str = None):
    if not ruta_carpeta:
        ruta_carpeta = os.path.join(os.path.expanduser("~"), "Downloads")

    logger.info(f"Iniciando organizacion de archivos en: {ruta_carpeta}")

    if not os.path.exists(ruta_carpeta):
        logger.error(f"La carpeta {ruta_carpeta} no existe")
        return {"error": f"La carpeta {ruta_carpeta} no existe"}

    # Categorías detalladas
    categorias = {
        "documentos": [
            ".pdf",
            ".doc",
            ".docx",
            ".txt",
            ".ppt",
            ".pptx",
            ".xls",
            ".xlsx",
            ".odt",
            ".rtf",
            ".md",
        ],
        "imagenes": [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
            ".tiff",
            ".svg",
            ".webp",
            ".ico",
            ".raw",
        ],
        "videos": [
            ".mp4",
            ".avi",
            ".mov",
            ".mkv",
            ".flv",
            ".wmv",
            ".m4v",
            ".3gp",
            ".webm",
            ".vob",
        ],
        "archivos_comprimidos": [
            ".zip",
            ".rar",
            ".7z",
            ".tar",
            ".gz",
            ".bz2",
            ".xz",
            ".iso",
            ".tgz",
        ],
        "programas": [
            ".exe",
            ".msi",
            ".deb",
            ".rpm",
            ".app",
            ".dmg",
            ".apk",
            ".jar",
            ".bat",
            ".sh",
        ],
        "audio": [
            ".mp3",
            ".wav",
            ".ogg",
            ".flac",
            ".aac",
            ".wma",
            ".m4a",
            ".opus",
            ".mid",
            ".aiff",
        ],
        "codigo": [
            ".py",
            ".js",
            ".html",
            ".css",
            ".java",
            ".php",
            ".c",
            ".cpp",
            ".cs",
            ".go",
            ".swift",
            ".ts",
            ".rb",
            ".sql",
            ".json",
            ".xml",
        ],
        "diseno": [
            ".psd",
            ".ai",
            ".xd",
            ".sketch",
            ".fig",
            ".cdr",
            ".indd",
            ".eps",
            ".blend",
        ],
        "datos": [
            ".csv",
            ".db",
            ".sqlite",
            ".sql",
            ".xlsx",
            ".accdb",
            ".json",
            ".xml",
            ".yaml",
            ".yml",
        ],
        "ebooks": [".epub", ".mobi", ".azw", ".azw3", ".fb2", ".djvu"],
        "fuentes": [".ttf", ".otf", ".woff", ".woff2", ".eot"],
    }

    total_archivos = 0
    archivos_movidos = 0
    resultados_por_categoria = {}

    # Crear carpetas si no existen
    for categoria in list(categorias.keys()) + ["otros"]:
        os.makedirs(os.path.join(ruta_carpeta, categoria), exist_ok=True)
        resultados_por_categoria[categoria] = 0

    archivos = [
        f
        for f in os.listdir(ruta_carpeta)
        if os.path.isfile(os.path.join(ruta_carpeta, f))
    ]
    total_archivos = len(archivos)
    logger.info(f"Se encontraron {total_archivos} archivos para organizar")
    total_archivos = len(archivos)

    for archivo in archivos:
        if archivo.startswith(".") or archivo == "organizador_archivos.log":
            continue

        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        extension = os.path.splitext(archivo)[1].lower()

        categoria_destino = "otros"
        for categoria, extensiones in categorias.items():
            if extension in extensiones:
                categoria_destino = categoria
                break

        # No mover si ya está en la carpeta correcta
        if os.path.dirname(ruta_archivo) == os.path.join(
            ruta_carpeta, categoria_destino
        ):
            logger.debug(f"Archivo {archivo} ya está en la carpeta correcta")
            continue

        carpeta_destino = os.path.join(ruta_carpeta, categoria_destino)
        ruta_destino = os.path.join(carpeta_destino, archivo)

        if os.path.exists(ruta_destino):
            nombre, ext = os.path.splitext(archivo)
            contador = 1
            while os.path.exists(
                os.path.join(carpeta_destino, f"{nombre}_{contador}{ext}")
            ):
                contador += 1
            ruta_destino = os.path.join(carpeta_destino, f"{nombre}_{contador}{ext}")

        try:
            shutil.move(ruta_archivo, ruta_destino)
            archivos_movidos += 1
            resultados_por_categoria[categoria_destino] += 1
            logger.info(
                f"Movido: {archivo} → {categoria_destino}/{os.path.basename(ruta_destino)}"
            )
        except Exception as e:
            logger.error(f"Error al mover {archivo}: {str(e)}")
            print(f"Error al mover {archivo}: {str(e)}")

    logger.info(
        f"Organizacion completada: {archivos_movidos} de {total_archivos} archivos organizados"
    )

    return {
        "mensaje": f"Se organizaron {archivos_movidos} de {total_archivos} archivos",
        "ruta": ruta_carpeta,
        "resumen": {
            "total": total_archivos,
            "organizados": archivos_movidos,
            "por_categoria": resultados_por_categoria,
        },
    }


@mcp.tool("Analizar Carpeta")
def analizar_carpeta(ruta_carpeta: str = None):
    if not ruta_carpeta:
        ruta_carpeta = os.path.join(os.path.expanduser("~"), "Downloads")

    logger.info(f"Analizando carpeta: {ruta_carpeta}")

    if not os.path.exists(ruta_carpeta):
        logger.error(f"La carpeta {ruta_carpeta} no existe")
        return {"error": f"La carpeta {ruta_carpeta} no existe"}

    # Categorías detalladas (igual que en ordenar_archivos)
    categorias = {
        "documentos": [
            ".pdf",
            ".doc",
            ".docx",
            ".txt",
            ".ppt",
            ".pptx",
            ".xls",
            ".xlsx",
            ".odt",
            ".rtf",
            ".md",
        ],
        "imagenes": [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
            ".tiff",
            ".svg",
            ".webp",
            ".ico",
            ".raw",
        ],
        "videos": [
            ".mp4",
            ".avi",
            ".mov",
            ".mkv",
            ".flv",
            ".wmv",
            ".m4v",
            ".3gp",
            ".webm",
            ".vob",
        ],
        "archivos_comprimidos": [
            ".zip",
            ".rar",
            ".7z",
            ".tar",
            ".gz",
            ".bz2",
            ".xz",
            ".iso",
            ".tgz",
        ],
        "programas": [
            ".exe",
            ".msi",
            ".deb",
            ".rpm",
            ".app",
            ".dmg",
            ".apk",
            ".jar",
            ".bat",
            ".sh",
        ],
        "audio": [
            ".mp3",
            ".wav",
            ".ogg",
            ".flac",
            ".aac",
            ".wma",
            ".m4a",
            ".opus",
            ".mid",
            ".aiff",
        ],
        "codigo": [
            ".py",
            ".js",
            ".html",
            ".css",
            ".java",
            ".php",
            ".c",
            ".cpp",
            ".cs",
            ".go",
            ".swift",
            ".ts",
            ".rb",
            ".sql",
            ".json",
            ".xml",
        ],
        "diseno": [
            ".psd",
            ".ai",
            ".xd",
            ".sketch",
            ".fig",
            ".cdr",
            ".indd",
            ".eps",
            ".blend",
        ],
        "datos": [
            ".csv",
            ".db",
            ".sqlite",
            ".sql",
            ".xlsx",
            ".accdb",
            ".json",
            ".xml",
            ".yaml",
            ".yml",
        ],
        "ebooks": [".epub", ".mobi", ".azw", ".azw3", ".fb2", ".djvu"],
        "fuentes": [".ttf", ".otf", ".woff", ".woff2", ".eot"],
    }

    # Invertir el diccionario para búsqueda rápida
    extension_a_categoria = {}
    for categoria, extensiones in categorias.items():
        for extension in extensiones:
            extension_a_categoria[extension] = categoria

    # Estadísticas por categoría y extensión
    stats = {
        "total_archivos": 0,
        "total_carpetas": 0,
        "espacio_usado": 0,  # en bytes
        "por_categoria": {},
        "por_extension": {},
        "archivos_mas_grandes": [],
        "archivos_mas_recientes": [],
    }

    # Inicializar contadores por categoría
    for categoria in list(categorias.keys()) + ["otros"]:
        stats["por_categoria"][categoria] = {"cantidad": 0, "espacio": 0}

    # Recorrer archivos y carpetas
    for item in os.listdir(ruta_carpeta):
        ruta_item = os.path.join(ruta_carpeta, item)

        if os.path.isfile(ruta_item):
            stats["total_archivos"] += 1
            tamano = os.path.getsize(ruta_item)
            stats["espacio_usado"] += tamano

            fecha_modificacion = os.path.getmtime(ruta_item)
            extension = os.path.splitext(item)[1].lower()

            # Actualizar estadísticas por extensión
            if extension not in stats["por_extension"]:
                stats["por_extension"][extension] = {
                    "cantidad": 0,
                    "espacio": 0,
                    "categoria": extension_a_categoria.get(extension, "otros"),
                }

            stats["por_extension"][extension]["cantidad"] += 1
            stats["por_extension"][extension]["espacio"] += tamano

            # Actualizar estadísticas por categoría
            categoria = extension_a_categoria.get(extension, "otros")
            stats["por_categoria"][categoria]["cantidad"] += 1
            stats["por_categoria"][categoria]["espacio"] += tamano

            # Guardar para los archivos más grandes
            stats["archivos_mas_grandes"].append(
                {"nombre": item, "tamano": tamano, "ruta": ruta_item}
            )

            # Guardar para los archivos más recientes
            stats["archivos_mas_recientes"].append(
                {"nombre": item, "fecha": fecha_modificacion, "ruta": ruta_item}
            )

        elif os.path.isdir(ruta_item):
            stats["total_carpetas"] += 1

    # Ordenar y limitar listas
    stats["archivos_mas_grandes"] = sorted(
        stats["archivos_mas_grandes"], key=lambda x: x["tamano"], reverse=True
    )[:10]

    stats["archivos_mas_recientes"] = sorted(
        stats["archivos_mas_recientes"], key=lambda x: x["fecha"], reverse=True
    )[:10]

    # Convertir timestamps a strings legibles
    for archivo in stats["archivos_mas_recientes"]:
        archivo["fecha"] = datetime.fromtimestamp(archivo["fecha"]).strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    stats["por_extension"] = {
        k: v for k, v in stats["por_extension"].items() if v["cantidad"] > 0
    }

    logger.info(
        f"Análisis completado: {stats['total_archivos']} archivos en {stats['total_carpetas']} carpetas"
    )

    return {
        "mensaje": f"Análisis completado para {ruta_carpeta}",
        "ruta": ruta_carpeta,
        "estadisticas": stats,
    }
