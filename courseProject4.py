def open_user_file():
    try:
        file = open("user_data.txt", "a+")
        user_ids = []
        file.seel(0)
        for line in file:
            user_data = line.strip().split("|")
            user_id = user_data[0]
            user_ids.append(user_id)
        return file, user_ids
    except IOError:
        print("Error: unable to open user data file.")
        return None, None

def collect_user_info(file, user_ids):
    print("Enter user information ('End' to terminate):")
    while True:
        user_id = input("User ID: ")
        if user_id.lower() == "end":
            break

        if user_id in user_ids:
            print("User ID already exist. Please enter a different ID.")
            continue 

        password = input("Password: ")
        authorization = input("Authorization code (Admin/User): ")
        if authorization.lower() not in ["admin", "user"]:
            print("Invalid authorization code. Please enter 'Admin' or 'user'.")
            continue

        file.write(f"{user_id}|{password}|{authorization}\n")
        user_ids.append(user_id)

    print("User information collected successfully")

def display_user_info(file):
    print("=== User Information ===")
    file.seek(0)
    for line in file:
        user_data = line.strip().split("|")
        user_id = user_data[0]
        password = user_data[1]
        authorization = user_data[2]
        print(f"User ID: {user_id}")
        print(f"Password: {password}")
        print(f"Authorization code: {authorization}")
        print()

def main():
    file, user_ids = open_user_file()
    if file is None or user_ids is None:
        return

    collect_user_info(file, user_ids)
    display_user_info(file)

    file.close()

main()

class Login:
    def __init__(self, user_id, password, authorization):
        self.user_id = user_id
        self.password = password
        self.authorization = authorization

    def user_login():
        user_ids = []
        password = []
        authorization = []

        with open("user_data.txt", "r") as file:
            for line in file:
                user_data = line.strip().split("|")
                user_id = user_data[0]
                password = user_data[1]
                authorization = user_data[2]

                user_ids.append(user_ids)
                password.append(password)
                authorization.append(authorization)

        input_user_id = input("Enter User ID: ")
        if input_user_id not in user_ids:
            print("Invalid User ID.")
            return

        user_index = user_ids.index(input_user_id)
        input_password = input("Enter password: ")
        if input_password != password[user_index]:
            print("Invalid Password.")
            return

        authorization = authorization[user_index]
        login = Login(input_user_id, input_password, authorization)

        if authorization.lower() == "admin":
            (login)