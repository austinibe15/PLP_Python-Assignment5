# file_handling_assignment.py  

def main():  
    try:  
        # File Creation: Create and write to a new text file  
        with open("my_file.txt", "w") as file:  
            file.write("Hello, World!\n")  
            file.write("This is the second line.\n")  
            file.write("The third line has a number: 123.\n")  
        
        print("File created and initialized successfully!")  

        # File Reading and Display: Read the contents of the file  
        with open("my_file.txt", "r") as file:  
            content = file.read()  
            print("\nContents of 'my_file.txt':")  
            print(content)  
        
        # File Appending: Open the file in append mode and add more lines  
        with open("my_file.txt", "a") as file:  
            file.write("This is the fourth line.\n")  
            file.write("Appending the fifth line with a number: 456.\n")  
            file.write("Finally, this is the sixth line.\n")  
        
        print("\nAdditional lines appended successfully!")  

    except FileNotFoundError:  
        print("Error: The file was not found.")  
    except PermissionError:  
        print("Error: You do not have permission to access the file.")  
    except Exception as e:  
        print(f"An unexpected error occurred: {e}")  
    finally:  
        print("\nFile handling operation completed.")  

if __name__ == "__main__":  
    main()