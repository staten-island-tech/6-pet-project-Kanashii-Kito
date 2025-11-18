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
    if char > 8:
        return "You need at least 8 Characters in ur password."


    return {'Email':email, 'Password': password}

print(isvalid("test", "test"))
