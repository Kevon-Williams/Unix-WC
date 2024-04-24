import os
import argparse

def main():
    #initialize/create the arg parser 
    parser = argparse.ArgumentParser(description="WIP 'wc' unix command line tool clone. ") 

    #command line argument with short and long form
    parser.add_argument('-c', '--check', type=str, help="Returns file size in bytes") 

    #parse command line arguments
    args = parser.parse_args() 

    #store entered input
    file = args.check 

    print(f"{get_file_size(file)} bytes")  


def get_file_size(file):
    with open(file, errors="ignore") as file:
        file.seek(0,os.SEEK_END)
        return file.tell()

if __name__ == '__main__':
    main()
