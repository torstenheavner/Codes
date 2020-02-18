from math import *

mat = {
    "cable": 0,
    "copper": 0,
    "rubber": 0,
    "redstone": 0,
    "iron": 0,
    "diamond": 0,
    "refiron": 0,
    "glowstone": 0,
    "lapis": 0,
    "cobble": 0,
    "lead": 0,
    "tin": 0,
    "glasspane": 0,
    "coaldust": 0,
    "diamondust": 0,
    "glass": 0,
    "flint": 0,
    "waterbucket": 0,
    "----------------": 1,
    "circut": 0,
    "advancircut": 0,
    "furnace": 0,
    "machineframe": 0,
    "advanmachineframe": 0,
    "bronze": 0,
    "advancedalloy": 0,
    "carbonplate": 0,
    "battery": 0,
    "coolantcell": 0,
    "generator": 0
}


def cable():
    global mat
    mat["rubber"] = mat["rubber"] + ((6 * mat["cable"]) / 6)
    mat["copper"] = mat["copper"] + ((3 * mat["cable"]) / 6)


def ironplate(count):
    global mat
    mat["iron"] = mat["iron"] + count


def circut(count):
    global mat
    mat["cable"] = mat["cable"] + (6 * count)
    mat["redstone"] = mat["redstone"] + (2 * count)
    mat["refiron"] = mat["refiron"] + count
    mat["circut"] = mat["circut"] + count


def advancircut(count):
    global mat
    circut(count)
    mat["redstone"] = mat["redstone"] + (4 * count)
    mat["glowstone"] = mat["glowstone"] + (2 * count)
    mat["lapis"] = mat["lapis"] + (2 * count)
    mat["advancircut"] = mat["advancircut"] + count


def furnace(count):
    global mat
    mat["cobble"] = mat["cobble"] + (8 * count)
    mat["furnace"] = mat["furnace"] + count


def machineframe(count):
    global mat
    mat["refiron"] = mat["refiron"] + (8 * count)
    mat["machineframe"] = mat["machineframe"] + count


def advanmachineframe(count):
    global mat
    machineframe(count)
    advancedalloy(count * 2)
    carbonplate(count * 2)
    mat["advanmachineframe"] = mat["advanmachineframe"] + count


def advancedalloy(count):
    global mat
    mat["refiron"] = mat["refiron"] + (3 * count)
    mat["tin"] = mat["tin"] + (3 * count)
    bronze(count * 3)
    mat["advancedalloy"] = mat["advancedalloy"] + count


def bronze(count):
    global mat
    mat["tin"] = mat["tin"] + count
    mat["copper"] = mat["copper"] + (count * 3)
    mat["bronze"] = mat["bronze"] + count


def carbonplate(count):
    global mat
    mat["coaldust"] = mat["coaldust"] + (count * 8)
    mat["carbonplate"] = mat["carbonplate"] + count


def battery(count):
    global mat
    mat["cable"] = mat["cable"] + count
    mat["lead"] = mat["lead"] + (4 * count)
    mat["redstone"] = mat["redstone"] + (2 * count)
    mat["battery"] = mat["battery"] + count


def generator(count):
    global mat
    furnace(count)
    machineframe(count)
    battery(count)
    mat["generator"] = mat["generator"] + count


def grinder(count):
    global mat
    mat["flint"] = mat["flint"] + (count * 3)
    mat["cobble"] = mat["cobble"] + (count * 2)
    machineframe(count)
    circut(count)


def industrialgrinder(count):
    global mat
    advancircut(count * 3)
    grinder(count)
    advanmachineframe(count)


def basicsolarpanel(count):
    global mat
    mat["glasspane"] = mat["glasspane"] + (3 * count)
    mat["coaldust"] = mat["coaldust"] + (3 * count)
    generator(count)
    circut(2 * count)


def advansolarpanel(count, basic):
    global mat
    mat["glass"] = mat["glass"] + (3 * count)
    mat["coaldust"] = mat["coaldust"] + (3 * count)
    if not basic:
        machineframe(count)
    advancircut(2 * count)


def industrialsolarpanel(count, advanced):
    global mat
    mat["diamondust"] = mat["diamondust"] + (3 * count)
    mat["glass"] = mat["glass"] + (3 * count)
    if not advanced:
        machineframe(count)
    advancircut(2 * count)


def coolantcell(count):
    global mat
    if count % 2 == 1:
        count = count + 1
    mat["tin"] = mat["tin"] + ((count / 2) * 4)
    mat["waterbucket"] = mat["waterbucket"] + (count / 2)
    mat["collantcell"] = mat["coolantcell"] + count


def overclockupgrade(count):
    global mat
    mat["cable"] = mat["cable"] + (count * 2)
    circut(count)
    coolantcell(count * 3)


def energycrystal(count):
    global mat
    mat["redstone"] = mat["redstone"] + (count * 8)
    mat["diamond"] = mat["diamond"] + count


def lapotron(count):
    global mat
    mat["lapis"] = mat["lapis"] + (count * 6)
    circut(count * 2)
    energycrystal(count)


while 1:
    mat = {
        "cable": 0,
        "copper": 0,
        "rubber": 0,
        "redstone": 0,
        "iron": 0,
        "diamond": 0,
        "refiron": 0,
        "glowstone": 0,
        "lapis": 0,
        "cobble": 0,
        "lead": 0,
        "tin": 0,
        "glasspane": 0,
        "coaldust": 0,
        "diamondust": 0,
        "glass": 0,
        "flint": 0,
        "waterbucket": 0,
        "----------------": 1,
        "circut": 0,
        "advancircut": 0,
        "furnace": 0,
        "machineframe": 0,
        "advanmachineframe": 0,
        "bronze": 0,
        "advancedalloy": 0,
        "carbonplate": 0,
        "battery": 0,
        "coolantcell": 0,
        "generator": 0
    }
    item = input("\n\nItem: ").lower()
    count = int(input("Count: "))

    if item == "grinder":
        grinder(count)

    elif item == "oupgrade":
        overclockupgrade(count)

    elif item == "bsp":
        basicsolarpanel(count)

    elif item == "asp":
        basic = input("Do you already have basic solar panels? (y/n): ")
        if basic == "y":
            basic = True
        else:
            basic = False
        advansolarpanel(count, basic)

    elif item == "isp":
        advanced = input("Do you already have advanced solar panels? (y/n): ")
        if advanced == "y":
            advanced = True
        else:
            advanced = False

        industrialsolarpanel(count, advanced)

    else:
        try:
            eval("%s(%s)" % (item, count))
        except:
            pass

    cable()
    for key, item in mat.items():
        if item != 0:
            if item <= 64:
                print("%s %s" % (item, key))
            else:
                print("%s %s (%s full stacks, with %s extra)" % (
                item, key, floor(item / 64), item - (floor(item / 64) * 64)))
