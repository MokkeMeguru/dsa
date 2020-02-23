#include <bits/stdc++.h>
#include <math.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> A(N, 0);
  int sum = 0;
  for (int i = 0; i < N; i++) {
    cin >> A.at(i);
    sum += A.at(i);
  }
  int mean = sum / N;
  for (int i = 0; i < N; i++) {
    cout << abs(int(A.at(i)) - mean) << endl;
  }
}
