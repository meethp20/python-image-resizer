##    Resizes an input image to standard Chrome extension icon sizes.

 ##   Args:
        input_path (str): Path to the source image (preferably 512x512 or similar).
        output_dir (str): Folder where resized icons will be saved.
        sizes (tuple): Icon sizes to generate (default: 16, 48, 128).

 ##   Returns:
        dict: Map of size to file path for each saved image.
