from constants import *
from functions import *

#SEE SECTION fonksiyonudur. amacı kullanıcıdan aldığı kelimeyi veritabanından çekip
#kullanıcıya kelimeyi ve anlamlarını gösterebilmektir.
def see():
    '''This function prints the stored meanings of the user-given word with \
the corresponding stored examples.
    '''
    # call function "header" from functions module to print the section name
    # in a fancy way:
    header("SEE SECTION")
    # with the while loop continuous search of multiple wordds is possible
    # unless any break statement inside the while loop:
    while 1:
        # call function "waiting" from functions module:
        waiting("Insert a Word", F2)
        # with the built-in function 'input', get the word from user that is
        # intended to insert into database. 'strip' built-in function returns a
        # copy of the typed word with the leading and trailing characters
        ## removed. These characters are the specified set of characters inside
        # the 'ignore_these' variable. You can access it from the 'constants'
        # module.
        word = input(">").strip(ignore_these).lower()
        # This if block exits the SEE SECTION and returns to the MAIN MENU:
        if not word:
            quitting("see")
            break
        # If user typed a non-alphabetic word, this if block prints proper
        # usage of the SEE SECTION and starts over the while loop:
        if not control(word)["is_it_valid"]:
            waiting("\nProper Usage:\ninsert a word\n>[word, not number or any \
weird character]\n", F2)
            continue
        # select the meanings and examples of the given and controlled word
        # from database by calling 'select_from' function from 'functions'
        # module:
        meanings = select_from(word)
        # check if there is not any record selected from database:
        if not meanings["Fields"]:
            waiting("\nNot Found...\nSorry :(\n", F2)
            timer(0.7)
            continue
        # print for aesthetic concerns:
        print()
        # iterate over field names:
        for field in meanings["Fields"]:
            # set variable 'sentence' for each iteration:
            sentence = ""
            # iterate over the meanings of the field name:
            for meaning in meanings["Fields"][field]:
                # update variable 'sentence' for printing and aesthetic
                # concerns:
                sentence += meaning + ", "
            else:
                # function 'modifier_for_viewing' returns the last modified
                # version of the sentence that includes meanings of the field
                # and field name in a custom way:
                waiting(modifier_for_viewing(sentence, field), F3)
        # iterate over Examples:
        for count, example in enumerate(meanings["Examples"]):
            # check if it is the first example and print custom 'Example'
            # header:
            if count == 0:
                waiting("\n" + "\\" * 5 + "__" + "Examples" + \
                        "__" + "/" * 5, F2)
            # print examples:
            waiting("({0}) {1}".format(count + 1, example), F3)
        else:
            # print for aesthetic concerns:
            if meanings["Examples"]:
                print("\n")
            else:
                print()
