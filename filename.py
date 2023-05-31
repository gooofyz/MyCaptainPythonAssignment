filename= input("Enter the Filename: \n")
extension= filename.split(".")
if extension[-1]== "py":
    print("Python Extension")
elif extension[-1]== "java":
    print("Java Extension")
elif extension[-1]== "html":
    print("HTML Extension")
elif extension[-1]== "c":
    print("C Extension")
else:
    print(" Sorry,I dont know!")