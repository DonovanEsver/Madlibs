# string concatenation (aka hwo to put strings together)
# suppose we ant to create a string that says "subscribe to _____"
# youtuber = "Li Gima" # some string variable

# a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Help me! I have been kidnapped by a very {adj} man! Im so scared plz call for help \
I dont want to die while {verb1} and {verb2} like {famous_person} did!"

print(madlib)