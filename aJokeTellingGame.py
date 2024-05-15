# A Joke Telling Game
# The premise behind this game is to showcase different ways to use strings within print functions
# This is from Invent Your Own Computer Games with Python by Al Sweigart

print('What do you get when you cross a snowman with a Vampire?')
# input is there to give player time to read the joke before the punchline appears.
input()
print('Frostbite!')
print()
# The backslash tells you that the letter right after it is an escape character.
# An escape character lets you print special characters that are difficult or impossible to enter into the source code.
# such as the single quote in a string value that begins and ends with single quotes.
print('What do dentists call an astronaut\'s cavity?')
input()
print('A black hole!')
print()
print('Knock Knock')
input()
print('Who\'s there?')
input()
print('Interrupting cow.')
input()
# Normally, print() adds a newline character to the end of the string it prints.
# A blank print() function will just print a newline.
# print() can optionally have a second parameter: end.
# An argument is the value passed in a function call.
# The blank string passed to print() is called a keyword argument.
# The end in end='' is called a keyword parameter.
print('Interrupting cow wh', end='')
print('-MOO')