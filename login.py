
def login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Invalid Username or Password"


# Test the login function
print(login("admin", "1234"))
print(login("user", "wrong"))
