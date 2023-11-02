import pyperclip

# Copy a string to the clipboard
pyperclip.copy("This is a string.")

# Paste the string
print(pyperclip.paste())

def read_file(filename):
  """Reads the contents of a text file and returns it as a string."""
  with open(filename, "r") as f:
    return f.read()


def main():
  """Reads the contents of a text file and prints it to the console."""
  filename = input("Enter the filename: ")
  contents = read_file(filename)
  print(contents)

if __name__ == "__main__":
  main()


