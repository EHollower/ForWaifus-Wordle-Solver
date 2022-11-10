#include <bits/stdc++.h>
using namespace std;
string v[15000], s[15000];
int m;
long double auxiliar;
int paternFind(string word, string guess)
{
    int cod = 0, fr[26];
    memset(fr, 0 , sizeof(fr));
    for(int i = 0; i < 5; i++){
        fr[word[i] - 65] = 1;
    }
    for(int i = 0; i < 5; i++){
        if(word[i] == guess[i]){
            cod = cod * 3 + 2; // green
        }
        else if(fr[guess[i] - 65] != 0){
            cod = cod * 3 + 1; //yellow
        }
        else{
            cod = cod * 3; // grey
        }
    }
    return cod;
}
string optimalWordFind(int n)
{
    long double maxx = -1;
    int poz;
    string cuvoptim;
    for(int i = 1; i <= m; i++){
        int nrpatern[250];
        memset(nrpatern, 0, sizeof(nrpatern));
        for(int j = 1; j <= n; j++){
            int cod = paternFind(v[j], v[i]);
            nrpatern[cod]++;
        }
        long double entropieCuv = 0;
        for(int j = 0; j < 243; j++){
            if(nrpatern[j] > 0){
                long double p = 1.0 * nrpatern[j] / n, aux = 1; //probabilitatea paternului
                entropieCuv += p * log2(aux / p);
            }
        }
        if(entropieCuv > maxx){
            maxx = entropieCuv;
            auxiliar = maxx;
            cuvoptim = v[i];
            poz = i;
        }
    }

    return cuvoptim;
}
int newSet(int patern, int n, string cuvoptim)
{
    int newN;
    for(int j = 1; j <= n; j++){
        int cod = paternFind(v[j], cuvoptim);
        if(cod == patern){
            ++newN;
            swap(v[newN], v[j]);
        }
    }
    return newN;
}
int main()
{
    ifstream f("wordle.in");
    ofstream g("wordle.out");
    int i = 1, j, k;
    while(f >> s[i]){
        v[i] = s[i];
        i++;
    }
    m = i - 1;
    int n = i - 1, sum;
    for(i = 1; i <= 100; i++){
        string word = s[i], cuvoptim = "TAREI";
        for(j = 1; j <= m; j++)
            v[j] = s[j];
        int oldN = n, patern = paternFind(word, cuvoptim), n = newSet(patern, m, cuvoptim), ct = 1;
        g << word << " " << cuvoptim << " ";// << 6.41381 << " " << log2(1.0 * oldN / n) << "\n";
        while(patern != 242){
            oldN = n;
            cuvoptim = optimalWordFind(n);
            ct++;
            patern = paternFind(word, cuvoptim);
            n = newSet(patern, n, cuvoptim);
            g << cuvoptim << " ";// << auxiliar << " " << log2(1.0 * oldN / n) << "\n";
            if(patern == 242) break;
        }
        sum += ct;
        g << ct << "\n";
    }
    cout << 1.0 * sum / m;
    return 0;
}
