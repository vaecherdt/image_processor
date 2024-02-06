from arguments import parse_arguments
from processing import process_images


def main():
    args = parse_arguments()
    process_images(args.folder_path, args.defect)


if __name__ == "__main__":
    main()
