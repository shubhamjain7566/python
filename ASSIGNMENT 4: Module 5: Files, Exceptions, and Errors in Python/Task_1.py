try :
    fileData = open("sample.txt", "r")
    print(f"Reading the file content\nLine 1: {fileData.readline()}Line 2: {fileData.readline()}")
    fileData.close()
except FileNotFoundError:
    print("Error: the file 'sample.txt' was not found.")