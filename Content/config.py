"""
Configuración del sistema de conversión PPTX a Markdown
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuración centralizada del sistema"""

    # API Configuration
    ANTHROPIC_API_KEY = ''
    ANTHROPIC_MODEL = 'claude-sonnet-4-5-20250929'  # Claude Sonnet 4.5 con soporte visual

    # Clasificación de slides
    VISUAL_KEYWORDS = [
        'diagram', 'table', 'schema', 'model', 'relationship', 'flow',
'architecture', 'graph', 'image', 'figure', 'erd', 'database',
'workflow', 'process', 'structure'
    ]

    # Umbrales para clasificación
    MIN_IMAGE_COUNT = 1  # Número mínimo de imágenes para considerar slide visual
    MIN_TEXT_LENGTH = 20  # Longitud mínima de texto para considerar slide de texto

    # Directorios
    BASE_DIR = Path(__file__).parent
    OUTPUT_DIR = BASE_DIR / 'markdown'

    # Costos estimados (USD por 1M tokens)
    COST_PER_INPUT_TOKEN = 3.00 / 1_000_000  # Claude Sonnet
    COST_PER_OUTPUT_TOKEN = 15.00 / 1_000_000

    # Tracking
    ENABLE_COST_TRACKING = True
    VERBOSE = True

    @classmethod
    def ensure_output_dir(cls):
        """Crea el directorio de salida si no existe"""
        cls.OUTPUT_DIR.mkdir(exist_ok=True)

    @classmethod
    def validate(cls):
        """Valida que la configuración sea correcta"""
        if not cls.ANTHROPIC_API_KEY:
            raise ValueError(
                "ANTHROPIC_API_KEY no encontrada. "
                "Crea un archivo .env con tu API key."
            )
