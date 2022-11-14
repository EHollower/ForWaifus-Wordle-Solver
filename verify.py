import subprocess
import os
from dictionary import wordle_dictionary

for wordle in wordle_dictionary:
      os.system("py game.py " + wordle)