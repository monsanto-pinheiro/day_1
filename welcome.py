# coding: utf-8

# Execute the program and see what happens.
# Then modify the program so that X is replaced by the day of the week input.
# Hint: see what we did with the name.

message = """
Caro/a {0},

Bem-vindo/a ao iBiMED.
O dia da semana é {1}!

meu nome é {0},

Hasta la vista,
"""

name = input("Como te chamas? ")
week_day = input("Dia da semana? ")

print(message.format(name, week_day))
