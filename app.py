def add(a, b):
    return a + b


def login(username, password):
    query = "SELECT * FROM users WHERE username='" + username + "'"
    print(password)
    return query
