#!/usr/bin/env python3
"""
Optimizador de archivos Markdown para base de conocimiento

Reescribe secciones de análisis visual para enfocarse solo en conceptos,
elimina información de diseño, y asegura que todo esté en inglés.
"""
import re
import sys
from pathlib import Path
from anthropic import Anthropic
from config import Config


class MarkdownOptimizer:
    """Optimiza archivos markdown para uso como base de conocimiento"""

    def __init__(self):
        self.config = Config()
        self.client = Anthropic(api_key=self.config.ANTHROPIC_API_KEY)
        self.total_cost = 0.0

    def optimize_file(self, md_path: Path) -> bool:
        """
        Optimiza un archivo markdown individual

        Args:
            md_path: Ruta al archivo markdown

        Returns:
            True si se procesó exitosamente
        """
        print(f"\n{'='*60}")
        print(f"Procesando: {md_path.name}")
        print(f"{'='*60}")

        # Leer contenido
        content = md_path.read_text(encoding='utf-8')

        # Encontrar todas las secciones con análisis visual
        visual_sections = self._find_visual_sections(content)

        if not visual_sections:
            print("  ✓ No hay secciones visuales para procesar")
            # Solo quitar "**Tipo:**" y traducir si es necesario
            content = self._remove_type_labels(content)
            content = self._ensure_english(content)
            md_path.write_text(content, encoding='utf-8')
            return True

        print(f"  Encontradas {len(visual_sections)} secciones visuales")

        # Procesar cada sección visual
        for i, (slide_num, old_analysis) in enumerate(visual_sections, 1):
            print(f"  [{i}/{len(visual_sections)}] Reescribiendo slide {slide_num}...", end='')

            try:
                new_analysis = self._rewrite_visual_analysis(old_analysis, slide_num)
                content = content.replace(old_analysis, new_analysis)
                print(" ✓")
            except Exception as e:
                print(f" ✗ Error: {e}")
                continue

        # Quitar etiquetas de "**Tipo:**"
        content = self._remove_type_labels(content)

        # Asegurar que todo esté en inglés
        content = self._ensure_english(content)

        # Guardar archivo actualizado
        md_path.write_text(content, encoding='utf-8')

        print(f"  ✓ Archivo optimizado exitosamente")
        return True

    def _find_visual_sections(self, content: str) -> list:
        """
        Encuentra todas las secciones con análisis visual

        Returns:
            Lista de tuplas (slide_number, analysis_text)
        """
        visual_sections = []

        # Patrón para encontrar secciones visuales
        pattern = r'## (\d+)\..*?\*\*Tipo:\*\* 🎨 Visual.*?### Análisis Visual\s+(.*?)(?=\n---|\n## \d+\.|\Z)'

        matches = re.finditer(pattern, content, re.DOTALL)

        for match in matches:
            slide_num = match.group(1)
            analysis = match.group(2).strip()
            visual_sections.append((slide_num, analysis))

        return visual_sections

    def _rewrite_visual_analysis(self, old_analysis: str, slide_num: str) -> str:
        """
        Reescribe el análisis visual enfocándose solo en conceptos

        Args:
            old_analysis: Texto original del análisis
            slide_num: Número del slide

        Returns:
            Nuevo análisis enfocado en conceptos
        """
        prompt = f"""You are analyzing educational slide content for a knowledge base.

Original analysis:
{old_analysis}

TASK: Rewrite this content focusing ONLY on the educational concepts, information, and knowledge being presented.

REMOVE:
- Descriptions of visual design (colors, fonts, backgrounds, layout)
- Comments about slide aesthetics or presentation style
- Phrases like "the slide shows", "the diagram displays", "visually"
- Any metadata about how information is presented

KEEP and ENHANCE:
- Core concepts and definitions
- Technical information and explanations
- Relationships between concepts
- Examples and code snippets
- Tables and structured data (convert to markdown tables)
- Diagrams content (describe what relationships/concepts they show, not how they look)

REQUIREMENTS:
- Write in clear, concise English
- Use markdown formatting (headers, lists, code blocks, tables)
- Focus on knowledge that would be useful for understanding the topic
- Be direct and informative
- If it's a table, reproduce it in markdown format
- If it's a diagram, explain the concepts and relationships it illustrates

Output the rewritten content directly, without any preamble or explanation."""

        response = self.client.messages.create(
            model=self.config.ANTHROPIC_MODEL,
            max_tokens=2000,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        # Track costs
        input_tokens = response.usage.input_tokens
        output_tokens = response.usage.output_tokens
        cost = (input_tokens * self.config.COST_PER_INPUT_TOKEN +
                output_tokens * self.config.COST_PER_OUTPUT_TOKEN)
        self.total_cost += cost

        return response.content[0].text.strip()

    def _remove_type_labels(self, content: str) -> str:
        """Elimina las líneas que dicen **Tipo:** 🔤 Texto o **Tipo:** 🎨 Visual"""
        # Patrón para encontrar líneas con **Tipo:**
        pattern = r'\*\*Tipo:\*\* [🔤🎨].*?\n\n'
        content = re.sub(pattern, '', content)
        return content

    def _ensure_english(self, content: str) -> str:
        """
        Asegura que las secciones clave estén en inglés
        (Solo traduce headers y metadata, no todo el contenido)
        """
        # Traducir headers comunes
        translations = {
            'Tabla de Contenidos': 'Table of Contents',
            'Contenido': 'Content',
            'Análisis Visual': 'Visual Analysis',
            'Metadatos de Procesamiento': 'Processing Metadata',
            'Clasificación de Slides': 'Slide Classification',
            'Costos de API': 'API Costs',
            'Sistema': 'System',
            'Slides de texto': 'Text slides',
            'Slides visuales': 'Visual slides',
            'Porcentaje optimizado (sin API)': 'Optimized percentage (without API)',
            'Tokens de entrada': 'Input tokens',
            'Tokens de salida': 'Output tokens',
            'Costo total': 'Total cost',
            'Generado por': 'Generated by',
            'Fecha de conversión': 'Conversion date',
            'Archivo original': 'Original file',
            'Total de slides': 'Total slides',
            'Fecha': 'Date'
        }

        for spanish, english in translations.items():
            content = content.replace(spanish, english)

        return content

    def get_cost_summary(self) -> dict:
        """Retorna resumen de costos"""
        return {
            'total_cost_usd': self.total_cost
        }


def main():
    """Función principal"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Optimiza archivos markdown para base de conocimiento'
    )
    parser.add_argument(
        'input',
        nargs='?',
        help='Archivo markdown o directorio a optimizar'
    )
    parser.add_argument(
        '--batch',
        action='store_true',
        help='Procesar todos los archivos markdown en el directorio'
    )

    args = parser.parse_args()

    optimizer = MarkdownOptimizer()

    if args.batch:
        # Procesar todos los archivos en el directorio markdown
        md_dir = Path(__file__).parent / 'markdown'
        md_files = sorted(md_dir.glob('*.md'))

        print(f"\n🎯 Optimizando {len(md_files)} archivos markdown\n")

        success_count = 0
        for md_file in md_files:
            try:
                if optimizer.optimize_file(md_file):
                    success_count += 1
            except Exception as e:
                print(f"  ✗ Error procesando {md_file.name}: {e}")

        # Resumen final
        cost_info = optimizer.get_cost_summary()
        print(f"\n{'='*60}")
        print(f"RESUMEN")
        print(f"{'='*60}")
        print(f"Archivos procesados: {success_count}/{len(md_files)}")
        print(f"Costo total de optimización: ${cost_info['total_cost_usd']:.4f} USD")

    elif args.input:
        # Procesar un solo archivo
        md_path = Path(args.input)
        if not md_path.exists():
            print(f"Error: Archivo no encontrado: {md_path}")
            sys.exit(1)

        optimizer.optimize_file(md_path)
        cost_info = optimizer.get_cost_summary()
        print(f"\nCosto de optimización: ${cost_info['total_cost_usd']:.4f} USD")

    else:
        parser.print_help()
        print("\n💡 Ejemplo de uso:")
        print("  python3 optimize_markdown.py --batch")
        print("  python3 optimize_markdown.py markdown/SIM---L01a.md")


if __name__ == '__main__':
    main()
