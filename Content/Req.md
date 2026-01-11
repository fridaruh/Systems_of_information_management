# Sistema de Conversión de PPTX a Markdown

Sistema inteligente que convierte presentaciones PowerPoint (.pptx) a archivos Markdown (.md), optimizando costos de API al procesar visualmente solo los slides que contienen diagramas e imágenes complejas.

## Características

- **Clasificación Inteligente**: Analiza cada slide y lo clasifica como "texto" o "visual"
- **Extracción Sin Costos**: Procesa slides de texto usando parsing directo (sin API)
- **Procesamiento Visual Selectivo**: Usa Claude API solo para slides con diagramas/imágenes
- **Markdown Estructurado**: Genera documentos bien organizados con tabla de contenidos
- **Tracking de Costos**: Muestra tokens utilizados y costos estimados
- **Procesamiento por Lotes**: Convierte múltiples archivos automáticamente

## Requisitos

- Python 3.8 o superior
- API Key de Anthropic Claude
- Archivos PPTX de entrada

## Instalación

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Configurar API Key

Crea un archivo `.env` en este directorio con tu API key de Anthropic:

```bash
cp .env.example .env
```

Edita `.env` y agrega tu API key:

```
ANTHROPIC_API_KEY=sk-ant-api03-tu-key-aqui
```

Puedes obtener una API key en: https://console.anthropic.com/

## Uso

### Convertir un archivo individual

```bash
python pptx_to_markdown.py "SIM - L01a.pptx"
```

### Convertir todos los archivos PPTX en el directorio

```bash
python pptx_to_markdown.py --batch
```

### Convertir archivos con patrón específico

```bash
python pptx_to_markdown.py --batch --pattern "SIM - L0*.pptx"
```

### Opciones adicionales

```bash
# Desactivar mensajes detallados
python pptx_to_markdown.py "archivo.pptx" --no-verbose

# Ver ayuda
python pptx_to_markdown.py --help
```

## Estructura del Proyecto

```
Lectures/
├── pptx_to_markdown.py      # Script principal (CLI)
├── config.py                 # Configuración central
├── slide_classifier.py       # Clasificador de slides
├── text_extractor.py         # Extracción de texto sin API
├── visual_processor.py       # Procesamiento visual con Claude
├── markdown_generator.py     # Generador de archivos .md
├── requirements.txt          # Dependencias Python
├── .env.example              # Template de configuración
├── .gitignore               # Archivos ignorados por git
├── README.md                # Esta documentación
└── markdown/                # Directorio de salida (se crea automáticamente)
    └── *.md                 # Archivos markdown generados
```

## Cómo Funciona

### Pipeline de Procesamiento

```
1. CLASIFICACIÓN
   ├─ Analiza cada slide del PPTX
   ├─ Detecta imágenes, tablas, diagramas
   ├─ Busca keywords visuales
   └─ Clasifica como 'text' o 'visual'

2. EXTRACCIÓN DE TEXTO (sin costo)
   ├─ Procesa slides clasificados como 'text'
   ├─ Usa python-pptx para parsing directo
   └─ Preserva estructura y formato

3. PROCESAMIENTO VISUAL (con Claude API)
   ├─ Procesa solo slides clasificados como 'visual'
   ├─ Convierte slide a imagen
   ├─ Envía a Claude para análisis
   └─ Extrae: diagramas, tablas, código, relaciones

4. GENERACIÓN DE MARKDOWN
   ├─ Combina datos de texto y visuales
   ├─ Genera estructura con TOC
   ├─ Formatea en markdown
   └─ Guarda en /markdown/
```

### Criterios de Clasificación

Un slide se clasifica como **VISUAL** si:
- Contiene imágenes embebidas
- Tiene tablas o gráficos
- El texto incluye keywords como: "diagrama", "tabla", "esquema", "modelo", "ERD", etc.

