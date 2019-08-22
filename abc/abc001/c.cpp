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

bool check(x,y,t){
  //その点が条件を満たすかcheck
  bool flg = true;
  int i;
  int j;
  i = x;
  j = y;
  while(true){
    if(t[i][j] == 'Q'){
      flg = false;
      break;
    }
    i++;
    j++;
    if(i == 8 or j == 8) break;
  }
  i = x;
  j = y;
  while(flg){
    if(t[i][j] == 'Q'){
      flg = false;
      break;
    }
    i--;
    j--;
    if(i == 0 or j == 0) break;
  }
  i = x;
  j = y;
  while(flg){
    if(t[i][j] == 'Q'){
      flg = false;
      break;
    }
    i--;
    j++;
    if(i == 0 or j == 8) break;
  }
  i = x;
  j = y;
  while(flg){
    if(t[i][j] == 'Q'){
      flg = false;
      break;
    }
    i++;
    j--;
    if(i == 8 or j == 0) break;
  }

  return flg

}


int main(void){
  vector<vector<char>> t(8, vector<char>(8));
  string s;
  
  vector<int> n;

  REP(i,8){
    cin >> s;
    bool flg = true;
    REP(j,8){
      t[i][j] = s[j];
      if(s[j] == 'Q') flg = false;
    }
    if(flg) n.push_back(i);
  }
  
  int ansi;
  int ansj;
  bool ansflg = false;
  REP(i,5){
    REP(j,5){
      if( check(n[i%5],n[(i+j)%5],t) && check(n[(i+1)%5],n[(i+j+1)%5],t) && check(n[(i+2)%5],n[(i+j+2)%5],t) && check(n[(i+3)%5],n[(i+j+3)%5],t) && check(n[(i+4)%5],n[(i+j+4)%],t)) ansflg = true;
      
      if(ansflg){
        ansj = j;
        break;
      } 
    
    }
    if(ansflg){
      ansi = i;
    }
  
  }

  if(ansflg){
    REP(i,5){
      t[n[(ansi+i)%5]][n[(ansi+ansj+i)%5]] = 'Q';
    }
  
  
  }else{
    
    cout << "No Answer" << endl;
  }


}
