try:
    File = open("this.txt","r")
except EOFError as e:
    print("EOF Error")
except IOError as e:
    print("We are able to Handle This Error.")
finally:
    print("This Will be Printed Irrespective Of Exception Error Occoured.")

