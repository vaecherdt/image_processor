import os
import json
from PIL import Image


def process_images(folder_path, defect):
    image_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".jpg")]
    file_renaming_counter = 1
    image_data = []

    for image in image_files:
        print(f"image: {image}")
        timestamp = get_timestamp(image)
        exif = get_exif(image)
        file_renaming_counter = rename_files(image, defect, file_renaming_counter, folder_path)

        image_data.append({
            "file_name": f"{defect}_{file_renaming_counter}.jpg",
            "timestamp": timestamp,
            "exif": exif,
            "defect": defect
        })
    print(image_data)
    return image_data


def get_exif(file_path):
    try:
        image = Image.open(file_path)
        exif_data = {k: v for k, v in image.getexif().items() if isinstance(v, (bytes, str))}
    except IOError:
        print(f"Cannot open image at {file_path}.")
        return json.dumps({"Unknown"})
    return json.dumps(exif_data)


def get_timestamp(file_path):
    try:
        image = Image.open(file_path)
    except IOError:
        print(f"Cannot open image at {file_path}.")
        return {"Unknown"}
    try:
        timestamp = image.getexif().get(306, "Unknown")
    except KeyError:
        print(f"EXIF data does not contain timestamp for {file_path}.")
        return {"Unknown"}

    return timestamp


def rename_files(original_path, defect, counter, folder_path):
    new_file_name = f"{defect}_{counter}.jpg"
    new_file_path = os.path.join(folder_path, new_file_name)
    os.rename(original_path, new_file_path)
    return counter + 1
