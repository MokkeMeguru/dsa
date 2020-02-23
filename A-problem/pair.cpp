#include <bits/stdc++.h>
using namespace std;

int main()
{
  unsigned int N;
  cin >> N;
  vector<pair<unsigned int, unsigned int>> pairs(N, make_pair(0, 0));
  unsigned int ai, bi;
  for (auto &pii : pairs) {
    cin >> ai >> bi;
    pii = make_pair(bi, ai);
  }
  sort(pairs.begin(), pairs.end());
  for (auto &pii: pairs) {
    unsigned int ai, bi;
    tie(bi, ai) = pii;
    cout << ai << " "<< bi <<endl;
  }
  return 0;
}
