from arguments import parse_arguments
from processing import process_images
from database import save_image_data


def main():
    arguments = parse_arguments()
    folder_path = arguments.folder_path
    defect = arguments.defect

    image_data = process_images(folder_path, defect)
    save_image_data(image_data)


if __name__ == "__main__":
    main()
