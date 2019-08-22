#include <bits/stdc++.h>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>
#include <regex>
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define ARRAY_LEN(ARR) (sizeof(ARR) / sizeof((ARR)[0]))
using namespace std;


int main(void){
  int n;
  string s;
  cin >> n;
  cin >> s;
  
  int mi = n+1;
  int ma = -1;

  vector<char> w = {'1','2','3','4'};

  int c;
  REP(i,4){
    c = 0;
    REP(j,n){
      if(s[j] == w[i]) c++;
    
    }
    mi = min(mi,c);
    ma = max(ma,c);
  
  }
  cout << ma << " " << mi << endl;

}
