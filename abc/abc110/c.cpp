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
  std::string s;
  std::string t;
  cin >> s;
  cin >> t;
  bool flg;
  flg = true;
  int stot[26];
  int ttos[26];
  REP(i,26){
     stot[i] = -1;
     ttos[i] = -1;
  }
  REP(i,s.length()){
    int x,y;
    x = (unsigned char)s[i] - 97;
    y = (unsigned char)t[i] - 97;
    if(stot[x] < 0){
      stot[x] = y;
    }
    else if(stot[x] != y){
      flg = false;
    }

    if(ttos[y] < 0){
      ttos[y] = x;
    }
    else if(ttos[y] != x){
      flg = false;
    }

  }
  if(flg) cout << "Yes" << endl;
  else cout << "No" << endl;

}
