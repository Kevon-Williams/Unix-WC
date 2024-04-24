import os
import argparse

def main():
    #initialize/create the arg parser 
    parser = argparse.ArgumentParser(description="WIP 'wc' unix command line tool clone. ") 

    #command line argument with short and long form
    parser.add_argument('-c', '--characters', type=str, help="Returns file size in bytes") 
    parser.add_argument('-l', '--lines', type=str, help="Returns the number of lines in a file") 
    parser.add_argument('-w', '--words', type=str, help="Returns the number of words in a file") 

    #parse command line arguments
    args = parser.parse_args() 

    #store entered input
    file = args.characters
    file_lines = args.lines
    file_words = args.words

    if file != None:
        print(f"{get_file_size(file)} bytes") 
    elif file_lines != None:
        print(f"{get_file_lines(file_lines)} lines")
    elif  file_words != None:
        print(f"{get_file_words(file_words)} words")

    


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

def get_file_words(file):
    number_of_words = 0
    with open(file, errors="ignore") as file:
        data = file.read()
        lines = data.split()
        number_of_words += len(lines)
    
    return number_of_words


if __name__ == '__main__':
    main()
