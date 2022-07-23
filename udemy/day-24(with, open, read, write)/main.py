# THIS WAY, always have to remember to close file!
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()  # Always mustn't forget this!

# Instead, developers prefer to use "with" that doesn't require "close" at the end.
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# with open ("my_file.txt", mode="r") as file:
#         = with open ("my_file.txt") as file:  # Default: Read only mode (cannot write)
# with open ("my_file.txt", mode="w") as file:  # Delete all the previous text and write new text
# with open ("my_file.txt", mode="a") as file:  # Append mode
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# When mode="w" and if the file doesn't exist, it's going to create a new file for you.
with open("new_file.txt", mode="w") as file:
    file.write("New text.")