Un slide se clasifica como **TEXTO** si:
- Solo contiene texto sin elementos visuales complejos
- No tiene imágenes ni diagramas
- Puede ser extraído completamente mediante parsing

### Optimización de Costos

El sistema está diseñado para minimizar el uso de la API:

- **Slides de texto**: Procesamiento local, costo = $0
- **Slides visuales**: Enviados a Claude API para análisis
- **Resultado típico**: 40-60% de slides procesados sin costo

Ejemplo de costos (presentación de 30 slides):
- 15 slides de texto → $0.00
- 15 slides visuales → ~$0.02 - $0.05 USD

## Formato de Salida

Los archivos Markdown generados incluyen:

- **Header**: Metadata del archivo (fecha, nombre original, total de slides)
- **Tabla de Contenidos**: Links a cada slide
- **Slides**: Cada uno con:
  - Número y título
  - Badge de tipo (🔤 Texto / 🎨 Visual)
  - Contenido de texto
  - Análisis visual (si aplica)
- **Footer**: Estadísticas de procesamiento y costos

## Ejemplo de Salida

```markdown
# SIM L01a

**Fecha de conversión:** 2026-01-11
**Archivo original:** `SIM - L01a.pptx`
**Total de slides:** 33

---

## Tabla de Contenidos

1. [Introducción a Sistemas de Información](#slide-1-introduccion)
2. [Bases de Datos Relacionales](#slide-2-bases-de-datos)
...

## 1. Introducción a Sistemas de Información {#slide-1-introduccion}

**Tipo:** 🔤 Texto

### Contenido

Un sistema de información es...

---

## 2. Modelo Entidad-Relación {#slide-2-erd}

**Tipo:** 🎨 Visual

### Contenido

Diagrama ERD de base de datos de empleados

### Análisis Visual

El diagrama muestra tres entidades principales:
- Empleados (id, nombre, departamento_id)
- Departamentos (id, nombre, ubicación)
- Proyectos (id, titulo, presupuesto)
...

---
```

## Troubleshooting

### Error: "ANTHROPIC_API_KEY no encontrada"

**Solución**: Verifica que creaste el archivo `.env` y agregaste tu API key

```bash
cp .env.example .env
# Edita .env y agrega tu API key real
```

### Error: "Archivo no encontrado"

**Solución**: Asegúrate de que el archivo PPTX existe y la ruta es correcta

```bash
# Usa ruta absoluta o relativa correcta
python pptx_to_markdown.py "./SIM - L01a.pptx"
```

### Warning: "No se pudieron extraer imágenes"

**Nota**: La extracción de imágenes tiene limitaciones. El sistema puede no renderizar todos los elementos visuales perfectamente, pero enviará el contexto textual a Claude para análisis.

### Costos muy altos

**Solución**:
- Verifica que la clasificación está funcionando (revisa la salida)
- Ajusta `VISUAL_KEYWORDS` en `config.py` para ser más restrictivo
- Usa `--no-verbose` para reducir output innecesario

## Limitaciones Conocidas

1. **Renderizado de Slides**: La conversión de slides a imágenes es simplificada. Para resultados óptimos, considera exportar manualmente algunos slides complejos como imágenes.

2. **Animaciones**: No se preservan animaciones o transiciones.

3. **Notas del Presentador**: Actualmente no se incluyen en el output (funcionalidad planificada).

4. **Fórmulas Matemáticas**: Fórmulas complejas pueden no convertirse correctamente a markdown.

## Roadmap

- [ ] Soporte para exportación de slides a imágenes usando LibreOffice
- [ ] Inclusión de notas del presentador
- [ ] Soporte para fórmulas LaTeX
- [ ] Caché de resultados para evitar reprocesamiento
- [ ] Interfaz web opcional
- [ ] Soporte para archivos PDF

## Soporte

Para reportar bugs o solicitar features, abre un issue en el repositorio del proyecto.

## Licencia

Este proyecto es de uso educativo para el curso Systems of Information Management.

---

Desarrollado con Claude Code
