#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B, C;
  cin >> A >> B >> C;
  vector<int> vec = {A, B, C};
  int _max = *max_element(vec.begin(), vec.end());
  int _min = *min_element(vec.begin(), vec.end());
  cout << _max - _min << endl;
}
