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

int calc(int p,vector<vector<int> >s){
  int x;
  int size;
  size = s[p].size();
  if(size == 0) x = 1;
  else if(size == 1) x = calc(s[p][0],s)* 2 + 1;
  else{
    int mi = 100000000;
    int ma = -1;
    REP(i,size){
      int y;
      y = calc(s[p][i],s);
      mi = min(y,mi);
      ma = max(y,ma);
    }
    x = mi + ma + 1; 
  }
  return x;
}



int main(void){
  
  int n;
  cin >> n;
  vector<vector<int>> s (n+1,vector<int> () );

  REP(i,n-1){
    int b;
    cin >> b;
    s[b].push_back(i+2);
  }

  cout << calc(1,s) << endl;

   
} 
