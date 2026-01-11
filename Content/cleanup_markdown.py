#!/usr/bin/env python3
"""
Limpieza de archivos Markdown - Elimina contenido duplicado y antiguo
"""
import re
from pathlib import Path


def cleanup_visual_analysis(content: str) -> str:
    """
    Elimina secciones antiguas de análisis visual que quedaron duplicadas

    Las secciones antiguas comienzan con "## 1. DESCRIPCIÓN VISUAL" y contienen
    descripciones de diseño que no queremos.
    """
    # Patrón para encontrar y eliminar secciones antiguas dentro de Visual Analysis
    # Busca desde "## 1. DESCRIPCIÓN VISUAL" hasta el próximo "---" o final de sección
    pattern = r'(### Visual Analysis\s+.*?)(## 1\. DESCRIPCIÓN VISUAL.*?)(?=\n---|\Z)'

    def replace_func(match):
        # Solo mantener la primera parte (el nuevo análisis)
        return match.group(1).rstrip() + '\n\n'

    content = re.sub(pattern, replace_func, content, flags=re.DOTALL)

    # Limpiar cualquier sección que empiece con "## 2. CONTENIDO:"
    pattern2 = r'## 2\. CONTENIDO:.*?(?=\n---|\n## \d+\.|\Z)'
    content = re.sub(pattern2, '', content, flags=re.DOTALL)

    # Limpiar secciones que empiecen con "## 3." "## 4." etc
    pattern3 = r'## [3-9]\. [A-Z].*?(?=\n---|\n## \d+\.|\Z)'
    content = re.sub(pattern3, '', content, flags=re.DOTALL)

    return content


def cleanup_file(md_path: Path) -> bool:
    """Limpia un archivo markdown individual"""
    print(f"Limpiando: {md_path.name}...", end='')

    try:
        # Leer contenido
        content = md_path.read_text(encoding='utf-8')

        # Aplicar limpieza
        cleaned_content = cleanup_visual_analysis(content)

        # Solo guardar si hubo cambios
        if content != cleaned_content:
            md_path.write_text(cleaned_content, encoding='utf-8')
            print(" ✓ Limpiado")
            return True
        else:
            print(" (sin cambios)")
            return False
    except Exception as e:
        print(f" ✗ Error: {e}")
        return False


def main():
    """Función principal"""
    md_dir = Path(__file__).parent / 'markdown'
    md_files = sorted(md_dir.glob('*.md'))

    print(f"\n🧹 Limpiando {len(md_files)} archivos markdown\n")

    cleaned_count = 0
    for md_file in md_files:
        if cleanup_file(md_file):
            cleaned_count += 1

    print(f"\n✓ Proceso completado: {cleaned_count} archivos modificados")


if __name__ == '__main__':
    main()
