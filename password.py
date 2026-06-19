 def validate_password(password) :
...     if len(password) < 8 :
...         return False, "password must be atleast 8 character."
...
...     if not any (char.isupper() for char in password) :
...         return False, "password must include at least one uppercase letter"
...
...     if len(password) % 2 == 0:
...        return False, "password length must be  an odd number"
...
...     else:
...         return True, "password created successfully you really done well!"
...
... while True:
...
...     user_password = input("create a secured password: ").strip()
...     valid, message = validate_password (user_password)
...     print(f"\n{message}")
...
...     if valid :
...         break
...     else:
...         print("try again.\n")
...