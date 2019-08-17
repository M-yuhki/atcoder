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
  int n,m,x,y;
  cin >> n >> m >> x >> y;
  vector<int> xx;
  vector<int> yy;
  REP(i,n){
    int a;
    cin >> a;
    xx.push_back(a);
  }

  REP(i,m){
    int b;
    cin >> b;
    yy.push_back(b);
  }


  int xmax = *std::max_element(xx.begin(), xx.end());
  int ymin = *std::min_element(yy.begin(), yy.end());

  if(max(x,xmax) < min(y,ymin)){
    cout << "No War" << endl;
  }else{
    cout << "War" << endl;
  }

}
