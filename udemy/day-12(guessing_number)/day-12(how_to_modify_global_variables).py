
###################################
## How to modify global variables #
###################################

enemies = 1


def increase_enemies():

    print(f"enemies inside function: {enemies}")
    # enemies += 1
    # 👆 UnboundLocalError: local variable 'enemies' referenced before assignment
    return enemies + 1


enemies = increase_enemies()

print(enemies)
