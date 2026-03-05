import random
print("Nice to meet you in my game!!")
choise= input("Choose a number. 1, 2, or 3: ")
silly_list=["Bombardiro crocodilo", "banana that eats monkeys", "my math teacher"]
silly_word=random.choice(silly_list)
number=input("input a number ;): ")
number2=input("HUH?? a number again: ")
measure_of_time=input("input a measure of time: ")
transportation=input("now choose a transport: ")
adjective=input("now choose an adjective: ")
adjective2=input("didnt hear you, one more time: ")
adjective3=input("bruh, again: ")
adjective4=input("one more timee: ")
adjective5=input("one laast time: ")
plural=input("type a magical creature, plural: ")
plural2=input("a simple plural that comes to your mind: ")
plural3=input("a plural, again: ")
plural4=input("what did you say?: ")
plural5=input("one last time, a plural: ")
noun=input("Type a random object in front of you: ")
noun2=input("That is boring. choose another object: ")
noun3=input("one more object: ")
noun4=input("an object again: ")
noun5=input("i said again!!!!: ")
verb=input("What are you doing nnow? Choose a verb: ")
verb2=input("another one: ")
color=input("what is the color you dislike the most?: ")
body_part=input("part of a body: ")
body_part2=("part of the body, yes, again!: ")
adj_feeling=input("Type an adjective that describes a feeling: ")
adj_feeling2=input("one more timeeeeeeee: ")
animal=input("name an animal: ")
verbing=input("enter a verb agaaain:" )
verbing+="ing"
adverb=input("input an andverb(ending with 'ly'): ")
place=input("whats your favorite place?: ")
name=input("what is your neighbours name??: ")
p_noun=input("proper noun, pleasee: ")
room=input("type a room in a house: ")23344
if choise=="1":
    print(f"""It was about {number} {measure_of_time} ago when I arrived at the hospital in a {transportation}.
     The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here. 
     There are nurses here who have {color} {body_part}. If someone wants to come into my room I told them that they have to {verb} first. 
     I’ve decorated my room with {number2} {noun2}. Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}.
      I heard that all doctors {verb} {noun4} every day for breakfast. The most {adjective2} thing about being in the hospital is the {silly_word} {noun} !""")
if choise=="2":
    print(f"""This weekend I am going camping with {p_noun} {name}.
        I packed my lantern, sleeping bag, and {noun}. I am so {adj_feeling} to {verb} in a tent.
      I am {adj_feeling2} we might see a(n) {animal}, I hear they’re kind of dangerous.
      While we’re camping, we are going to hike, fish, and {verb2}. 
    I have heard that the {color} lake is great for {verbing}.
    Then we will {adverb} hike through the forest for {number} {measure_of_time}. 
     If I see a {color} {animal} while hiking, I am going to bring it home as a pet!
    At night we will tell {number2} {silly_word }stories and roast {noun2} around the campfire!!""")
else:
    print(f"""Dear {p_noun} {name}, I am writing to you from a {adjective} castle in an enchanted forest.
           I found myself here one day after going for a ride on a {color} {animal} in {place}.
           There are {adjective2} {plural} and {adjective3} {plural2} here! 
          In the {room} there is a pool full of {noun}.
           I fall asleep each night on a {noun2} of {noun3} {plural } and dream of {adjective4} {noun4} {plural5}.
           It feels as though I have lived here for {number} {measure_of_time}. 
          I hope one day you can visit, although the only way to get here now is {verbing} on a {adjective5} {noun5}!! """)
print(f"I am done of generating stories for you, ask {name} next time, not me!!!!!!!")