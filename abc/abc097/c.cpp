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
  string s;
  cin >> s;
  int k;
  cin >> k;
  vector<string> ans;
  int len = s.length();
  REP(i,len){
    REP(j,k+1){
      ans.push_back(s.substr(i,j));
    }
  }

  std::sort(ans.begin(), ans.end());
  ans.erase(std::unique(ans.begin(), ans.end()), ans.end());

  cout << ans[k] << endl;

}
