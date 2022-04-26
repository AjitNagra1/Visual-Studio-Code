def test_username(username,password):
    if username=='PythonPadawan' and password=='honduras123':
        print('Welcome PythonPadawan')
    else:
        print('User with name',username,'and password',password,'does not exist!')

username=input('What is your username? - ')
print(username)
password=input('What is your password? - ')
test_username(username,password)