import os
from PIL import Image

SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".webp")

def compress_image(input_path, output_path, quantity):
    try:
        with Image.open(input_path) as img:
            if img.mode in ("RGB", "P"):
                img = img.convert("RGB")

            img.save(output_path, optimize=True, quality=quantity)

    except Exception as e:
        print(f"Failed to compress image: {e}")

def compress_images(input_folder, output_folder, quantity):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):

        if filename.lower().endswith(SUPPORTED_FORMATS):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            compress_image(input_path, output_path, quantity)

    print("Done compressing images!")

def resize_image(input_path, output_path, width, height):
    try:
        with Image.open(input_path) as img:
            resized = img.resize((width, height))

            if resized.mode in ("RGB", "P"):
                resized = resized.convert("RGB")

            resized.save(output_path, optimize=True, quality=100)
            print(f"✔ Resized: {os.path.basename(input_path)}")

    except Exception as e:
        print(f"Failed to resize image: {e}")


def resize_images(input_folder, output_folder, width=400, height=350):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if not filename.lower().endswith(SUPPORTED_FORMATS):
            continue

        input_path = os.path.join(input_folder, filename)
        name, ext = os.path.splitext(filename)
        new_filename = f"{name}_{width}x{height}{ext}"
        output_path = os.path.join(output_folder, new_filename)

        resize_image(input_path, output_path, width, height)

def convert_image(input_path, output_path, fmt="JPEG"):
    try:
        with Image.open(input_path) as img:
            if fmt.upper() in ("JPEG", "JPG") and img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            if fmt.upper() in ("PNG"):
                img.save(output_path, format=fmt, optimize=True)
            else:
                img.save(output_path, format=fmt, optimize=True, quality=100)

    except Exception as e:
        print(f"Failed to convert image: {e}")

def get_unique_path(path):
    if not os.path.exists(path):
        return path

    base, ext = os.path.splitext(path)
    counter = 1

    while True:
        new_path = f"{base}_{counter}{ext}"
        if not os.path.exists(new_path):
            return new_path
        counter += 1

def convert_images(input_folder, output_folder, fmt="JPEG"):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if not filename.lower().endswith(SUPPORTED_FORMATS):
            continue

        input_path = os.path.join(input_folder, filename)
        name, _ = os.path.splitext(filename)
        ext = "." + fmt.lower()
        new_filename = f"{name}{ext}"

        output_path = os.path.join(output_folder, new_filename)
        output_path = get_unique_path(output_path)

        convert_image(input_path, output_path, fmt)

def main():
    input_folder = "./../data/images"
    output_folder = os.path.join(input_folder, "compressed")
    thumb_output_folder = os.path.join(input_folder, "thumbnails")
    thumb_output_convert = os.path.join(input_folder, "converted")

    quantity = 60

    compress_images(input_folder, output_folder, quantity)
    resize_images(input_folder, thumb_output_folder, 200, 210)
    convert_images(input_folder, thumb_output_convert, "PNG")

if __name__ == "__main__":
    main()