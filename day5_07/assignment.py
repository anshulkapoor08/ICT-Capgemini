# Define custom exceptions
class BlankNameError(Exception):
    """Raised when the name is blank."""
    pass

class InvalidEmailError(Exception):
    """Raised when the email does not end with .com or .in."""
    pass

# Function to get user input and validate
def validate_input(name, email):
    if not name.strip():  # Check if name is empty or just spaces
        raise BlankNameError("Error: Name cannot be blank.")
    
    if not (email.endswith(".akgec.ac.in") ):
        raise InvalidEmailError("Error: Email ID must end with .akgec.ac.in.")
    
    print("Validation successful! Name and Email are valid.")

# Main program
try:
    name = input("Enter Name: ").strip()
    email = input("Enter Email ID: ").strip()
    
    validate_input(name, email)

except BlankNameError:
    print("Name cannot be blank.")

except InvalidEmailError:
    print("Email ID must end with .akgec.ac.in.")