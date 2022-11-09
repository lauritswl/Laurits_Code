# # Importing from turtle module
# from turtle import Turtle, Screen
# # Importing from another module
# import another_module
# print(another_module.another_string)
#
#
# # From module turtle we import the class turtle and define Timmy as a turtle object.
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral3")
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(270)
# timmy.forward(100)
# print(timmy)
#
# #Define screen object
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()
#
# # You can find packages at pypi.org

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
print(table)