try :
    fileData = open("output.txt", "r+")
    textWrite  = input("Enter the text to write to the file: ")
    fileData.write(textWrite)
    print("Data successfully written to output.txt\n")
    fileData.close()

    fileData = open("output.txt", "a")
    textAppend = input("Enter additional text to append: ")
    fileData.write("\n")
    fileData.write(textAppend)
    print("Data successfully appended.\n")
    fileData.close()

    with open('output.txt', "r") as file:
        for line in file:
            print(line.strip())


except FileNotFoundError:
    print("Error: the file 'output.txt' was not found.")