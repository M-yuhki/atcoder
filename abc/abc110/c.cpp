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
    int sp,tp;
    sp = (unsigned char)s[i] - 97;
    tp = (unsigned char)t[i] - 97;
    cout << sp << ":" << tp << endl;    
    if(stot[sp] < 0 and ttos[sp] < 0){
      stot[sp] = tp;
      ttos[tp] = sp;
    }
    else if(stot[sp] != tp || ttos[tp] != sp){
      flg = false;
      break;
    }


  }
  if(flg) cout << "Yes" << endl;
  else cout << "No" << endl;

}
