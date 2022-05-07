#By VeloxExcidium
'''This script backspaces by one word from where the cursor is. This script must be run in the Pythonista keyboard.'''

import keyboard
import re

context = keyboard.get_input_context()[0]
com = re.compile(r'(\S+)')
contextsplit = com.split(str(context))
wordcount = len(contextsplit)-1
keyboard.backspace((len(contextsplit[wordcount])))
context1 = keyboard.get_input_context()[0]
contextsplit1 = context1.split()
wordcount1 = len(contextsplit1)-1
keyboard.backspace((len(contextsplit1[wordcount1])))
