import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="WIP 'wc' unix command line tool clone. ")
    parser.add_argument('-c', '--count')

    file_name = input("Enter your file name: ")
    print(get_file_size(file_name))
    pass

def get_file_size(file):
    with open(file, errors="ignore") as file:
        file.seek(0,os.SEEK_END)
        return file.tell()

if __name__ == '__main__':
    main()
