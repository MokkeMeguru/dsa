#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < int(n); i++)
#define SENTINEL INT_MAX
using namespace std;

void solve(int H, int W) {
  vector<string> table;
  set<pair<int, int>> prevs;
  string temp;
  rep(i, H){
    cin >> temp;
    table.push_back(temp);
  }
  auto x = 0;
  auto y = 0;
  while(table[y][x] != '.') {
    if (prevs.count(make_pair(x, y))) {
      cout << "LOOP" <<endl;
      return;
    } else {
      prevs.insert(make_pair(x, y));
    }
    if (table[y][x] == '>') {
      ++x;
    } else if (table[y][x] == 'v') {
      ++y;
    } else if (table[y][x] == '^') {
      --y;
    } else if (table[y][x] == '<') {
      --x;
    }
  }
  cout << x << " " << y << endl;
  return;
}

int main() {
  int H, W;
  while(true) {
    cin >> H >> W;
    if (H == 0 && W == 0) {
      break;
    } else {
      solve(H, W);
    }
  }

}
