#!/usr/bin/env python3
def numbered_lines(filename):
    with open(filename, "r") as f:
        file_lines = f.readlines()
    line_number = 1
    with open("numbered_lines.txt", "w") as f:
        for line in file_lines:
            f.write(str(line_number)+" "+line+"\n")
            line_number+=1



def main():
    numbered_lines("small.txt")

if __name__ == "__main__":
    main()
