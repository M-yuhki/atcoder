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
  cin >> a;
  int ma = 0;
  FOR(i,1,a) ma = max( ma, i * (a - i));
  cout << ma << endl;


}

