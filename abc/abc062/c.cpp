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
  ll h;
  ll w;
  cin >> h >> w;
  ll ans;
  if(h % 3 == 0 || w % 3==0){
    ans = 0;
  }
  else{
    ans = h * w + 1;
    ll sx,sy,sz,s;
    ll d,e;
    FOR(i,1,h){
      sx = i*w;
      e = h-i;
      s = e*w;
      sy = e*(w/2);
      sz = s - sy;
      d = max({sx,sy,sz}) - min({sx,sy,sz});
      ans = min(d,ans);
      if(e > 1){
        sy = (e/2)*w;
        sz = s - sy;
        d = max({sx,sy,sz}) - min({sx,sy,sz});
        ans = min(d,ans);
      }
    }

    swap(h,w);
  
    FOR(i,1,h){
      sx = i*w;
      e = h-i;
      s = e*w;
      sy = e*(w/2);
      sz = s - sy;
      d = max({sx,sy,sz}) - min({sx,sy,sz});
      ans = min(d,ans);
      
      if(e > 1){
        sy = (e/2)*w;
        sz = s - sy;
        d = max({sx,sy,sz}) - min({sx,sy,sz});
        ans = min(d,ans);
     
      }
    }
  }

  cout << ans << endl;

}
