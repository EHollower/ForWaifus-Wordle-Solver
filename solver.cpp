/* The following program is ment to work as a solver for the wordle game

How does it work: -> it communicates with the wordle game troughout communication.txt
                  -> communication.txt is used both as input and output be that a non-standardized coding convention
                  -> the solver awaits a base 3 number such that it can calculate the next optimal word the can be used for the next guess
                  -> once the game.py is closed, solver.exe should close as well

How it calculates the entropy: -> Ricardo scrie de aici in engleza pls


Why did we write the solver in cpp? -> well because of the efficiency that it offers and familiarity with the language
*/

//libraries that we need for the solver
#include <fstream>
#include <string.h>
#include <math.h>
#include <iostream>

//pragma opitimization to imporve the performance a bit (hopefully :_())
#pragma GCC optimize("Ofast,unroll-loops")

//this function will continueously read 
// from communication.txt untill game.py provides a base 3 number or a "termination string"
int get_pattern() {
      std::ifstream f;
      std::string DataDump;
      //read till smth. happens
      while(true) {
            f.open("communication.txt");
            f >> DataDump;
            f.close();

            //if from communication.txt we recive "---" then we know that we should stop here because game.py was stoped
            if(DataDump == "---") {
                  exit(0);
            }

            //since we know what type of date we send and recive from communication.txt we will know that
            //when we recive an input with length less than or equal to 3 that we have an input from game.py
            if(DataDump.length() <= 3) {
                  return stoi(DataDump);
            }
      }
      //the functions should never reach this point, its use is just to avoid the warning from the compiler
      return -1;
}

//push the optimal word to game.py after calculating the optimal guess
//used to clear up the code a bit
void push_wordle(std::string woptim) {
      std::ofstream g;
      g.open("communication.txt");

      g << woptim;
      g.close();
}

//reads all the words that will be allowed in game.py
//used to clear up the code a bit
void read_wordle_dictionary(std::string wordle_dictionary[], int& n) {
      std::ifstream f;
      f.open("cuvinte_wordle.txt");
      
      while(f >> wordle_dictionary[++n]);
      --n;
      f.close();
}

//Ricardo scrie aici ce face functia mai in detaliu in engleza, pls
//poti pune commenturi si prin program
int pattern_find(std::string word, std::string guess) {
      int code = 0, n = word.length();
      for(int i = 0;i < n;i++) {
            //green
            if(word[i] == guess[i]) {
                  code = code * 3 + 2;
                  continue;
            }
            //yellow
            if(word.find(guess[i]) != std::string::npos) {
                  code = code * 3 + 1;
                  continue;
            }
            //gray
            code = code * 3;
      }

      return code;
}

//Ricardo scrie aici ce face functia mai in detaliu in engleza, pls
//poti pune commenturi si prin program
std::string optimal_word_find(const std::string wd[], int m, int n) {
      int nrpattern[250];
      std::string woptim;
      long double entropy_max = -1;

      for(int i = 1;i <= m;i++) {
            memset(nrpattern, 0x0, sizeof(nrpattern));

            for(int j = 1;j <= n;j++)
                  ++nrpattern[pattern_find(wd[j], wd[i])];

            long double entropy_word = 0, p;
            for(int j = 0; j < 243; j++){
                  if(nrpattern[j]) {
                        p = 1.0 * nrpattern[j] / n;
                        entropy_word += p * -log2(p);
                  }
            }

            if(entropy_word > entropy_max) {
                  entropy_max = entropy_word;
                  woptim = wd[i];
            }
      }

      return woptim;
}

//Ricardo scrie aici ce face functia mai in detaliu in engleza, pls
//poti pune commenturi si prin program
int newSet(int n, int pattern, std::string wd[], std::string woptim) {
      int newN = 0;
      for(int j = 1;j <= n;j++) {
            int cod = pattern_find(wd[j], woptim);
            if(cod == pattern) {
                  std::swap(wd[++newN], wd[j]);
            }
      }
      return newN;
}

//Poti sa scrii si pe aici ceva in cazu in care e nevoie
int main() {
      int m = 0;
      std::string wordle_dictionary[15000];
      read_wordle_dictionary(wordle_dictionary, m);

      int n = m;
      std::string woptim = "TAREI";
      push_wordle(woptim);

      int pattern;
      pattern = get_pattern();
      n = newSet(m, pattern, wordle_dictionary, woptim);

      while(n != 0) {
            woptim = optimal_word_find(wordle_dictionary, m, n);
            push_wordle(woptim);

            pattern = get_pattern();
            n = newSet(n, pattern, wordle_dictionary, woptim);
            if(pattern == 242) {
                  break;
            }
      }

      return 0;
}