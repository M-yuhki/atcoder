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
  int a;
  int b;
  cin >> a >> b;
  
  int d;
  d = abs(a - b);
  vector<int> v = {0,1,2,3,2,1,2,3,3,2};
  cout << d/10 + v[d%10] << endl;


}
