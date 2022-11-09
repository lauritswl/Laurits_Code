class User:
    def __init__(self, user_id, username):
        # initialise attributes
        print("Print this when new user is created")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1




user_1 = User("001", "Laurits")
user_2 = User("002", "Martine")
print(
    "### Before following ###"
)
print(f"{user_1.username} following {user_1.following}")
print(f"{user_1.username} followers {user_1.followers}")
print(f"{user_2.username} following {user_2.following}")
print(f"{user_2.username} followers {user_2.followers}")
user_1.follow(user_2)
print(
    "### After following ###"
)
print(f"{user_1.username} following {user_1.following}")
print(f"{user_1.username} followers {user_1.followers}")
print(f"{user_2.username} following {user_2.following}")
print(f"{user_2.username} followers {user_2.followers}")


