#  Mad Libs Story Generator

A fun little Python game where you type in random words and the program builds a silly story with them!
No experience needed to play — just run it and follow the instructions.

-----

##  What is Mad Libs?

Mad Libs is a word game where someone fills in a list of words (a noun, a color, an animal, etc.)
without knowing the story. Then the words get dropped into a template and you get a funny, random story!

This version has 3 different stories to choose from:

- 🏥 A hospital stay
- ⛺ A camping trip
- 🏰 A letter from an enchanted castle

-----

##  What You Need

- Python 3 installed on your computer
- That’s it! No extra libraries or installs needed.

Don’t have Python? Download it free at: https://www.python.org/downloads/

-----

## How to Run the Game

1. Download the file madlibs_beginner.py
1. Open a terminal (or command prompt on Windows)
1. Navigate to the folder where you saved the file:
   
     cd Downloads
   1. Run the file:
   
     python madlibs_beginner.py
   
> On Mac/Linux, you might need to type python3 instead of python

-----

## How to Play

Once the game starts, this is what happens step by step:

Step 1 — Choose a story number:
Pick a story: 1, 2, or 3
> 2

Step 2 — Answer the word prompts. Just type any word that fits!
A name: Sandra
A color: purple
An animal: flamingo
A noun (any object): sock
Another noun: lamp
A verb (action word): dance
An adjective (describing word): crunchy
A number: 7
A place: the moon

Step 3 — Read your silly story:
Me and Sandra went camping near the moon.
We packed a sock and a lamp.
We were so excited to dance in a tent.
At night we saw a purple flamingo and screamed for 7 minutes!

-----

##  Files in This Project
madlibs2.py   ← the game itself, run this!
README.md             ← this file, explaining everything

-----

##  How the Code Works (for beginners)

Here is a quick explanation of what each part of the code does:

1. Importing random
import random

This loads Python’s built-in random module so we can pick a surprise word from a list.

2. Picking a silly word
silly_list = ["Bombardiro crocodilo", "banana that eats monkeys", "my math teacher"]
silly_word = random.choice(silly_list)

Every time you play, one of these three funny phrases gets secretly picked and used in your story.

3. Asking the player to choose a story
choice = input("> ")

input() shows a prompt and waits for the player to type something. Whatever they type gets saved in choice.

4. Validating the choice
while choice != "1" and choice != "2" and choice != "3":
    print("Please type 1, 2, or 3!")
    choice = input("> ")

This while loop keeps asking until the player types a valid option. It won’t let you continue with a wrong answer.

5. Collecting words
name  = input("A name: ")
color = input("A color: ")

Each input() line shows a prompt and saves the player’s answer into a variable.

6. Printing the story
if choice == "1":
    print(f"...story with {noun} and {color}...")
elif choice == "2":
    print(f"...different story...")
else:
    print(f"...third story...")

The if/elif/else block checks which story was chosen and prints the matching one.
The f"..." is called an f-string — it lets you drop variables directly into text using {variable_name}.

-----
