#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < int(n); i++)
using namespace std;

bool all_search(vector<int> &A, int m, int idx) {
  if (int(A.size()) == idx or m < 0)
    return m == 0;
  return all_search(A, m - A.at(idx), idx+ 1) || all_search(A, m, idx + 1);
}

int main() {
  int n;
  vector<int> A;
  int temp;
  cin >> n;
  rep(_, n){
    cin >> temp;
    A.push_back(temp);
  }
  int q;
  vector<int> M;
  cin >> q;
  rep(_, q) {
    cin >> temp;
    M.push_back(temp);
  }
  for(auto &item: M) {
    if (all_search(A, item, 0))
      cout << "yes" << endl;
    else
      cout << "no" << endl;

  }
}
