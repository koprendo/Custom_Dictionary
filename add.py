from constants import *
from functions import *

def add():
    '''This function inserts the user-given word and its meaning into the \
database file which is specified in the configuration.txt file.
    '''
    # call function "header" from functions module to print the section name
    # in a fancy way:
    header("ADD SECTION")
    # with while loop continuous addition of words into database is possible
    # unless any break statement inside the while loop:
    while True:
        # call function "waiting" from functions module:
        waiting("Insert a Word", F2)
        # with the built-in function 'input', get the word from user that is
        # intended to insert into database. 'strip' built-in function returns a
        # copy of the typed word with the leading and trailing characters
        ## removed. These characters are the specified set of characters inside
        # the 'ignore_these' variable. You can access it from the 'constants'
        # module.
        word = input(">").strip(ignore_these).lower()
        # This if block exits the ADD SECTION and returns to the MAIN MENU:
        if not word:
            quitting("add")
            break
        # control function returns a dictionary which has information about
        # existence of space and non-alphabetic character in the word:
        test_of_word = control(word)
        # If user typed a non-alphabetic word, this if block prints proper
        # usage of the ADD SECTION and starts over the while loop:
        if not test_of_word["is_it_valid"]:
            waiting("\nProper Usage:\ninsert a word\n>[word, not number or any \
weird character]\n", F2)
            continue

        waiting("Insert the Meaning", F2)
        # get the meaning and class of the user-given word by calling 'input'
        # built-in function:
        meaning_sentence = input(">").strip(ignore_these).lower()
        # this code block exits the ADD SECTION and returns to the MAIN MENU
        # when nothing typed by the user:
        if not meaning_sentence:
            quitting("add")
            break

        test_of_meaning = control(meaning_sentence)

        if not test_of_meaning["is_it_valid"]:
            waiting("\nInsert the meaning with the class of the word, not \
number or any weird character\n", F2)
            continue
        # since the meaning sentence requires the class of the world after the
        # corresponding meaning of the user-given word, space character must be
        # placed between them. This if block checks it and restart the whole
        # addition process from scratch in case of absence of the space
        # character:
        if test_of_meaning["no_space"]:
            waiting("\nProper Usage:\ninsert the meaning\n>[meaning of the \
word] + [space] + [class of the word]\n", F2)
            continue
        # expected meaning sentence from user requires at least one space
        # between meaning of the word and the class of the word. Since
        # the leading and trailing spaces removed by 'strip' function, the last
        # space character positions just before the class of the word. The
        # code below returns that position's index:
        field_space_index = meaning_sentence.rfind(" ")
        # seperating meaning and the class of the word by using the
        # value of the variable 'field_space_index':
        meaning, field = meaning_sentence[:field_space_index].strip(), \
                       meaning_sentence[field_space_index:].strip().capitalize()
        # check if the user-given class is not valid:
        if field not in valid_fields:
            waiting("\nYou must specify a valid class of the word. See defined \
valid classes for the program below:\n" + ", ".join(valid_fields), F2)
            continue
        # check if the user-given class is Example:
        if field == "Example":
            waiting("\nTo add example text, type 'exadd' command in the main \
menu...", F3)
            quitting("add")
            break
        # check if the user-gien class of the word is not Phrase when the word
        # includes at least one space. Only the 'Phrase' typed words can include
        # space character:
        if not test_of_word["no_space"]:
            if field != "Phrase":
                waiting("\nOnly the 'Phrase' word class can contain spaces when\
 you're inserting the word.\n", F2)
                continue
        # 'insert_into' function from the functions module inserts the given
        # arguments into the database and returns a message for successful
        # operation when insertion is done. Any exception throughout the process
        # of the function, returns 'None':
        inserting_status = insert_into(word, meaning, field)
        # If insertion failed, execute the if block below:
        if inserting_status == None:
            waiting("\nSomething went wrong when inserting the word into the \
database.\nContact with the programmer.\n", F2)
            continue
        # print the message for successful insertion process:
        else:
            waiting(inserting_status, F2)
