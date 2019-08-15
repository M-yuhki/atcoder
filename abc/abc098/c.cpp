#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <algorithm>
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define ARRAY_LEN(ARR) (sizeof(ARR) / sizeof((ARR)[0]))
using namespace std;
int main(void){
  int n;
  cin >> n;
  string s;
  cin >> s;
  int ans = n + 1;
  int p;
  std::vector<int> w {0};
  std::vector<int> e {0};
  REP(i,n){
    if(s[i] == 'W'){
      w.push_back(w[i] + 1);
      e.push_back(e[i]);
    }else{
      w.push_back(w[i]);
      e.push_back(e[i] + 1);
    }
  
  }
  w.push_back(w[n]);
  e.push_back(e[n]);

  FOR(i,1,n+1){
    p = w[i-1] + e[n+1] - e[i];
    ans = min(ans,p);
  }

  cout << ans << endl;

}
