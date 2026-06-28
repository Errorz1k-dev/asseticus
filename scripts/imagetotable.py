import os

# Get the directory where this script file lives (repo/scripts/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Both your images and README are inside the assets folder
IMAGE_DIR = os.path.join(SCRIPT_DIR, "..", "assets")
README_PATH = os.path.join(SCRIPT_DIR, "..", "assets", "README.md") # Fixed path
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
            # Since README.md is in the same folder as the images, 
            # the HTML path is just the image filename itself.
            img_path = images[i+j]
            table_html += f'    <td align="center"><img src="{img_path}" width="200px"/><br/><b>{images[i+j]}</b></td>\n'
        else:
            table_html += "    <td></td>\n"
    table_html += "  </tr>\n"
table_html += "</table>"

with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Using your 't' markers
START_MARKER = "<--,.-->"
END_MARKER = "<--.,-->"

if START_MARKER in content:
    # If using the exact same tag for start and end, split carefully
    parts = content.split(START_MARKER)
    if len(parts) >= 3:
        before = parts[0]
        after = parts[2]
        new_content = f"{before}{START_MARKER}\n{table_html}\n{END_MARKER}{after}"
        
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Success: assets/README.md image table updated.")
    else:
        print("Error: Make sure you have exactly two markers in your assets/README.md")
else:
    print(f"Error: Could not find markers {START_MARKER} in assets/README.md")
