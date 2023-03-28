#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
["Alain", "Brian", "Chris", "Justin", "Angela", "Rick"]
Choose a person from the list to replace:Rick
Enter the replacement:Dan
["Alain", "Brian", "Chris", "Justin", "Angela", "Dan"]

"""

people = ["Alain", "Brian", "Chris", "Justin", "Angela", "Rick"]
print(people)

replaceing = str(input("enter a name on the list: "))
replacement = str(input("enter a name of your choosing: "))
x = people.index(replaceing)
people.insert(x, replacement)
people.remove(replaceing)
print(people)