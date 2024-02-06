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
            # Implement the remaining steps
        else:
            print(f"Image {file_path} is a duplicate. Skipping...")
    if defect is None:
        print("Defect not specified")
    else:
        print(defect)


def extract_metadata(file_path):
    try:
        image = Image.open(file_path)
        timestamp = image.getexif().get(36867, "Unknown")
        metadata = {
            "timestamp": timestamp
        }
        return metadata
    except Exception as e:
        print(f"Error extracting metadata from {file_path}: {e}")
        return {"timestamp": "Unknown"}
