import os

# Moving up one level to look inside the repository root
IMAGE_DIR = "../assets"  
README_PATH = "../README.md"
COLUMNS = 3  

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
            # The HTML path in the README still needs to point to "assets/..." relative to the README location
            img_path = f"assets/{images[i+j]}"
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
    print("Success: README.md image table updated via scripts folder.")
else:
    print("Error: Could not find markers in README.md")
