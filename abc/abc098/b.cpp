#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
using namespace std;
int main(void){
  int n;
  cin >> n;
  string s;
  cin >> s;
  
  int ans = 0;

  int p;
  string l;
  string r;
  REP(i,n){
    p = 0;
    for(char c='a';c<='z';c++){
        l = s.substr(0,i);
        r = s.substr(i);
        if( count(l.cbegin(), l.cend(), c) > 0 && count(r.cbegin(), r.cend(), c) > 0){
            p++;
          }
      }
    ans = max(p,ans);
    
    }
  cout << ans << endl;

}
