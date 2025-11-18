# def login_valid (email, password):
#     targetchar = "@"
#     if not email:
#         return "Please enter a email."
#     if email == " ":
#         return "Please enter a email without spaces in it"
#     if email.islower == 

#     password = input ("Please enter ur password")
        



def isvalid (email, password):
    if "@" not in email:
        return "Not vaild email"
    if " " in email:
        return "Spaces are not allowed in a email."
    char = len(password)
    if char < 8:
        return "You need at least 8 Characters in ur password."
    # if password.isupper:
    #     return ""
    # the commented lines of code above won't work because .upper is for the whole string to be uppercased.



    if (any(x.isupper() for x in password) and len < 0):
        return "Please put at least 1 uppercase letter in ur password."
    
    if (any(x.isdigit() for x in password) and len < 0):
        return "Please have at least 1 number in ur password"




    return {'Email':email, 'Password': password}

print(isvalid("test@gmail.com", "test1236"))







def isvalid(email, password):

    if "@" not in email:
        return "Not a valid email."
    if " " in email:
        return "Spaces are not allowed in an email."

    if len(password) <= 8:
        return "You need at least 8 characters in your password."

    if not any(x.isupper() for x in password):
        return "Please put at least 1 uppercase letter in your password."


    if not any(x.isdigit() for x in password):
        return "Please have at least 1 number in your password."

    return {'Email': email, 'Password': password}

print(isvalid("test @gmail.com", "test1236"))



