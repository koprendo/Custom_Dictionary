import sqlite3
from constants import *
from functions import *

def example_add():
    # call function "header" from functions module to print the section name
    # in a fancy way:
    header("EXAMPLE ADDITION SECTION")
    # call function "waiting" from functions module:
    waiting("Type the Word", F2)
    # get a word to be referenced from the user:
    word = input(">").strip(ignore_these).lower()
    # call function 'waiting' before requesting example:
    waiting("Type the Example Text", F2)
    # get an example sentence for the given word from the user:
    example = input(">").strip()
    # execute if block only if both 'word' and 'example' variable have at least
    # one character:
    if word and example:
        try:
            # create a connection object that represents the database:
            con = sqlite3.connect(file_name)
            # create a cursor object by using the cursor() method of connection
    		# instance:
            cur = con.cursor()
            # select the id number of the given word from database:
            cur.execute("SELECT id FROM Word WHERE title = (?);", (word, ))
            fetched = cur.fetchone()
            # execute if block only if there is not such word in the database
            # and raise 'NoWord' exception from constants module:
            if not fetched:
                raise NoWord
            # assign selected id number of the given word:
            word_id = fetched[0]
            # insert the given example text:
            cur.execute("INSERT OR IGNORE INTO Example (title) VALUES (?);", \
(example, ))
            # select id number of the inserted or already inserted example text:
            cur.execute("SELECT id FROM Example WHERE title = (?);", \
(example, ))
            # insert necessary data into the table 'example_connection':
            cur.execute("INSERT OR IGNORE INTO example_connection (example_id, \
                         word_id) VALUES (?, ?);", (cur.fetchone()[0], word_id))
            # save the changes
            con.commit()
        except sqlite3.Error:
            raise Exception("Something went wrong in the example insertion \
process. Contact the programmer.\n")
        except NoWord:
            waiting("\nThere is no such word ('{}') in the database\
.\n".format(word), F3)
            quitting("example addition")
        else:
            waiting("\nInserting example for '" + word + "' has successfully \
completed.\n", F3)
        finally:
            # close connection
            con.close()
    else:
        waiting("\nSorry... You should specify at least one character \
when you are typing a word and an example.", F3)
        quitting("example addition")
