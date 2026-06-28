import os

def generate_image_table():
    assets_dir = "assets"
    readme_path = os.path.join(assets_dir, "readme.md")
    target_heading = "# **different assets for my projects**"

    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)

    valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')
    
    # Structure data by subfolder group
    # Key: Subfolder path relative to assets (or "" for root assets folder)
    # Value: List of tuples (filename, relative_path_for_src)
    structure = {}

    for root, _, files in os.walk(assets_dir):
        # Determine the subfolder name relative to assets/
        subfolder = os.path.relpath(root, assets_dir)
        if subfolder == ".":
            subfolder = ""
        else:
            subfolder = subfolder.replace(os.sep, '/')

        for file in files:
            if file.lower().endswith(valid_extensions):
                rel_path = os.path.relpath(os.path.join(root, file), assets_dir).replace(os.sep, '/')
                if subfolder not in structure:
                    structure[subfolder] = []
                structure[subfolder].append((file, rel_path))

    columns = 3
    table_lines = ["<table>"]

    # Sort groups: Root assets folder first, then subfolders alphabetically
    sorted_groups = sorted(structure.keys(), key=lambda x: (x != "", x))

    for group in sorted_groups:
        items = sorted(structure[group], key=lambda x: x[0])
        
        # Add a subfolder header row ONLY if the images belong to a subfolder
        if group:
            table_lines.append(f'  <tr>\n    <td colspan="{columns}" align="center" style="font-weight: bold;">{group}</td>\n  </tr>')

        # Chunk the images in this group into rows of 3
        for i in range(0, len(items), columns):
            row_items = items[i:i+columns]
            
            # Row 1: Image names
            name_cells = []
            for name, _ in row_items:
                name_cells.append(f'    <td align="center"><b>{name}</b></td>')
            if len(row_items) < columns:
                for _ in range(columns - len(row_items)):
                    name_cells.append('    <td></td>')
            table_lines.append("  <tr>\n" + "\n".join(name_cells) + "\n  </tr>")

            # Row 2: Images directly below names
            img_cells = []
            for _, src_path in row_items:
                img_cells.append(f'    <td align="center"><img src="./{src_path}" width="250"></td>')
            if len(row_items) < columns:
                for _ in range(columns - len(row_items)):
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
