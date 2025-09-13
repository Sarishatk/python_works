
from copy import copy,deepcopy

anu_food = [["dosa","sambar"],
            ["burger","shawarma"],
            ["kanji","chammandhi"]]

print(anu_food)

manu_food =copy(anu_food)

anu_food[0][0] = "idli"

print(manu_food)
