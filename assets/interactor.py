from assets.colors import *

def clear_data():
      open("communication.txt", "w").close()


def get_word():
      f = open("communication.txt", "r")
      guess = f.read()
      f.close()
      return guess

def push_code(code):
      g = open("communication.txt", "w")
      g.write(str(code))
      g.close()

def push_exit():
      g = open("communication.txt", "w")
      g.write('---')
      g.close()

def outcome(wordle, guess):
      freq = [0 for i in range(27)]
      n, code = len(wordle), 0
      for i in range(n):
            freq[ord(wordle[i]) - ord('A')] += 1

      for i in range(n):
            if guess[i] == wordle[i]:
                  colorTemp[i] = colors_arr[2]
                  code = code * 3 + 2
                  continue
            if freq[ord(guess[i]) - ord('A')] >= 1:
                  colorTemp[i] = colors_arr[3]
                  code = code * 3 + 1
                  continue
            colorTemp[i] = colors_arr[5]
            code = code * 3

      push_code(code)
      return False if colorTemp.count(colors_arr[2]) == n else True