#include <bits/stdc++.h>
using namespace std;

unsigned long long luka(unsigned long long n,
                        vector<unsigned long long> &memo) {
  if (n == 0)
    return 2;
  else if (n == 1)
    return 1;
  else if (memo.at(n)) {
    return memo.at(n);
  } else {
    memo.at(n) = luka(n - 1, memo) + luka(n - 2, memo);
    return memo.at(n);
  }
}

int main() {
  unsigned long long n;
  scanf("%llu", &n);
  vector<unsigned long long> memo(87, 0);
  printf("%llu\n", luka(n, memo));
  return 0;
}
