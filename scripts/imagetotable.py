import os

# Get the directory where this script file actually lives (repo/scripts/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up one level to the repository root, then into the folders
IMAGE_DIR = os.path.join(SCRIPT_DIR, "..", "assets")
README_PATH = os.path.join(SCRIPT_DIR, "..", "README.md")
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
            # The HTML path written to the README still needs to be relative to the README
            img_path = f"assets/{images[i+j]}"
            table_html += f'    <td align="center"><img src="{img_path}" width="200px"/><br/><b>{images[i+j]}</b></td>\n'
        else:
            table_html += "    <td></td>\n"
    table_html += "  </tr>\n"
table_html += "</table>"

with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

START_MARKER = "..,."
END_MARKER = ".,.."

if START_MARKER in content and END_MARKER in content:
    before = content.split(START_MARKER)[0]
    after = content.split(END_MARKER)[1]
    new_content = f"{before}{START_MARKER}\n{table_html}\n{END_MARKER}{after}"
    
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Success: README.md image table updated dynamically.")
else:
    print(f"Error: Could not find markers {START_MARKER} and {END_MARKER} in README.md")
