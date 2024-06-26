# Markdown Callout Converter

A Python script to convert MS Docs call-out (aka admonitions or asides) syntax to MkDocs Material style callouts.

## Purpose

I write my notes natively in Obsidian but I wanted an effortless way to host some of my markdown notes in a wiki format, which led me to use MkDocs with the Material theme. However, MkDocs uses a different syntax for admonitions:

MkDocs syntax:
```markdown
!!! note
    This is a note.
```

Obsidian/MS Docs syntax:
```markdown
> [!NOTE]
> This is a note.
```

To maintain the visual aesthetic of callouts in Obsidian, I created a Python script to parse and convert all instances of callouts to the MkDocs format within the MkDocs project folder.

I keep my "live" Obsidian notebook in one location and copy/paste all the contents to the folder where my MkDocs wiki lives, and then I run the script.

## Features

- Converts Obsidian/MS Docs callout syntax (e.g., `[!NOTE]`) to MkDocs Material style (`!!! note`)
- Supports various callout types such as note, warning, info, and more

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/markdown-callout-converter.git
   cd markdown-callout-converter
   ```

2. **Place your Markdown files**:
   Ensure your Markdown files are located in the `docs` directory.

3. **Run the script**:
   ```bash
   python preprocess_markdown.py
   ```

4. **Build your MkDocs site**:
   ```bash
   mkdocs build
   ```

## Installation

- Python 3.x
- MkDocs
- MkDocs Material

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.
