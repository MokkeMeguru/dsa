#include <bits/stdc++.h>
#include <boost/format.hpp>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> ds(N, 0);
  for(auto &item: ds) {
    cin >> item;
  }
  auto s = set<int>(ds.begin(), ds.end());
  cout << s.size()<<endl;

  return 0;
}
