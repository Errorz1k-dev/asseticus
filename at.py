import os

def generate_image_table():
    assets_dir = "assets"
    readme_path = os.path.join(assets_dir, "readme.md")
    target_heading = "# **different assets for my projects**"

    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)

    valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')
    images = []

    for root, _, files in os.walk(assets_dir):
        for file in files:
            if file.lower().endswith(valid_extensions):
                relative_path = os.path.relpath(os.path.join(root, file), assets_dir)
                relative_path = relative_path.replace(os.sep, '/')
                images.append(relative_path)
                
    images.sort()
    
    columns = 3
    table_lines = ["<table>"]
    
    for i in range(0, len(images), columns):
        row_images = images[i:i+columns]
        
        # Path string for the group (e.g., "folder/image.png" or "img1.png | img2.png")
        path_label = " | ".join(row_images)
        
        # Row 1: Spanned Header for names/paths
        table_lines.append(f'  <tr>\n    <td colspan="{columns}" align="center" style="font-weight: bold;">{path_label}</td>\n  </tr>')
        
        # Row 2: Images
        img_cells = []
        for img in row_images:
            img_cells.append(f'    <td><img src="./{img}" width="250"></td>')
            
        # Pad empty cells if columns are not filled completely
        if len(row_images) < columns:
            for _ in range(columns - len(row_images)):
                img_cells.append('    <td></td>')
                
        table_lines.append("  <tr>\n" + "\n".join(img_cells) + "\n  </tr>")
        
    table_lines.append("</table>")
    table_content = "\n".join(table_lines)

    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = target_heading + "\n"

    if target_heading in content:
        parts = content.split(target_heading, 1)
        new_content = f"{parts[0]}{target_heading}\n\n{table_content}\n"
    else:
        new_content = f"{content}\n\n{target_heading}\n\n{table_content}\n"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    generate_image_table()
