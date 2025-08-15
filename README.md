# Organizador de Archivos MCP

Este proyecto implementa un servidor MCP (Model Context Protocol) que proporciona herramientas para organizar automáticamente archivos en la carpeta de descargas (u otras carpetas) según su formato.

## Funcionalidades

### 1. Ordenar Archivos por Formato

Esta herramienta organiza automáticamente los archivos en subcarpetas según su extensión. Las categorías incluyen:

- documentos: PDF, Word, Excel, PowerPoint, etc.
- imagenes: JPG, PNG, GIF, etc.
- videos: MP4, AVI, MKV, etc.
- archivos_comprimidos: ZIP, RAR, 7Z, etc.
- programas: EXE, MSI, etc.
- audio: MP3, WAV, FLAC, etc.
- codigo: Python, JavaScript, HTML, etc.
- diseno: PSD, AI, XD, etc.
- datos: CSV, JSON, XML, etc.
- ebooks: EPUB, MOBI, etc.
- fuentes: TTF, OTF, etc.
- otros: Cualquier archivo que no encaje en las categorías anteriores

### 2. Analizar Carpeta

Esta herramienta analiza el contenido de una carpeta y proporciona estadísticas detalladas sobre los tipos de archivos, tamaños, fechas de modificación, etc.

## Requisitos

- Python 3.12 o superior
- Librería MCP (`uv add "mcp[cli]"`)

## Uso

### Iniciar el servidor

```bash
uv run mcp dev main.py
```

Esto iniciará un servidor MCP en el puerto 3000.

### Usar con el cliente MCP

Una vez que el servidor está en ejecución, puedes utilizar el cliente MCP para interactuar con él:

```bash
# Ordenar archivos en la carpeta de descargas
mcp tool "Ordenar Archivos por Formato"

# Ordenar archivos en una carpeta específica
mcp tool "Ordenar Archivos por Formato" --ruta_carpeta="C:/ruta/a/tu/carpeta"

# Analizar el contenido de la carpeta de descargas
mcp tool "Analizar Carpeta"

# Analizar una carpeta específica
mcp tool "Analizar Carpeta" --ruta_carpeta="C:/ruta/a/tu/carpeta"
```

## Personalización

Si deseas modificar las categorías o extensiones reconocidas, puedes editar el diccionario `categorias` en el archivo `main.py`.
