import os
from subprocess import call

data = input("data: ")
width = input("width: ")
output = input("otput: ")
CMD = f"meme {data} -text -nostatus -protein -minw {width} > {output}"

if __name__ == '__main__':
    c = call(CMD, shell=True)

    with open(output) as outfile:
        for line in outfile:
            if 'regular expression' in line:
                separator = outfile.readline()
                regex = outfile.readline().rstrip()
                break

    os.remove('outfile')
    print(regex)