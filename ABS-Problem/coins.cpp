#include <bits/stdc++.h>
#include <boost/format.hpp>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
map<string, int> m{{"A", 10}, {"B", 2}, {"C", 1}};

int main() {
  int A, B, C, X;
  cin >> A;
  cin >> B;
  cin >> C;
  cin >> X;
  X = X / 50;
  auto c = 0;
  vector<int> As(A + 1, 0);
  rep(i, A + 1) { As[i] = m.at("A") * i; }
  vector<int> Bs(B + 1, 0);
  rep(i, B + 1) { Bs[i] = m.at("B") * i; }
  vector<int> Cs(C + 1, 0);
  rep(i, C + 1) { Cs[i] = m.at("C") * i; }

  for(auto &ic: Cs) {
    for(auto &ib: Bs) {
      for(auto &ia: As) {
        if (ic + ib + ia == X) c++;
      }
    }
  }
  cout << c << endl;
  return 0;
}
