file = input()

with open(fr"D:\Downloads\{file}.txt") as f_read, open("new.fasta", 'w') as f_write:
    for line in f_read:
        f_write.write(line.replace('@', '>'))
        f_write.write(f_read.readline())
        f_read.readline()
        f_read.readline()
