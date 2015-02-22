# Grocery randomizer and list-maker


#### PROJECT IDEAS:
# Auto-run once per week
# Email a list of food for the week?
# Use bash and cron for this?

import collections
from random import randint

# DICT of all the meals and the ingredients
meals = {
	"pizza" : ["dough", "sauce", "cheese"],
	"kale pasta" : ["pasta", "kale", "onions", "mushrooms", "red wine"],
	"sandwiches" : ["bread", "veggies", "cheese", "butter"],
	"chinese veggies" : ["broccoli", "ginger", "chillis", "eggs", "rice"],
	"peach curry" : ["tomatoes", "peaches", "onions"]
}

## Creates a reduced dictionary. If a duplicate occurs, loops again
choices = {}
meal_list = []
for x in range(0, int(raw_input("How many meals? "))):
	# picks a meal at random
	# if it's in the list, tries again
	# if not, adds it, then breaks the loop
	while True:
		y = meals.keys()[randint(0, (len(meals) - 1))]
		if y not in meal_list:
			meal_list.append(y)
			break 	 # adds to the meal list, breaks the loop
		else:
			pass	 # repeats the loop
	# adds ingredients to the choices dict
	choices[y] = meals[y]

# builds a list of ingredients needed	
ingr = [ingredients for meals in choices for ingredients in choices[meals]]

# counts multiple occurrences of ingredients and builds a list of ingr, then
# creates strings of the ingredients and their occurrences using list comprehension
list_ingr = [str(items[0]) + ": " + str(items[1]) for items \
		in [[x, collections.Counter(ingr)[x]] for x in collections.Counter(ingr)]]

# converts the list into a paragraph string of the list
strlist = ""
for items in list_ingr:
	strlist = strlist + "\n" + "%s" % items

# Prints the meals and ingredients/counters to the console
print meal_list
print strlist

# saves the meals and ingredients/counters into a .txt
with open("list.txt", "w+") as file:
	file.write(str(meal_list) + "\n\n\n" + strlist)

