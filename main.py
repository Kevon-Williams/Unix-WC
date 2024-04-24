import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="WIP 'wc' unix command line tool clone. ")
    parser.add_argument('-c', '--check', type=str, help="Returns file size in bytes")
    args = parser.parse_args()

    file = args.check

    print(get_file_size(file))


def get_file_size(file):
    with open(file, errors="ignore") as file:
        file.seek(0,os.SEEK_END)
        return file.tell()

if __name__ == '__main__':
    main()
