
def decoder(password):
    password = list(password)
    password = [int(x) for x in password]

    for i in range(len(password)):
        password[i] -= 3
        if password[i] <= 0:
            password[i] += 10

    return "".join(str(num) for num in password)