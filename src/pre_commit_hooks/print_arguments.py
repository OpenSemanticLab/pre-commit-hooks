import argparse


def print_arguments(arguments: list[str]):
    for argument in arguments:
        print(argument)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    print_arguments(args.filenames)
    return 0  # retval 0 means success


if __name__ == "__main__":
    main()
