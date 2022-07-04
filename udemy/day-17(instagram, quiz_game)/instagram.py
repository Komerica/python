# Attribute is a variable that's associated with an object
# Attributes: the things that the object has  Ex) seats = 5  (if it was a Car class)
# Methods: the things that the object does.

#############
# Instagram #
#############

class User:
    # __init__ is normally used to initialize the attributes.
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
user_2 = User("002", "jack")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)




