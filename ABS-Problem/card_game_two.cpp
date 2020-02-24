#include <bits/stdc++.h>
#include <boost/format.hpp>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> as(N, 0);
  for(auto &item: as) {
    cin >> item;
  }
  sort(as.begin(), as.end());
  auto plus= true;
  auto res = 0;
  for(auto &item: as) {
    if(plus){
      plus = false;
      res += item;
    } else {
      plus= true;
      res -= item;
    }
  }
  cout << abs(res) << endl;
  return 0;
}
