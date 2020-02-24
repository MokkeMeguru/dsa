#include <bits/stdc++.h>
#include <boost/format.hpp>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

template <typename Iter> void _sort(Iter begin, Iter end);
template <typename Iter>
void _merge(Iter leftBegin, Iter leftEnd, Iter rightBegin, Iter rightEnd,
            Iter dest);
template <typename T> bool _comp(T left, T right);
template <typename T> void _heap_sort(vector<T>&);
template <typename T> void _build_heap(vector<T>&);
template <typename T> void _shift_down(vector<T>&, int root, int size);

template <typename T> void _shift_down(vector<T>& vec, int root, int size) {
  auto left = 2 * root + 1;
  auto right = 2 * root + 2;
  auto new_root = root;
  if (left > size -1) return;
  if (left == size - 1) {
    new_root = left;
  }
  else {
    if (!_comp(vec.at(left), vec.at(right)))
      new_root = left;
    else
      new_root = right;
  }
  if (new_root != root) {
    if (_comp(vec.at(root), vec.at(new_root))) {
      swap(vec.at(root), vec.at(new_root));
      _shift_down(vec, new_root, size);
    }
  }
}

template <typename T> void _heap_build(vector<T>& vec) {
  for (int root = int(vec.size()) / 2; root >= 0; root--) {
    _shift_down(vec, root, vec.size());
  }
}

template <typename T> void _heap_sort(vector<T>& vec) {
  _heap_build(vec);
  for (int m = vec.size() - 1; m > 0; m--) {
    swap(vec.at(0), vec.at(m));
    _shift_down(vec, 0, m);
  }
}

template <typename T> bool _comp(T left, T right) {
  printf("? %c %c\n", 'A' + left, 'A' + right);
  fflush(stdout);
  char ans;
  scanf(" %c", &ans);
  if (ans == '>')
    return true;
  else
    return false;
}

template <typename Iter>
void _merge(Iter leftBegin, Iter leftEnd, Iter rightBegin, Iter rightEnd,
            Iter dest) {
  while (leftBegin < leftEnd && rightBegin < rightEnd) {
    if (_comp(*leftBegin, *rightBegin))
      *dest++ = *leftBegin++;
    else
      *dest++ = *rightBegin++;
  }
  while (leftBegin < leftEnd) {
    *dest++ = *leftBegin++;
  }
  while (rightBegin < rightEnd) {
    *dest++ = *rightBegin++;
  }
}

template <typename Iter> void _sort(Iter begin, Iter end) {

  // base
  auto dist = end - begin;
  if (dist <= 1)
    return;
  typename iterator_traits<Iter>::value_type temp{};
  // split twice -> copy to left / right
  auto middle = begin + dist / 2;
  vector<decltype(temp)> left;
  vector<decltype(temp)> right;
  copy(begin, middle, back_inserter(left));
  copy(middle, end, back_inserter(right));
  _sort(left.begin(), left.end());
  _sort(right.begin(), right.end());
  _merge(left.begin(), left.end(), right.begin(), right.end(), begin);
};

int main() {
  int N, Q;
  cin >> N >> Q;
  vector<int> base(N, 0);
  rep(i, base.size()) { base.at(i) = i; }
  if (N == 5) {
    _heap_sort(base);
    // _sort(base.begin(), base.end());
  } else {
    _sort(base.begin(), base.end());
  }
  // reverse(base.begin(), base.end());
  cout << "! ";
  for (auto b : base) {
    cout << char('A' + b);
  }
  cout << endl;
  return 0;
}
