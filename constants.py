from random import choice

# define which variables can be imported when "from constants import *"
# statement is executed:
__all__ = ["F0", "F1", "F2", "F3", "ignore_these", "valid_fields", "user_name", "file_name",
            "produce_random_calling", "produce_random_farewell", "NoWord"]

# hardcoded second values for the purpose of printing text one by one
# to the screen or keeping waiting the program:
F0 = 0.015
F1 = 0.03
F2 = 0.04
F3 = 0.05

# hrdcoded specific characters for the purpose of stripping the given input
# from the user:
ignore_these = ".!#,*:() "

# valid field names:
valid_fields = ["Adjective", "Adverb", "Conjunction", "Determiner", "Noun", \
                "Phrase", "Preposition", "Pronoun", "Verb"]

# reading user name and database file name from configuration.txt file
# and appending them into list:
tmp_list = []
with open("configuration.txt", mode="r") as tmp_file:
    for line in tmp_file:
        tmp_list.append(line[line.find(" ") + 1:line.find("\n")])

# unpacking and assigning a collection of values:
user_name, file_name = tmp_list
# capitalize() method of str instance returns a copy of string with its first
# character capitalized and rest lowercased:
user_name = user_name.capitalize()

# list that contains calling and farewll expressions:
calling_list = ["my lord", "darling", user_name, "master",
                "sir", "sir " + user_name]
farewell_list = ["See you soon...", "I hope I can see you again...",
                 "See you later...", "Goodbye sir " + user_name + "...",
                 "Thank you for your time...", "Work Hard!\nNever Give Up!"]

# define functions that are returning a member of a given list randomly:
def produce_random_calling():
    return choice(calling_list)

def produce_random_farewell():
    return produce_random_calling() + "\n" + choice(farewell_list)

class NoWord(Exception):
    pass
