#include <bits/stdc++.h>
#include <boost/format.hpp>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

template <typename Iter> void _sort(Iter begin, Iter end);
template <typename Iter> void _merge(Iter leftBegin, Iter leftEnd, Iter rightBegin, Iter rightEnd, Iter dest);
template <typename T> bool _comp(T left, T right);

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
  while(leftBegin < leftEnd && rightBegin < rightEnd) {
    if (_comp(*leftBegin,*rightBegin))
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

template<typename Iter>
auto sum(Iter begin, Iter end)
{
  typename iterator_traits<Iter>::value_type sum{};
  Iter _begin = begin;
  while(_begin != end) {
    sum += *_begin++;
  }
  return  sum;
}

int main() {
  int N, Q;
  cin >> N >> Q;
  vector<int> base(N, 0);
  rep(i, base.size()) { base.at(i) = i; }
  _sort(base.begin(), base.end());
  cout << "! ";
  reverse(base.begin(), base.end());
  for (auto b : base) { cout << char('A' + b); }
  cout << endl;
  return 0;
}
