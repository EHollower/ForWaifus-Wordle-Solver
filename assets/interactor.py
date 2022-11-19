from assets.colors import *

#create a new file
def clear_data():
      open("communication.txt", "w").close()


#get guess form the solver
def get_word():
      f = open("communication.txt", "r")
      guess = f.read()
      f.close()
      return guess

#push base 3 code to the solver
def push_code(code):
      g = open("communication.txt", "w")
      g.write(str(code))
      g.close()

#tell the solver to "shut down" the process has ended
def push_exit():
      g = open("communication.txt", "w")
      g.write('---')
      g.close()

#generate an output to communicate with the solver
def outcome(wordle, guess):
      freq = [0 for i in range(27)]
      n, code = len(wordle), 0
      for i in range(n):
            freq[ord(wordle[i]) - ord('A')] += 1

      for i in range(n):
            #if two letters are on the same position
            if guess[i] == wordle[i]:
                  colorTemp[i] = colors_arr[2]
                  code = code * 3 + 2
                  continue

            #if it is in the word
            if freq[ord(guess[i]) - ord('A')] >= 1:
                  colorTemp[i] = colors_arr[3]
                  code = code * 3 + 1
                  continue

            #if it isnt't in the word
            colorTemp[i] = colors_arr[5]
            code = code * 3

      push_code(code)

      #if we guessed corectly shut down the solver and diplay total number of guesses
      return False if colorTemp.count(colors_arr[2]) == n else True