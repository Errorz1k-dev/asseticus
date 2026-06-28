import os

def generate_image_table():
    assets_dir = "assets"
    readme_path = os.path.join(assets_dir, "readme.md")
    target_heading = "# **different assets for my projects**"

    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)

    valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')
    images = sorted([f for f in os.listdir(assets_dir) if f.lower().endswith(valid_extensions)])
    
    columns = 3
    table_lines = [
        "| | | |",
        "| --- | --- | --- |"
    ]
    
    for i in range(0, len(images), columns):
        row_images = images[i:i+columns]
        
        # Row 1: Names
        name_row = "|"
        for img in row_images:
            name_row += f" **{img}** |"
        if len(row_images) < columns:
            name_row += " |" * (columns - len(row_images))
            
        # Row 2: Images (Using width='250' to make them larger)
        img_row = "|"
        for img in row_images:
            img_row += f" <img src='./{img}' width='250'> |"
        if len(row_images) < columns:
            img_row += " |" * (columns - len(row_images))
            
        table_lines.append(name_row)
        table_lines.append(img_row)
    
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
