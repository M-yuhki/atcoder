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
  double ans;
  int n;
  cin >> n;
  vector<int> r(n);

  REP(i,n) cin >> r[i];

  sort(r.begin(),r.end());

  int t;

  REP(i,n){
    if(i % 2 == 0) t += r[n-1-i] * r[n-1-i];
    else t -= r[n-1-i]* r[n-1-i];
  }

  ans = t * 3.14159265358979323846264;
  printf("%.10lf\n", ans);
}
