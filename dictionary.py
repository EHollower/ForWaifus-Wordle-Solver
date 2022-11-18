#dictionary of strings that will be used in this repository.
f = open("cuvinte_wordle.txt", "r")
wordle_dictionary = []

#read the words on each line and put them into the vector
Lines = f.readlines()
for line in Lines:
      wordle_dictionary.append(line.strip())
