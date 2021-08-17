print("""
*************************
Username & Password Portal
*************************
""")

sys_username = "esero88"
sys_password = "password88"
attempt = 3

while True:
    username = input("username:")
    password = input("password:")
    if username != sys_username and password == sys_password:
        print("username is wrong...")
        attempt -= 1
    elif username == sys_username and password != sys_password:
        print("password is wrong...")
        attempt -= 1
    elif username != sys_username and password != sys_password:
        print("username and password is wrong...")
        attempt -= 1
    else:
        print("Successfully logged in")
        break
    if attempt == 0:
        print("Your attempt rights are finished...")
        break
