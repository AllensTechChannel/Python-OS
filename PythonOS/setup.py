# Ask for the user's name
owner = input("Create a Username: ")

# Save the username to 'SYSTEM//owner.txt'
with open('SYSTEM//owner.txt', 'w') as f:
    f.write(owner)

# Define the path to the input file
file_path = 'SYSTEM//owner.txt'

# Try to read the first character from the file
try:
    with open(file_path, 'r') as file_obj:
        first_char = file_obj.read(1)
    
    # If the file is empty (first_char is empty)
    if not first_char:
        # Update owner.txt with the username again
        with open('SYSTEM//owner.txt', 'w') as f:
            f.write("user name")

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

# Ask for the company name
company = input("Enter Your Organization: ")

# Save the company name to 'SYSTEM//ownercompany.txt'
with open('SYSTEM//ownercompany.txt', 'w') as f:
    f.write(company)


# Define the path to the input file
file_path = 'SYSTEM//ownercompany.txt'

# Try to read the first character from the file
try:
    with open(file_path, 'r') as file_obj:
        first_char = file_obj.read(1)
    
    # If the file is empty (first_char is empty)
    if not first_char:
        # Update owner.txt with the username again
        with open('SYSTEM//ownercompany.txt', 'w') as f:
            f.write("org name")

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

# Ask for the company name
company = input("Create a Password: ")

# Save the company name to 'SYSTEM//ownercompany.txt'
with open('SYSTEM//pwd.txt', 'w') as f:
    f.write(company)


# Define the path to the input file
file_path = 'SYSTEM//pwd.txt'

# Try to read the first character from the file
try:
    with open(file_path, 'r') as file_obj:
        first_char = file_obj.read(1)
    
    # If the file is empty (first_char is empty)
    if not first_char:
        # Update owner.txt with the username again
        with open('SYSTEM//pwd.txt', 'w') as f:
            f.write("defaultpassword")

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
    
