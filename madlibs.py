import random

silly_list = ["Bombardiro crocodilo", "banana that eats monkeys", "my math teacher"]
silly_word = random.choice(silly_list)

print("Welcome to Mad Libs!!")


def ask(prompt):
    while True:
        answer = input(prompt).strip()
        if answer:
            return answer
        print("Please type something!")


while True:
    choice = input("Pick a story: 1, 2, or 3: ").strip()
    if choice in ("1", "2", "3"):
        break
    print("Please enter 1, 2, or 3!")


name            = ask("A neighbour's name: ")
p_noun          = ask("A proper noun (like a title, e.g. Dr): ")
number          = ask("A number: ")
number2         = ask("Another number: ")
measure_of_time = ask("A measure of time (e.g. days): ")
adjective       = ask("An adjective: ")
adjective2      = ask("Another adjective: ")
adjective3      = ask("One more adjective: ")
adjective4      = ask("Yet another adjective: ")
adjective5      = ask("Last adjective: ")
noun            = ask("A noun: ")
noun2           = ask("Another noun: ")
noun3           = ask("One more noun: ")
noun4           = ask("Yet another noun: ")
noun5           = ask("Last noun: ")
verb            = ask("A verb: ")
verb2           = ask("Another verb: ")
verbing         = ask("A verb (will become -ing): ") + "ing"
adverb          = ask("An adverb (ending in -ly): ")
color           = ask("A color: ")
animal          = ask("An animal: ")
body_part       = ask("A body part: ")
body_part2      = ask("Another body part: ")
plural          = ask("A plural noun (magical creatures): ")
plural2         = ask("Another plural noun: ")
plural5         = ask("One more plural noun: ")
adj_feeling     = ask("An adjective describing a feeling: ")
adj_feeling2    = ask("Another feeling adjective: ")
transportation  = ask("A mode of transport: ")
place           = ask("Your favorite place: ")
room            = ask("A room in a house: ")


if choice == "1":
    print(f"""
It was about {number} {measure_of_time} ago when I arrived at the hospital in a {transportation}.
The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here.
The nurses have {color} {body_part}. To enter my room you have to {verb} first.
I've decorated it with {number2} {noun2}. The doctor was wearing a {noun3} on their {body_part2}.
All doctors eat {noun4} every day for breakfast. The most {adjective2} thing here is the {silly_word} {noun}!
""")

elif choice == "2":
    print(f"""
This weekend I am going camping with {p_noun} {name}.
I packed my lantern, sleeping bag, and {noun}. I am so {adj_feeling} to {verb} in a tent.
I am {adj_feeling2} we might see a(n) {animal} — I hear they're dangerous.
We are going to hike, fish, and {verb2}. The {color} lake is great for {verbing}.
We will {adverb} hike through the forest for {number} {measure_of_time}.
If I see a {color} {animal}, I'm bringing it home as a pet!
At night we'll tell {number2} {silly_word} stories and roast {noun2} around the campfire!!
""")

else:
    print(f"""
Dear {p_noun} {name}, I am writing from a {adjective} castle in an enchanted forest.
I got here after riding a {color} {animal} in {place}.
There are {adjective2} {plural} and {adjective3} {plural2} here!
In the {room} there is a pool full of {noun}.
I sleep on a {noun2} of {noun3} {plural} and dream of {adjective4} {noun4} {plural5}.
It feels like I've been here for {number} {measure_of_time}.
The only way to visit is by {verbing} on a {adjective5} {noun5}!!
""")

print(f"Done! Ask {name} next time, not me!!!!")
