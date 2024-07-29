import bcrypt

# script to prompt for username, password, confirm the password, and store the hashed password

# Get username from user
username = input("Enter your username: ")

# Get password from user
password = input("Enter your password: ")

# Confirm password from user
confirm_password = input("Re-enter your password: ")

# Check if the passwords match
if password == confirm_password:
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    # Store the hashed password in a temporary variable
    temp_password = hashed_password
    print("Password has been hashed and stored in a temporary variable. Hashed value is {hashed_password}")
else:
    print("Passwords did not match. Please try one more time")
