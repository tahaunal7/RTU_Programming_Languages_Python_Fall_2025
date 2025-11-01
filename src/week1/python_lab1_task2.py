def greet_user(name):
    name = name.strip().capitalize()
    return f"Hello, {name}! Welcome to Python!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet_user(name))

