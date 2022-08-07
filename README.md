# Introduction to Custom Dictionary Application
This is an application that I designed with **Python** for the activity of learning English vocabulary.   
It mainly has **2 functionalities**:  
- Insertion
  - Word or Phrase
  - Example Text
- Viewing  

You can insert any word or phrase that you want and view it later. This is useful when you have learned  
a new word or phrase because the application reminds you the word that you recently learned when you  
are inserting it.  

Also, you can insert an example sentence or paragraph for any word you inserted. Personally, I learned  
numerous words and phrases from various books, movies, articles, and daily conversations. Hence, saving  
the context was kind of necessary for better learning activity. I believe this functionality of the  
application will help you, as well.


## Before Starting To Use  
First, put all files in the same directory. After that you must initialize the **database_constructor.py** and  
then configure the user name and the name of the database file to be created. If you don't specify any  
user name, the program will assume 'USER_NAME' is your name and if you don't specify a file name, it will  
assume 'default' is the name of the database file to be created. After you specify the necessary names,  
the program creates 2 files:  
- Database File
  - The destination where your words and phrases will be stored with their meanings.
- Text File
  - The place (configuration.txt) where user name and name of the database file will be stored.
  - It is read-only and used by other functions of the application.
  
Now, if you have followed the instructions and have not encountered any problems, you have completed the   
tedious installation activities. You're ready to improve your vocabulary. The application will always be  
with you in your learning journey. Let's start a short tour of how to use the application. Follow me :)  
  
## How To Use  
Run the main program **eng.py**. The program will welcome you first and use fantastic words when addressing  
you. Because you're master of the program. If you want to memorize and save a word, call the app and give  
an order to keep the word registered. It has no right to question you. And you can ask the meaning of the  
already told word and it will give you a detailed explanation. It is not smart but a very dedicated servant.  

### Orders 
Since the application (I'll call it friend from here on out) is not smart, you must be careful when giving  
orders. There are basically 4 types of orders:
- add
- exadd
- see
- info
