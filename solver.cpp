#include <bits/stdc++.h>
#include <chrono>

using namespace std;

ifstream f;
ofstream g;

int m;
long double auxiliar;
string v[15000], s[15000];

int paternFind(string word, string guess) {
      int freq[26];
      memset(freq, 0, sizeof(freq));
      int cod = 0, n = word.length();

      for(int i = 0;i < n;i++)
            freq[word[i] - 'a'] = 1;

      for(int i = 0;i < n;i++) {
            //green
            if(word[i] == guess[i]) {
                  cod = cod * 3 + 2;
                  continue;
            }
            //yellow
            if(freq[guess[i] - 'a']) {
                  cod = cod * 3 + 1;
                  continue;
            }
            //gray
            cod = cod * 3;
      }
      return cod;
}

string optimalWordFind(int n) {
      int poz;
      string cuvoptim;
      long double maxx = -1;

      for(int i = 1;i <= m;i++) {
            int nrpatern[250];
            memset(nrpatern, 0, sizeof(nrpatern));

            for(int j = 1;j <= n;j++) {
                  int cod = paternFind(v[j], v[i]);
                  ++nrpatern[cod];
            }

            //probabilitatea paternului
            long double entropieCuv = 0;
            for(int j = 0; j < 243; j++){
                  if(nrpatern[j] > 0){
                        long double p = 1.0 * nrpatern[j] / n;
                        entropieCuv += p * log2(1.0 / p);
                  }
            }

            //probabilitatea maxim, cuvant optim
            if(entropieCuv > maxx) {
                  maxx = entropieCuv;
                  auxiliar = maxx;
                  cuvoptim = v[i];
                  poz = i;
            }
      }
      return cuvoptim;
}

int newSet(int n, int pattern, string cuvoptim) {
      int newN = 0;
      for(int j = 1;j <= n;j++) {
            int cod = paternFind(v[j], cuvoptim);
            if(cod == pattern) {
                  swap(v[++newN], v[j]);
            }
      }
      return newN;
}

int main() {
      f.open("cuvinte_wordle.txt");
      while(f >> s[++m]) {
            v[m] = s[m];
      }
      --m;
      f.close();

      int n = m, sum = 0;
      string cuvoptim = "TAREI";
      g.open("communication.txt");
      g << cuvoptim;
      g.close();
      std::this_thread::sleep_for(std::chrono::milliseconds(5000));
      int oldN = n, ct = 1, patern;
      f.open("communication.txt");
      f >> patern; n = newSet(m, patern, cuvoptim);
      f.close();
      while(patern != 242){
            oldN = n, cuvoptim = optimalWordFind(n), ++ct;
            g.open("communication.txt");
            g << cuvoptim;
            g.close();
            std::this_thread::sleep_for(std::chrono::milliseconds(5000));
            f.open("communication.txt");
            f >> patern; n = newSet(n, patern, cuvoptim);
            if(patern == 242) break;
      }
}