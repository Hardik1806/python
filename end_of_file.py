with open("text.txt", "r") as f:
    while True:
        line = f.readline()
        if line == "":              # to check for end of the file
            print("nend of file reached")
            break
        if line.strip() == "":     # stripping to remove /n in case there and printing blank line
            print("blank lne")
        else:
            print(line, end="")    