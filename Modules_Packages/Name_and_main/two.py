import one

print("Top level of Two.py")

one.func()

if "__name__" == "__main__":
    print("Two.py is being run directly")
else:
    print("Two.py is being imported into the another module")