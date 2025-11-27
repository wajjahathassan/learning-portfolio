"""Module providing a function printing python version."""
import random

print("""You are at the front door of a scary, old house.
      It looks dark and rusted.
      You are scared, but you really want to see what is inside.
      What do you do?""")
decision = input("(Open/Run): ")

if decision == "Open":
    print("""The door opens with a loud, creepy noise.
          Inside, you see a long, pitch black hallway and a staircase with dim lights.
          Where do you go?""")
    decision = input("(Enter the hallway/Go upstairs): ")

    if decision == "Enter the hallway":
        print("""It is pitch black in the hallway.
              Suddenly, you feel cold air and hear a child giggling... What do you do?""")
        decision = input("(Check for lights/Use flashlight): ")

        if decision == "Check for lights":
            print("""You find the switch and click it. Click!
                  But the house is old and rusted, so the lights do not work.
                  The loud click echoes in the dark.
                  The giggling stops... and you hear running footsteps coming for you!
                  Game Over!""")

        elif decision == "Use flashlight":
            print("""You turn on your flashlight.
                  The bright beam cuts through the pitch black darkness.
                  At the end of the long hall, you see two doors.
                  One is on the Left, and one is on the Right. Which door do you open?""")
            decision = input("(Left/Right): ")

            options = ["Left", "Right"]

            safe_door = random.choice(options)

            if decision == safe_door:
                print("""You enter the room and you see your wife.
                  She looks scared but safe.
                  You gently hold her hand and a bright light fills the room.
                  Suddenly, you wake up in your own bed!
                  Your wife is sleeping peacefully in your arms, looking as gorgeous and beautiful as ever.
                  It was just a bad dream!""")
            elif decision == "Left":
                print("""You walk into the room and everything goes black.
                Suddenly, you find yourself at the front door of a scary, old house.
                It looks dark and rusted.
                You are scared, but you really want to see what is inside and ...
                ... your nightmare continues ...""")
            elif decision == "Right":
                print("""You walk into the room and everything goes black.
                Suddenly, you find yourself at the front door of a scary, old house.
                It looks dark and rusted.
                You are scared, but you really want to see what is inside and ...
                ... your nightmare continues ...""")
            else:
                print("Awwww maayyynn! Not this agaaiiinn!")

        else:
            print("Oh my Gawd bro, hell noo!")

    elif decision == "Go upstairs":
        print("""You walk up the creaky stairs to find some light.
              At the top, you see two doors. Which door do you open?""")
        decision = input("(Door 1/Door 2): ")

        options = ["Door 1", "Door 2"]
        safe_door = random.choice(options)

        if decision == safe_door:
            print("""You enter the room and you see your wife.
                  She looks scared but safe.
                  You gently hold her hand and a bright light fills the room.
                  Suddenly, you wake up in your own bed!
                  Your wife is sleeping peacefully in your arms, looking as gorgeous and beautiful as ever.
                  It was just a bad dream!""")
        elif decision == "Door 1":
            print("""You walk into the room and everything goes black.
                Suddenly, you find yourself at the front door of a scary, old house.
                It looks dark and rusted.
                You are scared, but you really want to see what is inside and ...
                ... your nightmare continues ...""")
        elif decision == "Door 2":
            print("""You walk into the room and everything goes black.
                Suddenly, you find yourself at the front door of a scary, old house.
                It looks dark and rusted.
                You are scared, but you really want to see what is inside and ...
                ... your nightmare continues ...""")
        else:
            print("Why this science fudging man?")

    else:
        print("Ain't nobody got time for that!")

elif decision == "Run":
    print("You chose sanity... but... Game Over!")
else:
    print("Whaaaaaaaaaaaaaaaaaaaaaaattt???")
