import os
import re

# Define the directory containing your Markdown files
docs_dir = "docs"

# Define the mapping from MS Docs style to MkDocs Material style
callout_mapping = {
    "NOTE": "note",
    "ABSTRACT": "abstract",
    "INFO": "info",
    "TIP": "tip",
    "SUCCESS": "success",
    "QUESTION": "question",
    "WARNING": "warning",
    "FAILURE": "failure",
    "DANGER": "danger",
    "BUG": "bug",
    "EXAMPLE": "example",
    "QUOTE": "quote",
}

# Regular expression to match MS Docs callouts
msdocs_callout_re = re.compile(r'> \[!(\w+)\]([^\n]*)(.*?)\n\n', re.DOTALL)

def convert_callouts(content):
    def replace_callout(match):
        callout_type = match.group(1)
        title = match.group(2).strip()
        body = match.group(3).strip()
        mkdocs_callout_type = callout_mapping.get(callout_type, "note")
        if title:
            return f'!!! {mkdocs_callout_type} "{title}"\n    {body.replace("\n", "\n    ")}\n\n'
        else:
            return f'!!! {mkdocs_callout_type}\n    {body.replace("\n", "\n    ")}\n\n'
    return msdocs_callout_re.sub(replace_callout, content)

# Process all Markdown files in the docs directory
for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            new_content = convert_callouts(content)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)

print("Preprocessing complete.")