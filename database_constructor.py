# always run this source file once as the main program

def main(file_name="default", u_name="USER_NAME"):
	'''main function creates a database and executes SQL commands using SQLite \
syntax and saves values of the variables 'file_name' and 'u_name' into a \
read-only text file.
	'''

	# try-except block in case of any database connection error:
	try:
		# create a connection object that represents the database:
		con = sqlite3.connect(file_name + ".db")
		# create a cursor object by using the cursor() method of connection
		# instance:
		cur = con.cursor()
		# executescript for execution of multiple SQL statements at once:
		cur.executescript('''
			DROP TABLE IF EXISTS Adjective;
			DROP TABLE IF EXISTS Adverb;
			DROP TABLE IF EXISTS Conjunction;
			DROP TABLE IF EXISTS Determiner;
			DROP TABLE IF EXISTS Example;
			DROP TABLE IF EXISTS Noun;
			DROP TABLE IF EXISTS Phrase;
			DROP TABLE IF EXISTS Preposition;
			DROP TABLE IF EXISTS Pronoun;
			DROP TABLE IF EXISTS Verb;
			DROP TABLE IF EXISTS Word;
			DROP TABLE IF EXISTS connection;
			DROP TABLE IF EXISTS example_connection;

			CREATE TABLE "Adjective" (
				"id"	INTEGER NOT NULL,
				"title"	TEXT NOT NULL UNIQUE,
				PRIMARY KEY("id")
			);

			CREATE TABLE "Adverb" (
				"id"	INTEGER NOT NULL,
				"title"	TEXT NOT NULL UNIQUE,
				PRIMARY KEY("id")
			);

			CREATE TABLE "Conjunction" (
				"id"	INTEGER NOT NULL,
				"title"	TEXT NOT NULL UNIQUE,
				PRIMARY KEY("id")
			);

			CREATE TABLE "Determiner" (
				"id"	INTEGER NOT NULL,
				"title"	TEXT NOT NULL UNIQUE,
				PRIMARY KEY("id")
			);

			CREATE TABLE "Example" (
				"id"	INTEGER NOT NULL,
				"title"	TEXT NOT NULL UNIQUE,
				PRIMARY KEY("id")
			);

			CREATE TABLE "Noun" (
				"id"	INTEGER NOT NULL,
				"title"	TEXT NOT NULL UNIQUE,
				PRIMARY KEY("id")
			);

			CREATE TABLE "Phrase" (
				"id"	INTEGER NOT NULL,
				"title"	TEXT NOT NULL UNIQUE,
				PRIMARY KEY("id")
			);

			CREATE TABLE "Preposition" (
				"id"	INTEGER NOT NULL,
				"title"	TEXT NOT NULL UNIQUE,
				PRIMARY KEY("id")
			);

			CREATE TABLE "Pronoun" (
				"id"	INTEGER NOT NULL,
				"title"	TEXT NOT NULL UNIQUE,
				PRIMARY KEY("id")
			);

			CREATE TABLE "Verb" (
				"id"	INTEGER NOT NULL,
				"title"	TEXT NOT NULL UNIQUE,
				PRIMARY KEY("id")
			);

			CREATE TABLE "Word" (
				"id"	INTEGER NOT NULL,
				"title"	TEXT NOT NULL UNIQUE,
				PRIMARY KEY("id")
			);

			CREATE TABLE "connection" (
				"word_id"	INTEGER NOT NULL,
				"field_id"	INTEGER NOT NULL,
				"field"	TEXT NOT NULL,
				PRIMARY KEY("word_id","field_id","field")
			);

			CREATE TABLE "example_connection" (
				"example_id"	INTEGER NOT NULL,
				"word_id"	INTEGER NOT NULL,
				PRIMARY KEY("example_id","word_id")
			);

		''')
		# save the changes
		con.commit()

	# sqlite3.Error is a base class of the other exceptions in this module.
	# Therefore, it catches all sqlite3 related errors:
	except sqlite3.Error:
		print("Error: Something went wrong. Consult the programmer. Contact \
information can be found in info.txt file.")

	finally:
		# close connection
		con.close()

	# use open() built-in function in order to return a file object, the with
	# block ensures the file will be automatically closed:
	with open("configuration.txt", mode="w") as config_file:
		# write user name and database name to configuration file for later
		# uses.
		config_file.write("User_Name: {0}\nDatabase_Name: {1}.db\n".format(u_name,
		 file_name))

	# this makes configuration.txt file read-only:
	os.chmod("configuration.txt", S_IREAD)


if __name__ == "__main__":
	import sqlite3
	import os
	from stat import S_IREAD

	f_name = input("\n**WELCOME TO DATABASE CONSTRUCTOR**\nWhat would you like \
your database file name to be, please type\n>")
	user = input("\nType your name:\n>")

	# check if the variables 'f_name' and 'user' are entered by the user and
	# run main() with default values if the user has not entered any values.
	if f_name == '' and user == '':
		main()
	elif f_name == '':
		main(u_name=user)
	elif user == '':
		main(file_name=f_name)
	else:
		main(f_name, user)

	print("\nMISSION COMPLETED!")
