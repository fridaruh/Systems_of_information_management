"""
Generador de archivos Markdown a partir de datos extraídos
"""
from pathlib import Path
from typing import Dict, List
from datetime import datetime
from config import Config


class MarkdownGenerator:
    """Genera archivos markdown estructurados a partir de datos de slides"""

    def __init__(self, config: Config = None):
        self.config = config or Config()

    def generate_markdown(
        self,
        pptx_filename: str,
        text_slides: Dict[int, Dict[str, str]],
        visual_slides: Dict[int, Dict[str, str]],
        classifications: Dict[int, str],
        stats: Dict[str, any]
    ) -> str:
        """
        Genera un archivo markdown completo

        Args:
            pptx_filename: Nombre del archivo PPTX original
            text_slides: Datos de slides de texto
            visual_slides: Datos de slides visuales
            classifications: Clasificación de cada slide
            stats: Estadísticas del procesamiento

        Returns:
            Ruta del archivo markdown generado
        """
        # Preparar nombre de archivo de salida
        output_filename = self._sanitize_filename(pptx_filename)
        output_path = self.config.OUTPUT_DIR / f"{output_filename}.md"

        # Combinar todos los slides
        all_slides = {**text_slides, **visual_slides}

        # Generar contenido markdown
        content = self._build_markdown_content(
            pptx_filename,
            all_slides,
            classifications,
            stats
        )

        # Escribir archivo
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        if self.config.VERBOSE:
            print(f"\n✓ Markdown generado: {output_path}")

        return str(output_path)

    def _build_markdown_content(
        self,
        pptx_filename: str,
        all_slides: Dict[int, Dict[str, str]],
        classifications: Dict[int, str],
        stats: Dict[str, any]
    ) -> str:
        """Construye el contenido markdown completo"""
        lines = []

        # Header
        lines.append(self._generate_header(pptx_filename, stats))
        lines.append("")

        # Table of contents
        lines.append(self._generate_toc(all_slides))
        lines.append("")

        # Slides content
        slide_numbers = sorted(all_slides.keys())
        for slide_num in slide_numbers:
            slide_data = all_slides[slide_num]
            classification = classifications.get(slide_num, 'unknown')

            lines.append(self._generate_slide_section(
                slide_num,
                slide_data,
                classification
            ))
            lines.append("")

        # Footer with metadata
        lines.append(self._generate_footer(stats))

        return "\n".join(lines)

    def _generate_header(self, pptx_filename: str, stats: Dict) -> str:
        """Genera el encabezado del documento"""
        title = self._extract_title_from_filename(pptx_filename)
        date = datetime.now().strftime("%Y-%m-%d")

        header = f"""# {title}

**Fecha de conversión:** {date}
**Archivo original:** `{pptx_filename}`
**Total de slides:** {stats.get('total_slides', 0)}

---
"""
        return header

    def _generate_toc(self, all_slides: Dict[int, Dict[str, str]]) -> str:
        """Genera tabla de contenidos"""
        lines = ["## Tabla de Contenidos\n"]

        slide_numbers = sorted(all_slides.keys())
        for slide_num in slide_numbers:
            title = all_slides[slide_num].get('title', f'Slide {slide_num}')
            anchor = self._create_anchor(title, slide_num)
            lines.append(f"{slide_num}. [{title}](#{anchor})")

        return "\n".join(lines)

    def _generate_slide_section(
        self,
        slide_num: int,
        slide_data: Dict[str, str],
        classification: str
    ) -> str:
        """Genera la sección de un slide individual"""
        title = slide_data.get('title', f'Slide {slide_num}')
        content = slide_data.get('content', '')
        visual_description = slide_data.get('visual_description', '')

        lines = []

        # Título del slide
        anchor = self._create_anchor(title, slide_num)
        lines.append(f"## {slide_num}. {title} {{#{anchor}}}")
        lines.append("")

        # Badge de tipo
        badge = "🔤 Texto" if classification == 'text' else "🎨 Visual"
        lines.append(f"**Tipo:** {badge}")
        lines.append("")

        # Contenido de texto
        if content:
            lines.append("### Contenido")
            lines.append("")
            lines.append(content)
            lines.append("")

        # Descripción visual (solo para slides visuales)
        if visual_description:
            lines.append("### Análisis Visual")
            lines.append("")
            lines.append(visual_description)
            lines.append("")

        lines.append("---")

        return "\n".join(lines)

    def _generate_footer(self, stats: Dict) -> str:
        """Genera el pie de página con metadatos"""
        lines = ["\n---\n", "## Metadatos de Procesamiento\n"]

        # Estadísticas de clasificación
        lines.append("### Clasificación de Slides")
        lines.append(f"- Slides de texto: {stats.get('text_slides', 0)}")
        lines.append(f"- Slides visuales: {stats.get('visual_slides', 0)}")
        lines.append(
            f"- Porcentaje optimizado (sin API): "
            f"{stats.get('text_percentage', 0):.1f}%"
        )
        lines.append("")

        # Costos de API si están disponibles
        if 'api_cost' in stats:
            cost_data = stats['api_cost']
            lines.append("### Costos de API")
            lines.append(f"- Tokens de entrada: {cost_data.get('input_tokens', 0):,}")
            lines.append(f"- Tokens de salida: {cost_data.get('output_tokens', 0):,}")
            lines.append(
                f"- Costo total: ${cost_data.get('total_cost_usd', 0):.4f} USD"
            )
            lines.append("")

        # Información de generación
        lines.append("### Sistema")
        lines.append(f"- Generado por: PPTX to Markdown Converter")
        lines.append(f"- Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        return "\n".join(lines)

    def _sanitize_filename(self, filename: str) -> str:
        """Sanitiza el nombre del archivo para uso como nombre de archivo markdown"""
        # Remover extensión
        name = Path(filename).stem

        # Reemplazar caracteres especiales
        name = name.replace(' ', '-')
        name = name.replace('(', '')
        name = name.replace(')', '')

        return name

    def _extract_title_from_filename(self, filename: str) -> str:
        """Extrae un título legible del nombre del archivo"""
        name = Path(filename).stem
        # Ejemplo: "SIM - L01a" -> "SIM L01a"
        return name.replace('-', ' ').strip()

    def _create_anchor(self, title: str, slide_num: int) -> str:
        """Crea un anchor link para el TOC"""
        # GitHub-flavored markdown anchor
        anchor = title.lower()
        anchor = anchor.replace(' ', '-')
        anchor = ''.join(c for c in anchor if c.isalnum() or c == '-')
        return f"slide-{slide_num}-{anchor}"
