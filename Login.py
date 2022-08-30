print("**********\nLogin Name\n**********\n")



sys_login_name = "odreto"

sys_password  = "12345" 

login_name = input("Login Name:") 

password =  input("Password:")

if (login_name != sys_login_name and password == sys_password):
    print("Login_Name Mistake...")
elif (login_name == sys_login_name and password != sys_password):
    print("Password Mistake...")

elif (login_name != sys_login_name and password != sys_password):
    print("Login_Name and Password Mistake...")

else:
    print("Successful...")

