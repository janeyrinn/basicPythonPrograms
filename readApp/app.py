"""read_file = open("read.txt", "r")

for word in read_file.readlines():
    print(word)

read_file.close()"""

read_file = open("read.txt", "a") 

read_file.write("\nNew Appendage")

read_file.close()