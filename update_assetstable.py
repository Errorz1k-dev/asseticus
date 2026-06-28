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
    table_lines = ["| Image | Name | Image | Name | Image | Name |", "| --- | --- | --- | --- | --- | --- |"]
    
    for i in range(0, len(images), columns):
        row_images = images[i:i+columns]
        row_str = "|"
        for img in row_images:
            row_str += f" <img src='./{img}' width='100'> | `{img}` |"
        if len(row_images) < columns:
            row_str += " | |" * (columns - len(row_images))
        table_lines.append(row_str)
    
    table_content = "\n".join(table_lines)

    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = target_heading + "\n"

    if target_heading in content:
        parts = content.split(target_heading, 1)
        # Keeps everything before the heading, clears previous auto-generated tables directly under it
        new_content = f"{parts[0]}{target_heading}\n\n{table_content}\n"
    else:
        new_content = f"{content}\n\n{target_heading}\n\n{table_content}\n"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    generate_image_table()
