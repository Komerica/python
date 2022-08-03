import os

#############################
# How to create new folders #
#############################
print(os.getcwd())
path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)  # parents directory
print(os.getcwd())

for i in range(31, 41):
    if not os.path.exists(f"{path_parent}/day-{i}"):  # if folders exist, don't make it
        os.makedirs(f"{path_parent}/day-{i}")
