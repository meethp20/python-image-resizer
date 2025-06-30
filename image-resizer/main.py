from PIL import Image
import os

def generate_extension_icons(input_path, output_dir=".", sizes=(16, 48, 128)):
    icon = Image.open("C:\Users\meeth\OneDrive\Desktop\crome-extention").convert("RGBA")
    output_paths = {}

    for size in sizes:
        resized = icon.resize((size, size), Image.LANCZOS)
        output_path = os.path.join(output_dir, f"icon{size}.png")
        resized.save(output_path, format="PNG")
        output_paths[size] = output_path

    return output_paths
