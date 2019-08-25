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
typedef  unsigned long long ull;
typedef  long long ll;

int main(void){
  int x;
  int y;
  cin >> x >> y;
  vector<int> s = {1,3,5,7,8,10,12};
  vector<int> t = {4,6,9,11};

  bool sx,sy,tx,ty;
  sx = false;
  sy = false;
  tx = false;
  ty = false;
  REP(i,7){
    if(x == s[i]) sx = true; 
    if(y == s[i]) sy = true; 
    if(i <= 3){
    
      if(x == t[i]) tx = true; 
      if(y == t[i]) ty = true; 
    
    }

  }
  if( (sx && sy) || (tx && ty)) cout << "Yes" << endl;
  else cout << "No" << endl;


}
