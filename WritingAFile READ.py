print("Creating text file with write method")
textfile=open("n:\write_it.txt", "w")
textfile.write("Line\n")
textfile.write("Hello\n")
textfile.write("Writing a file")
textfile.close()

textfile=open("n:\write_it.txt", "r")
print(textfile.read())
textfile.close()
