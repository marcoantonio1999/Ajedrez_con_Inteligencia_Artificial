"""
Configuración 
Establece la ruta para encontrar las imágenes
"""

from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relativeToAssets(path: str) -> Path:
    """Define la ruta de las imágenes"""
    return ASSETS_PATH / Path(path)