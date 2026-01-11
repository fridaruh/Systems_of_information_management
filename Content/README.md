# Systems of Information Management (SIM) - Portfolio

This repository contains a comprehensive collection of academic projects, practical exercises, and specialized tools developed for the **Systems of Information Management** course. The project covers a wide range of topics, from database modeling and normalization to web development and AI-powered document processing.

## 🚀 Key Project: PPTX to Markdown Converter

Located in the `Lectures/` directory, this is an intelligent system designed to convert PowerPoint presentations (`.pptx`) into structured Markdown (`.md`) files.

### Features
- **Intelligent Classification**: Automatically distinguishes between text-heavy slides and visual slides (diagrams, images).
- **Cost Optimization**: Uses direct parsing for text slides and only invokes the **Anthropic Claude API** for complex visual analysis.
- **Structured Output**: Generates a clean Markdown file with a Table of Contents, visual analysis of diagrams, and processing statistics.
- **Batch Processing**: Supports converting entire directories of presentations at once.

### Quick Start (Lectures Tool)
1. Install dependencies: `pip install -r requirements.txt`
2. Configure your `.env` file with an `ANTHROPIC_API_KEY`.
3. Run: `python pptx_to_markdown.py your_presentation.pptx`

---

## 📊 Database Design & Modeling

Focused on relational database theory and practical application. This section includes comprehensive documentation on:

- **Mia's Sandwich Shop**: A complete EER (Extended Entity-Relationship) model and relational mapping.
- **Normalization Strategy**: Detailed justification for **1NF, 2NF, and 3NF** compliance to ensure data integrity and eliminate redundancies.
- **Business Logic**: Analysis of participation constraints, functional dependencies, and referential integrity.
- **Documentation**: See `mias_sandwich_shop_db_design.md` and `Store.md`.

---

## 🌐 Web Development & Programming

A series of practical implementations demonstrating core web concepts:

### Dynamic Web with PHP (`mia/` directory)
- **Component Reusability**: Conversion of a static site into a dynamic one using PHP `require` for headers and footers.
- **Consistency**: Implementation of a "Don't Repeat Yourself" (DRY) architecture for easier maintenance.

### JavaScript & Logic Exercises
- **Algorithms**: Implementations of Fibonacci sequences, Factorial functions, and Array manipulation.
- **UI Components**: Interactive examples including:
  - **Vending Machine Simulator**: State management and user interaction.
  - **Scientific Calculator**: Logic and event handling.
  - **Error Handling**: Demonstrations of common JavaScript error types and debugging.

---

## 📂 Project Structure

```text
.
├── Lectures/                # PPTX to Markdown conversion system
│   ├── pptx_to_markdown.py  # Main entry point
│   ├── visual_processor.py  # AI-powered visual analysis
│   └── ...
├── mia/                     # Mia's Sandwich Shop dynamic PHP site
├── week8-Examples.../       # Advanced lecture examples
├── Excercise*.html          # Practical JS/HTML labs
├── Store.md                 # Database design for a store
├── mias_sandwich_shop_db... # Database design documentation
└── VendingMachine.html      # Interactive logic exercise
```

---

## 🛠️ Technologies Used

- **Programming**: Python (3.8+), PHP, JavaScript.
- **AI/ML**: Anthropic Claude API (Vision/Text analysis).
- **Web**: HTML5, CSS3.
- **Modeling**: Meridan/EER, SQL Server/PostgreSQL principles.
- **Scripting**: Shell/Bash for automation.

---

## 🎓 Academic Context

This repository serves as a portfolio for the Systems of Information Management course. It demonstrates proficiency in systematic information processing, database theory, and modern software development workflows.

*Developed with the assistance of Claude Code.*
