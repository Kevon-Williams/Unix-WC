import os
import argparse

def main():
    #initialize/create the arg parser 
    parser = argparse.ArgumentParser(description="WIP 'wc' unix command line tool clone. ") 

    #command line argument with short and long form
    parser.add_argument('-c', '--check', type=str, help="Returns file size in bytes") 
    parser.add_argument('-l', '--lines', type=str, help="Returns file size in bytes") 

    #parse command line arguments
    args = parser.parse_args() 

    #store entered input
    file = args.check 
    file_lines = args.lines

    if file != None:
        print(f"{get_file_size(file)} bytes") 
    elif file_lines != None:
        print(f"{get_file_lines(file_lines)} lines") 

    


def get_file_size(file):
    with open(file, errors="ignore") as file:
        file.seek(0,os.SEEK_END)
        return file.tell()

def get_file_lines(file):
    line = 0
    with open(file ,errors="ignore") as file:
        for i in file:
            line+=1
    return line


if __name__ == '__main__':
    main()
