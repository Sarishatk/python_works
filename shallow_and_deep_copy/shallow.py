
from copy import copy,deepcopy

anu_food = [["dosa","sambar"],
            ["burger","shawarma"],
            ["kanji","chammandhi"]]

print(anu_food)

manu_food = deepcopy(anu_food)



manu_food[0][0] = "idli"

print(manu_food)



