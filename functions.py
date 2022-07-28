import sqlite3
import time
import string
import random
from constants import *
from collections import defaultdict


def modifier_for_viewing(sentence, field):
    '''This function returns the given meaning sentence and field name combined\
 in a custom format.
    '''
    before, _sep, after = sentence.rpartition(", ")
    return "{0}  ({1})".format(before, field)


def control(word):
    '''This function checks the given word with two considerations:\n\
1- Is there any space in the given word?\n\
2- Are all character in the given word alphabetic?\n\n\
Function returns a dictionary object:\n\
return  {"is_it_valid": ::bool::, "no_space": ::bool::}
    '''
    no_space = True
    if " " in word:
        no_space = False
        word = word.replace(" ", "")
    return {"is_it_valid": word.isalpha(), "no_space": no_space}


def timer(number):
    '''This function keeps program waiting for a given time value.
It uses sleep function from time module.
    '''
    time.sleep(number)


def create_verification():
    word = str()
    for i in range(3):
        number = random.randint(0, len(string.ascii_lowercase) - 1)
        letter = string.ascii_lowercase[number]
        word += letter
    return word


def waiting(message, time):
    '''This function prints the given message to the screen character by \
character and keep program waiting for a given time value after printing \
each character of the given message.
    '''
    for index in range(len(message)):
        # set the flush keyword argument as True in order to flush the
        # buffered output and set the end keyword argument as "" to prevent
        # any modification of original message when writing the message
        # character by character:
        print(message[index], end="", flush=True)
        timer(time)
    # exhaustion of for loop executes else block:
    else:
        print()


def header(header):
    '''This function prints the given name of the section header in a specific \
format.
It calls waiting function from functions module.
    '''
    waiting("\n" + "-" * 5 + header + "-" * 5, F1)


def quitting(name):
    '''This function returns quitting message from various sections.
    '''
    waiting("\nQuitting from " + name + " section....\nReturning to main \
menu...\n", F0)


def insert_into(word, meaning, field, *, file=file_name):
    '''This function inserts the given word, meaning, and the class of it into \
database.\n\Database information stored in the variable 'file_name'.\n\You \
can specify another database file with the syntax:\n\
    insert_into(word, meaning, field, file=::another_database_file::)\n\
But this is not recommended. The default value of the file parameter is the \
variable 'file_name' from constants module.
    '''
    # try-except-else-finally block in order to manage the process of the
    # connecting database and insertion successfully:
    try:
        # create a connection object that represents the database:
        con = sqlite3.connect(file)
        # create a cursor object by using the cursor() method of connection
		# instance:
        cur = con.cursor()
        # executescript for execution of multiple SQL statements at once:
        cur.executescript("""
            INSERT OR IGNORE INTO {0} (title) VALUES ('{1}');
            INSERT OR IGNORE INTO Word (title) VALUES ('{2}');
            INSERT OR IGNORE INTO connection (word_id, field_id, field) VALUES (
                (SELECT id FROM Word WHERE title = '{2}'),
                (SELECT id FROM {0} WHERE title = '{1}'),
                '{0}');""".format(field, meaning, word))
        # save the changes
        con.commit()
    # sqlite3.Error is a base class of the other exceptions in this module.
	# Therefore, it catches all sqlite3 related errors:
    except sqlite3.Error:
        raise Exception("Something went wrong when you tried to add data into \
the database. Contact the programmer.")
    # else block executed only if try statement is executed without any error.
    # this block enables function to return a message for successful operation:
    else:
        return "\nWell done. You have added a meaningful information.\n"
    # close connection
    finally:
        con.close()


def select_from(word, *, file=file_name):
    '''This function selects the meaning of the given word from the default \
database and returns it in a custom data structure:\n\
    {'Fields': collections.defaultdict(set), 'Examples': []}\n\
\nYou can specify another database file with the syntax:\n\
    select_from(word, file=::another_database_file::)\n\
But this is not recommended. The default value of the file parameter is the \
variable 'file_name' from constants module.
    '''
    try:
        # create a connection object that represents the database:
        con = sqlite3.connect(file)
        # create a cursor object by using the cursor() method of connection
		# instance:
        cur = con.cursor()
        # create defaultdict object (subclass of dict class) from collections
        # module. default_factory attribute is set object. class_dict variable
        # stores field names as keys and id numbers as a value of set:
        class_dict = defaultdict(set)
        # example_dict variable is designed to store unique id numbers of
        # examples:
        example_dict = set()
        # SQL code for selecting the corresponding data of the given word
        # from connection and example_connection tables:
        generic_sql = "SELECT c.field_id, c.field, e.example_id \
                       FROM connection AS c \
                       JOIN Word AS w  ON c.word_id = w.id \
                       LEFT JOIN example_connection AS e ON e.word_id = c.word_id \
                       WHERE w.title = ?;"
        # iterate ove selected rows:
        for row in cur.execute(generic_sql, (word,)):
            # 'row' variable is a tuple object consists of 3 elements; field
            # name as string, id number from relevant field table as integer,
            # and id number from Example table as integer:
            class_dict[row[1]].add(row[0])
            if row[2]:
                example_dict.add(row[2])
        # 'returnable' variable will be the returned variable:
        returnable = {"Fields":defaultdict(set), "Examples":[]}
        # iterate over selected field names:
        for field in class_dict.keys():
            # iterate over id numbers from the relevant field tables:
            for id in class_dict[field]:
                # select the corresponding meaning of the id number from
                # relevant field table:
                cur.execute("SELECT title FROM {} WHERE id = ?;".format(field),\
                            (id,))
                # add it into the variable 'returnable'. Notice the "Fields"
                # key:
                returnable["Fields"][field].add(cur.fetchone()[0])
        # iterate over id numbers of examples:
        for ex_id in example_dict:
            # select corresponding example sentences:
            cur.execute("SELECT title FROM Example WHERE id = ?;", (ex_id,))
            returnable["Examples"].append(cur.fetchone()[0])

        # save the changes
        con.commit()
    except sqlite3.Error:
        raise Exception("Something went wrong when you tried to select data \
from database. Contact the programmer.")
    else:
        return returnable
    finally:
        # close connection
        con.close()

if __name__ == "__main__":
    import sys
    print("The 'functions' module consists of 9 functions:\n1- control\n2- \
timer\n3- create_verification\n4- waiting\n5- header\n6- quitting\n7- \
insert_into\n8- select_from\n\n9- modifier_for_viewing")
    print("List of names in the scope of the 'functions' module:")
    for index, name in enumerate(dir()):
        print(str(index) + "-", name)
