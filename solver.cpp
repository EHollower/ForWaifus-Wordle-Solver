/* The following program is ment to work as a solver for the wordle game

How does it work: -> it communicates with the wordle game troughout communication.txt
                  -> communication.txt is used both as input and output be that a non-standardized coding convention
                  -> the solver awaits a base 3 number such that it can calculate the next optimal word the can be used for the next guess
                  -> once the game.py is closed, solver.exe should close as well

How it calculates the entropy: -> We calculate the entropy of a word by checking it in raport with every other word, we check what patern will be given if we guess
the first word, and the word to be guessed is every other word then we count every patern appearance, then we use the formula: 
S = P(0) / n * log2(n / P(0)) + P(1) / n * log2(n / P(1)) + ...... + P(242) / n log2(n / P(242)), where P(k) is the number of apappearances of every patern
and n is the total number of words, then we guess the optimal word, and check what words give the same patern in raport with our guess and create a smaller set,
then we repet the steps on a the smaller set until we get the word that we had to guess.


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

/*The words have all 5 letters, and every lattern can give us 3 situations when the word is guessed so we can reprezent the given pattern as a base 3 number where 
value 0 means grey, value 1 means yellow and value 2 means green, then we convert it to base 10 and give it a cod, this function returns the cod that guess gives
in raport with word(basically is as if we need to guess "word", and out guess is "guess")*/
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

/*This function checks every possibel guess in raport with the current set of possibel words, then it returns the optimal word*/
std::string optimal_word_find(const std::string wd[], int m, int n) {
      int nrpattern[250];
      std::string woptim;
      long double entropy_max = -1;

      for(int i = 1;i <= m;i++) {
            // m reprezents the total number of words that we can guess
            memset(nrpattern, 0x0, sizeof(nrpattern));
            // reprezents the cardinality of the curret set of possibel words
            for(int j = 1;j <= n;j++)
                  ++nrpattern[pattern_find(wd[j], wd[i])];

            // we calculate the amount of information that it gives
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

/*this function returns the smaller set of possibel words by checking what words from the current set gives us the same pattern as the one that needs to be guess,
when we guess the optimal word*/
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

int main() {
      int m = 0;
      std::string wordle_dictionary[15000];
      read_wordle_dictionary(wordle_dictionary, m);

      int n = m;
      // we will always find that is optimal to start with "TAREI", so we always start with "TAREI"
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
