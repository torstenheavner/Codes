# import tkinter as tk
import colorama
import matplotlib.pyplot as plt
from pynput import keyboard
# from tkinter import simpledialog
from termcolor import colored

colorama.init()
# root = tk.Tk()
# root.withdraw()

direction = "north"
biome = input("ENTER YOUR BIOME: ")
coordinates = [0, 0]

biomes = {
    "ocean": "#0077ff",
    "beach": "#eeff33",
    "oak forest": "#00aa33",
    "flower forest": "#ffaadd",
    "birch forest": "#bbbbbb",
    "dark oak forest": "#005500",
    "jungle": "#337700",
    "taiga": "#448722",
    "swamp": "#446633",
    "savanna": "#99cc88",
    "plains": "#aaff99",
    "desert": "#eeff66",
    "snowy": "#ffffff",
    "mountains": "#777777",
    "badlands": "#ee8822",
}

# coords = simpledialog.askstring(title="COORDINATES", prompt="ENTER YOUR COORDINATES")
coords = input("ENTER YOUR COORDS: ")
coordinates = coords.split(", ")
for num in range(len(coordinates)):
    coordinates[num] = int(coordinates[num])

plt.plot(coordinates[0], coordinates[1], label=biome, color=biomes[biome])


# root.mainloop()

# def get_input(title, prompt):
# 	return simpledialog.askstring(title=title, prompt=prompt)

def on_press(key):
    global direction, biome, coordinates
    change_direction = False
    try:
        k = key.char
    except:
        k = key.name

    # print(k)

    if k == "home":
        return False

    if k in ["up", "down", "left", "right"]:
        change_direction = True

    if k == "up":
        direction = "north"
    elif k == "down":
        direction = "south"
    elif k == "left":
        direction = "west"
    elif k == "right":
        direction = "east"

    elif k == "end":
        inn = input("ENTER NEW BIOME: ")
        biome = inn

    elif k == "insert":
        if direction == "up":
            coordinates[1] -= 50
        elif direction == "down":
            coordinates[1] += 50
        elif direction == "west":
            coordinates[0] -= 50
        elif direction == "east":
            coordinates[0] += 50
        plt.plot(coordinates[0], coordinates[1], label=biome, color=biomes[biome])
        print("PLOTTED [%s] POINT AT %s" % (colored(biome.upper(), "red"), colored(coordinates, "cyan")))

    elif k == "page_down":
        plt.show()

    if change_direction:
        print("[%s] CHANGED TO [%s]" % (colored("DIRECTION", "green"), colored(direction, "blue")))


listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
