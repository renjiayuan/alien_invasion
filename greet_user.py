def greet_users(names):
    for name in names:
        msg=f"Hello {name.title()}"
        print(msg)
usernames=['hanaah','ty','margot']
greet_users(usernames)