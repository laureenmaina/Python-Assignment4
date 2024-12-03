def read_and_modify_file():
    # Prompt the user for a filename
    fileinput = input("Please enter your text file name (without extension): ")
    filename = fileinput + ".txt"

    try:
        with open(filename, "r") as file:
            data = file.readlines()
        
        # Modify the data (eg, converting to uppercase)
        modified_data = [line.upper() for line in data]

        # Writes the modified data to the new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.writelines(modified_data)

        print(f"Modified file has been created: {new_filename}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except IOError:
        print("Error: An error occurred while reading or writing to the file.")
    except Exception as e:
        print(f"Unhandled exception: {e}")


read_and_modify_file()