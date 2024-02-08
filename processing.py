import os
from PIL import Image
from database import check_duplicate_image


def process_images(folder_path, defect):
    print("Processing images...")
    image_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".jpg")]

    for file_path in image_files:
        print(f"Processing image: {file_path}")
        if not check_duplicate_image(file_path):
            print(f"Image {file_path} is not a duplicate.")
            metadata = extract_metadata(file_path)
            print("Metadata:", metadata)
        else:
            print(f"Image {file_path} is a duplicate. Skipping...")
    if defect is None:
        print("Defect not specified")
    else:
        print(defect)


def extract_metadata(file_path):
    try:
        image = Image.open(file_path)
        exif_data = image.getexif()
        print(f"EXIF data for {file_path}: {exif_data}")
    except IOError:
        print(f"Cannot open image at {file_path}.")
        return {"timestamp": "Unknown"}
    try:
        timestamp = image.getexif().get(306, "Unknown")
    except KeyError:
        print(f"EXIF data does not contain timestamp for {file_path}.")
        return {"timestamp": "Unknown"}

    metadata = {
        "timestamp": timestamp
    }
    return metadata
