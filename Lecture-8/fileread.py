def main():
    infile = open("philisophers.txt","r")
    file_contents = infile.read()
    infile.close()
    print(file_contents)

main()