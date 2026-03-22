# Image Processing Pipeline

This Python script provides a simple pipeline for **image compression, resizing, and format conversion**. It is built using [Pillow](https://pillow.readthedocs.io/en/stable/) and works with common image formats like JPEG, PNG, and WebP.

---

## Features

1. **Compress Images**
   - Reduce file size by lowering image quality.
   - Supported formats: `.jpg`, `.jpeg`, `.png`, `.webp`.
   - Function: `compress_images(input_folder, output_folder, quantity)`

2. **Resize Images**
   - Resize images to a specific width and height.
   - Automatically renames output files to include dimensions (e.g., `image_200x210.jpg`).
   - Function: `resize_images(input_folder, output_folder, width, height)`

3. **Convert Image Format**
   - Convert images to JPEG, PNG, or WebP.
   - Handles transparency for formats that support it.
   - Function: `convert_images(input_folder, output_folder, fmt)`

4. **Prevent Overwriting**
   - Automatically appends `_1`, `_2`, etc., if the output filename already exists.
   - Function: `get_unique_path(path)`

---

## Installation

1. Install Python 3.7+  
2. Install dependencies:

```bash
pip install pillow