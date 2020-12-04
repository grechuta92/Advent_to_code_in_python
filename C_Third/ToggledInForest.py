import math


class Forest:
    """
     Small Forest:
        Correct answer:
            Multiple: 336
        Correct list:
            [2, 7, 3, 4, 2]

    Large Forest:
        Correct answer:
            Multiple: 7812180000

        Correct list:
            [100, 276, 85, 90, 37]
    """

    file = open("ForestLarge.txt", "r")
    list_forest = [var.rstrip("\n") for var in file]
    list_forest_extended = []
    file.close()
    list_trees = []

    move_right = 0
    move_down = 0
    vertical_index = 0
    horizontal_index = 0
    vertical_length = 0
    horizontal_length = 0
    horizontal_length_extended = 0
    vertical_length_extended = 0
    div_move = 0
    div_down = 0

    def move(self, right, down):
        self.list_forest_extended.clear()
        self.horizontal_index = 0
        self.vertical_index = 0
        self.vertical_length = 0
        self.horizontal_length = 0
        self.horizontal_length_extended = 0
        self.vertical_length_extended = 0
        self.div_move = 0
        self.div_down = 0

        self.move_right = int(right)
        self.move_down = int(down)

        print()
        self.horizontal_length = self.list_forest[-1].__len__()  # 11

        self.vertical_length = self.list_forest.__len__()  # 11

        self.div_move = int((self.vertical_length / self.horizontal_length))

        self.div_down = math.ceil((self.vertical_length / self.move_down) / self.horizontal_length)

        if self.move_right >= self.move_down:
            for var in self.list_forest:
                self.list_forest_extended.append(var * (self.move_right * (self.div_move + 1)))
        else:
            if int(self.div_move) == 0:
                self.div_move = 1
            for var in self.list_forest:
                self.list_forest_extended.append(var * self.div_down)

        self.vertical_length_extended = self.list_forest_extended.__len__()
        self.horizontal_length_extended = self.list_forest_extended[-1].__len__()

    def make_move(self):
        self.horizontal_index += self.move_right
        self.vertical_index += self.move_down


class Toboggan:
    moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    forest = Forest()
    trees_counter = 0
    multiple_trees_counter = 1

    for var in moves:
        trees_counter = 0
        forest.move(var[0], var[1])
        while forest.vertical_index < forest.vertical_length_extended and forest.horizontal_index <= forest.horizontal_length_extended:

            x = forest.list_forest_extended[forest.vertical_index][forest.horizontal_index]

            if x == "#":
                trees_counter += 1
                forest.make_move()
            elif x == ".":
                forest.make_move()
            else:
                break

        forest.list_trees.append(trees_counter)

    for var in forest.list_trees:
        multiple_trees_counter *= var

    temp_index = 0
    for var in moves:
        print(var[0], "turn right")
        print(var[1], "go down")
        print("Number of trees =", forest.list_trees[temp_index], end="\n\n")
        temp_index += 1

    print("Multiple value of trees counter from every board = ", multiple_trees_counter)
