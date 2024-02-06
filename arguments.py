import argparse


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Process the images in a folder, upload them to Google Drive and"
                                                 "store the image information in the database.")
    parser.add_argument("folder_path", help="Path to the folder containing the images.")
    parser.add_argument("-d", "--defect", help="Specify the defect of the grains in the images.")

    return parser.parse_args()
