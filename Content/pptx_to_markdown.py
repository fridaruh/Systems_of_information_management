#!/usr/bin/env python3
"""
Sistema de Conversión de PPTX a Markdown con Optimización de Costos

Convierte presentaciones PowerPoint a archivos Markdown, procesando visualmente
solo los slides que contienen diagramas e imágenes para minimizar costos de API.
"""
import argparse
import sys
from pathlib import Path
from typing import Optional

from config import Config
from slide_classifier import SlideClassifier
from text_extractor import TextExtractor
from visual_processor import VisualProcessor
from markdown_generator import MarkdownGenerator


class PPTXToMarkdownConverter:
    """Conversor principal que orquesta todo el pipeline"""

    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
        self.classifier = SlideClassifier(self.config)
        self.text_extractor = TextExtractor(self.config)
        self.visual_processor = VisualProcessor(self.config)
        self.markdown_generator = MarkdownGenerator(self.config)

    def convert(self, pptx_path: str) -> str:
        """
        Convierte un archivo PPTX a Markdown

        Args:
            pptx_path: Ruta al archivo PPTX

        Returns:
            Ruta del archivo markdown generado
        """
        pptx_path = Path(pptx_path)

        if not pptx_path.exists():
            raise FileNotFoundError(f"Archivo no encontrado: {pptx_path}")

        if not pptx_path.suffix.lower() == '.pptx':
            raise ValueError(f"El archivo debe ser .pptx: {pptx_path}")

        print(f"\n{'='*60}")
        print(f"Convirtiendo: {pptx_path.name}")
        print(f"{'='*60}\n")

        # Paso 1: Clasificar slides
        print("📊 Clasificando slides...")
        classifications = self.classifier.classify_presentation(str(pptx_path))
        stats = self.classifier.get_statistics(classifications)

        print(f"\n   Total: {stats['total']} slides")
        print(f"   Texto: {stats['text']} slides ({stats['text_percentage']:.1f}%)")
        print(f"   Visual: {stats['visual']} slides")

        # Separar slides por tipo
        text_slides = [num for num, cls in classifications.items() if cls == 'text']
        visual_slides = [num for num, cls in classifications.items() if cls == 'visual']

        # Paso 2: Extraer texto (sin costo)
        print(f"\n🔤 Extrayendo texto de {len(text_slides)} slides...")
        text_data = self.text_extractor.extract_from_presentation(
            str(pptx_path),
            text_slides
        )

        # Paso 3: Procesar slides visuales (con API)
        print(f"\n🎨 Procesando {len(visual_slides)} slides visuales con Claude API...")
        if visual_slides:
            visual_data = self.visual_processor.process_visual_slides(
                str(pptx_path),
                visual_slides
            )

            # Mostrar costos
            cost_info = self.visual_processor.get_cost_estimate()
            print(f"\n💰 Costos de API:")
            print(f"   Input tokens: {cost_info['input_tokens']:,}")
            print(f"   Output tokens: {cost_info['output_tokens']:,}")
            print(f"   Costo total: ${cost_info['total_cost_usd']:.4f} USD")
        else:
            visual_data = {}
            cost_info = {
                'input_tokens': 0,
                'output_tokens': 0,
                'total_cost_usd': 0.0
            }

        # Paso 4: Generar markdown
        print(f"\n📝 Generando archivo markdown...")
        processing_stats = {
            'total_slides': stats['total'],
            'text_slides': stats['text'],
            'visual_slides': stats['visual'],
            'text_percentage': stats['text_percentage'],
            'api_cost': cost_info
        }

        output_path = self.markdown_generator.generate_markdown(
            pptx_path.name,
            text_data,
            visual_data,
            classifications,
            processing_stats
        )

        print(f"\n{'='*60}")
        print(f"✅ Conversión completada exitosamente")
        print(f"{'='*60}")
        print(f"\nArchivo generado: {output_path}")
        print(f"Optimización de costos: {stats['text_percentage']:.1f}% de slides "
              f"procesados sin API")

        return output_path

    def convert_batch(self, directory: Path, pattern: str = "*.pptx") -> None:
        """
        Convierte múltiples archivos PPTX en un directorio

        Args:
            directory: Directorio con archivos PPTX
            pattern: Patrón de archivos a procesar
        """
        pptx_files = list(directory.glob(pattern))

        if not pptx_files:
            print(f"No se encontraron archivos {pattern} en {directory}")
            return

        print(f"\n🎯 Encontrados {len(pptx_files)} archivos para convertir\n")

        total_cost = 0.0
        successful = 0
        failed = 0

        for pptx_file in pptx_files:
            try:
                self.convert(str(pptx_file))
                successful += 1

                # Acumular costos
                if hasattr(self.visual_processor, 'get_cost_estimate'):
                    cost = self.visual_processor.get_cost_estimate()
                    total_cost += cost['total_cost_usd']

            except Exception as e:
                print(f"\n❌ Error procesando {pptx_file.name}: {e}")
                failed += 1
                continue

        # Resumen final
        print(f"\n{'='*60}")
        print(f"RESUMEN DEL BATCH")
        print(f"{'='*60}")
        print(f"Exitosos: {successful}/{len(pptx_files)}")
        print(f"Fallidos: {failed}/{len(pptx_files)}")
        print(f"Costo total estimado: ${total_cost:.4f} USD")


def main():
    """Función principal con CLI"""
    parser = argparse.ArgumentParser(
        description='Convierte presentaciones PPTX a Markdown optimizando costos de API'
    )

    parser.add_argument(
        'input',
        nargs='?',
        help='Archivo PPTX o directorio a convertir'
    )

    parser.add_argument(
        '--batch',
        action='store_true',
        help='Procesar todos los archivos PPTX en el directorio actual'
    )

    parser.add_argument(
        '--pattern',
        default='*.pptx',
        help='Patrón de archivos para modo batch (default: *.pptx)'
    )

    parser.add_argument(
        '--no-verbose',
        action='store_true',
        help='Desactivar mensajes detallados'
    )

    args = parser.parse_args()

    # Validar configuración
    try:
        Config.validate()
        Config.ensure_output_dir()
    except ValueError as e:
        print(f"❌ Error de configuración: {e}")
        print("\nCrea un archivo .env con tu ANTHROPIC_API_KEY")
        print("Ejemplo: ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)

    # Ajustar verbosidad
    if args.no_verbose:
        Config.VERBOSE = False

    # Crear conversor
    converter = PPTXToMarkdownConverter()

    try:
        if args.batch:
            # Modo batch
            directory = Path(args.input) if args.input else Path.cwd()
            converter.convert_batch(directory, args.pattern)

        elif args.input:
            # Modo single file
            converter.convert(args.input)

        else:
            # Si no hay argumentos, mostrar ayuda
            parser.print_help()
            print("\n💡 Ejemplos de uso:")
            print('  python pptx_to_markdown.py "SIM - L01a.pptx"')
            print('  python pptx_to_markdown.py --batch')
            print('  python pptx_to_markdown.py --batch --pattern "SIM*.pptx"')

    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
