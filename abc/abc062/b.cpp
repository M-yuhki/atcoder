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
  int h,w;
  cin >> h >> w;
  string e;
  e = string(w+2,"#");

  cout << e << endl;
  REP(i,h){ 
    string f;
    cin >> f;
    cout << "#" <<f << "#" << endl; 
  }
  cout << e << endl;

}
