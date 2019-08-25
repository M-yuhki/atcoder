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

const long long MOD = 1000000007;
typedef  long long ll;

int main(void){
  ll n,k;
  cin >> n >> k;
  vector<int> a(n);
  
  REP(i,n){
    cin >> a[i];
  }

  ll c,d;
  c = 0;
  d = 0;
  REP(i,n){
    FOR(j,i+1,n){
      if(a[i] > a[j]){
        c++;
        d++;
      } 
      else if(a[i] < a[j]) d++;
    }
  }
  ll ans = 0;
  ans = c * k % MOD  + ( k * (k-1) / 2 % MOD ) * d;
  ans = ans % MOD;
  cout << ans << endl;
   
} 
