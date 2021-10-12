locations = {0: "You are sleeping",
             1: "You are walking on a road",
             2: "You are at the top of a hill",
             3: "You are inside a building",
             4: "You are in a valley",
             5: "You are in the forest"}
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
words = {"North": "N", "East": "E", "West": "W", "South": "S", "Quit": "Q"}
loc = 1
while True:
    key = []
    def getKeysByValue1(dictOfElements, valueToFind):
        Key = ""
        listOfItems = dictOfElements.items()

        for item in listOfItems:

            if item[1] == valueToFind:
                Key = item[0]
        return Key



    availableExits = "".join(exits[loc].keys())
    # print(availableExits)
    for i in availableExits:
        if i != None:
            key.append(getKeysByValue1(words,i))
    # print(key)
    # while ('' in key):
    #     key.remove('')

    print(locations[loc])
    if loc == 0:
        break

    direction = input("Available exits are: " + ', '.join(key) + " ").capitalize()
    print()

    if words[direction] in exits[loc]:
        loc = exits[loc][words[direction]]

    else:
        print("You cannot go in that direction")


