#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < int(n); i++)
#define SENTINEL INT_MAX
using namespace std;

auto counter = 0;

void merge(vector<int> &S, int left, int mid, int right) {
  vector<int> lv(S.begin() + left, S.begin() + mid);
  vector<int> rv(S.begin() + mid, S.begin() + right);
  lv.push_back(SENTINEL);
  rv.push_back(SENTINEL);
  auto i = 0, j = 0;
  for (int k = left; k < right; k ++){
    counter ++;
    if (lv[i] <= rv[j]) {
      S[k] = lv[i++];
    } else {
      S[k] = rv[j++];
    }
  }
}

void merge_sort(vector<int> &S, int left, int right) {
  if (left + 1 < right) {
    auto mid = (left + right) / 2;
    merge_sort(S, left, mid);
    merge_sort(S, mid, right);
    merge(S, left, mid, right);
  }
}



int main() {
  int n;
  cin >> n;
  vector<int> S;
  int temp;
  rep(_, n) {
    cin >> temp;
    S.push_back(temp);
  }
  auto left = 0;
  auto right = int(S.size());
  merge_sort(S, left, right);
  auto first = true;
  for(auto &item: S) {
    if (first) {
      first = false;
      cout  << item;
    } else{
      cout << " " << item;
    }
  }
  cout << endl <<  counter << endl;
}
