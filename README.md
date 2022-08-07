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
Since the application is not smart, you must be careful when giving orders. There are currently 4 types of  
orders:
- add
  - To insert words and phrases with their meanings
- exadd
  - To insert examples for registered words and phrases
- see
  - To see the meaning(s) and example(s) of a desired word or phrase
  - This will show information only for words and phrases that are already inserted 
- info
  - To open **info.txt** file
  - You can always get detailed help by reading this user manual 
  
### Mechanics of The Application
When you run the program, you'll be in the **main menu** until you type an order described above. Each order  
take you into a special section. These sections are:
- Add Section
- Example Addition Section
- See Section   

**Add Section** and **See Section** run in a loop. When you're in **Add Section** for instance, the program will  
still wait for you to insert another word after inserting word(s). Same goes for **See Section**. You must type  
nothing in order to return **main menu**.  
On the contrary, **Example Addition Section** doesn't run in a loop. You can only add just one example. It returns  
to **main menu** automatically.  
After returning to **main menu**, you can type another or the same order if you want. **main menu** runs in a loop,  
as well. If you want to quit the application, just don't type any defined order in the **main menu**. And don't  
forget farewell, be nice with it :) 
