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
  string s,t;
  cin >> s;
  cin >> t;
  int p = 0;
  int b;
  b = s.length();
  int c;
  c = 0;
  bool flg;
  flg = false;
  REP(i,t.length()){
    
    while (true){
     if( (t[i] == s[p]) == 1){
        b = p;
        p += 1;
        if(p == s.length()){
          c += 1;
          p = 0;
        }
        break;
      }
      else if(b == p){
        flg = true;
        break;
      }
    
      p += 1;
      if(p == s.length()){
      
        p = 0;
        c += 1;
      }

    }

    if(flg) break;

  }

  if(flg) cout << -1 << endl;
  else cout << c*s.length() + p << endl;

}
