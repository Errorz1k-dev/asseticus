import os

IMAGE_DIR = "assets"  # Folder containing your images
README_PATH = "assets/readme.md"
COLUMNS = 3  # Adjust how many columns you want in your table

extensions = (".png", ".jpg", ".jpeg", ".gif", ".webp")

if not os.path.exists(IMAGE_DIR):
    print(f"Directory '{IMAGE_DIR}' not found. Creating it...")
    os.makedirs(IMAGE_DIR)

images = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(extensions)]
images.sort()

table_html = "<table>\n"
for i in range(0, len(images), COLUMNS):
    table_html += "  <tr>\n"
    for j in range(COLUMNS):
        if i + j < len(images):
            img_path = f"{IMAGE_DIR}/{images[i+j]}"
            table_html += f'    <td align="center"><img src="{img_path}" width="200px"/><br/><b>{images[i+j]}</b></td>\n'
        else:
            table_html += "    <td></td>\n"
    table_html += "  </tr>\n"
table_html += "</table>"

with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

START_MARKER = ""
END_MARKER = ""

if START_MARKER in content and END_MARKER in content:
    before = content.split(START_MARKER)[0]
    after = content.split(END_MARKER)[1]
    new_content = f"{before}{START_MARKER}\n{table_html}\n{END_MARKER}{after}"
    
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Success: README.md image table updated locally.")
else:
    print("Error: Could not find markers in README.md")
