"""
📘 File Operations in Python
----------------------------
This script demonstrates basic file handling operations in Python:
1. Opening a file
2. Reading/Writing/Appending data
3. Closing or removing a file

Supported Modes:
----------------
'r'  -> Read (default)
'w'  -> Write (creates/overwrites file)
'a'  -> Append
'r+' -> Read and Write
'w+' -> Write and Read (overwrites file)
'a+' -> Append and Read
"""

import os

def write_to_file(filename, text):
    """
    Writes text to a file (overwrites if file already exists).
    """
    with open(filename, 'w') as f:
        f.write(text)
    print(f"✅ Written successfully to '{filename}'.")


def append_to_file(filename, text):
    """
    Appends text to an existing file or creates one if not found.
    """
    with open(filename, 'a') as f:
        f.write(text)
    print(f"✅ Appended successfully to '{filename}'.")


def read_from_file(filename):
    """
    Reads and prints the content of a file.
    """
    try:
        with open(filename, 'r') as f:
            text = f.read()
            print(f"📄 Content of '{filename}':\n{text}")
    except FileNotFoundError:
        print("❌ File not found!")


def delete_file(filename):
    """
    Deletes a file if it exists.
    """
    if os.path.exists(filename):
        os.remove(filename)
        print(f"🗑️ File '{filename}' deleted successfully.")
    else:
        print("❌ File not found, nothing to delete.")


def main():
    """
    Example usage of file operations.
    Uncomment the operations you want to test.
    """
    # text = input("Enter your text: ")

    # write_to_file('file1.txt', text)
    # append_to_file('file1.txt', '\n' + text)
    # read_from_file('file1.txt')
    # os.rename('file1.txt', 'file2.txt')
    delete_file('file2.txt')


if __name__ == "__main__":
    main()
