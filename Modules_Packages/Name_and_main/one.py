def func():
    print("Function inside one.py")

print("Top level of one.py")

if __name__ == "__main__":
    print("One.py is being run directly")
else:
    print("One.py is being imported into another module")
    