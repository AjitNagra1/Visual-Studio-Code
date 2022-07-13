## string concatenation (putting strings together)
# suppose we want to create a string that says "subscribe to ____"
# youtuber = ""  # some string variable

# a few ways to do this
# print("subscribe to "+youtuber)
# print("subscribe to {}".format(youtuber))
# or f string method below, best way:
# print(f"subscribe to {youtuber}")

adj=input("Adjective: ")
verb1=input("Verb: ")
verb2=input("Verb: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2}!"

print(madlib)