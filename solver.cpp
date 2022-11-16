/* The following program is ment to work as a solver for the wordle game

How does it work: -> it communicates with the wordle game troughout communication.txt
                  -> communication.txt is used both as input and output be that a non-standardized coding convention
                  -> the solver awaits a base 3 number such that it can calculate the next optimal word the can be used for the next guess
                  -> once the game.py is closed, solver.exe should close as well

How it calculates the entropy: -> Ricardo scrie de aici in engleza pls


Questions:
Why did we write the documation/code/comments in english? -> because we felt like it
Why did we write the solver in cpp? -> well because of the efficiency that it offers and familiarity with the language

*/

//libraries that we need for the solver
#include <fstream>
#include <string.h>
#include <math.h>

int get_pattern() {
      std::ifstream f;
      std::string DataDump;
      while(true) {
            f.open("communication.txt");
            f >> DataDump;
            f.close();
      
            if(DataDump == "---") {
                  exit(0);
            }

            if(DataDump.length() <= 3) {
                  return stoi(DataDump);
            }
      }
      return -1;
}

void push_wordle(std::string woptim) {
      std::ofstream g;
      g.open("communication.txt");

      g << woptim;
      g.close();
}

void read_wordle_dictionary(std::string wordle_dictionary[], int& n) {
      std::ifstream f;
      f.open("cuvinte_wordle.txt");
      
      while(f >> wordle_dictionary[++n]);
      --n;
      f.close();
}

int pattern_find(std::string word, std::string guess) {
      int freq[26];
      memset(freq, 0, sizeof(freq));

      int code = 0, n = word.length();
      for(int i = 0;i < n;i++)
            freq[word[i] - 'A'] = 1;

      for(int i = 0;i < n;i++) {
            //green
            if(word[i] == guess[i]) {
                  code = code * 3 + 2;
                  continue;
            }
            //yellow
            if(freq[guess[i] - 'A']) {
                  code = code * 3 + 1;
                  continue;
            }
            //gray
            code = code * 3;
      }

      return code;
}

std::string optimal_word_find(std::string wd[], long double& aux, int m, int n) {
      std::string woptim;
      long double entropy_max = -1;

      for(int i = 1;i <= m;i++) {
            int nrpattern[250];
            memset(nrpattern, 0, sizeof(nrpattern));

            for(int j = 1;j <= n;j++) {
                  int cod = pattern_find(wd[j], wd[i]);
                  ++nrpattern[cod];
            }

            long double entropy_word = 0;
            for(int j = 0; j < 243; j++){
                  if(nrpattern[j] > 0) {
                        long double p = 1.0 * nrpattern[j] / n;
                        entropy_word += p * log2(1.0 / p);
                  }
            }

            if(entropy_word > entropy_max) {
                  entropy_max = entropy_word;
                  aux = entropy_max;
                  woptim = wd[i];
            }
      }

      return woptim;
}

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
      std::string woptim = "TAREI";
      push_wordle(woptim);

      int oldN = n, pattern;
      pattern = get_pattern();
      n = newSet(m, pattern, wordle_dictionary, woptim);

      while(n != 0) {
            long double aux;
            oldN = n, woptim = optimal_word_find(wordle_dictionary, aux, m, n);
            push_wordle(woptim);

            pattern = get_pattern();
            n = newSet(n, pattern, wordle_dictionary, woptim);
            if(pattern == 242) {
                  break;
            }
      }
      return 0;
}