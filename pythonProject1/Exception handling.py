import os
import time


# Function to check if a notebook file exists and create one if it doesn't
def check_notebook_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            print("No default notebook was found, created one.")


# Function to change the notebook file
def change_notebook():
    new_file = input("Give the name of the new file: ")
    if not os.path.exists(new_file):
        with open(new_file, 'w') as file:
            print("No notebook with that name detected, created one.")
    return new_file


# Function to read the notebook
def read_notebook(filename):
    try:
        with open(filename, 'r') as file:
            notes = file.readlines()
            for note in notes:
                print(note.strip())
    except IOError:
        print("An error occurred while reading the notebook.")


# Function to add a note to the notebook
def add_note(filename):
    note = input("Write a new note: ")
    timestamp = time.strftime("%H:%M:%S %m/%d/%y")
    with open(filename, 'a') as file:
        file.write(f"{note}:::{timestamp}\n")


# Function to empty the notebook
def empty_notebook(filename):
    try:
        open(filename, 'w').close()
        print("Notebook is now empty.")
    except IOError:
        print("An error occurred while emptying the notebook.")


# Main program
def main():
    default_filename = "notebook.txt"
    current_filename = default_filename

    check_notebook_file(current_filename)

    while True:
        print(f"Now using file {current_filename}")
        print("(1) Read the notebook")
        print("(2) Add note")
        print("(3) Empty the notebook")
        print("(4) Change the notebook")
        print("(5) Quit")

        choice = input("Please select one: ")

        if choice == "1":
            read_notebook(current_filename)
        elif choice == "2":
            add_note(current_filename)
        elif choice == "3":
            empty_notebook(current_filename)
        elif choice == "4":
            new_filename = change_notebook()
            current_filename = new_filename
        elif choice == "5":
            print("Notebook shutting down, thank you.")
            return 0
        else:
            print("Invalid choice. Please select a valid option (1-5).")


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
