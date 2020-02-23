#include <bits/stdc++.h>
#include <boost/format.hpp>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
map<string, int> integer_variables;
map<string, vector<int>> vector_variables;

void routing(string &);
void define_int();
void define_vector();
void print_int();
void print_vector();
int read_int();
vector<int> read_vector();

int read_int() {
  string variable;
  cin >> variable;
  if(isdigit(variable.at(0)))
    return stoi(variable);
  else
    return integer_variables.at(variable);
}

vector<int> read_vector() {
  string variable;
  vector<int> temp;
  cin >> variable;
  if( variable != "[")
    return vector_variables.at(variable);
  else {
    while (variable != "]") {
      temp.push_back(read_int());
      cin >> variable; // "," or "]"
    }
    return temp;
  }
}

int calc_int() {
  auto value = read_int();
  string expression;
  cin >> expression;
  while(expression != ";") {
    if (expression == "+")
      value += read_int();
    if (expression == "-")
      value -= read_int();
    cin >> expression;
  }
  return value;
}

vector<int> calc_vector() {
  auto value = read_vector();
  string expression;
  cin >> expression;
  while (expression != ";") {
    if (expression == "+") {
      auto _value = read_vector();
      rep(i, value.size()) value.at(i) += _value.at(i);
    }
    if (expression == "-") {
      auto _value = read_vector();
      rep(i, value.size()) value.at(i) -= _value.at(i);
    }
    cin >> expression;
  }
  return value;
}

void define_int() {
  string variable;
  cin >> variable;
  string expression;
  cin >> expression; //  "="
  integer_variables[variable] = calc_int();
}

void define_vector() {
  string variable;
  cin >> variable;
  string expression;
  cin >> expression; // "="
  vector_variables[variable] = calc_vector();
}

void print_int() {
  cout << calc_int() << endl;
}
void print_vector() {
  auto temp  = calc_vector();
  cout << "[";
  for(auto v : temp) {
    cout << " " << v ;
  }
  cout << " ]" << endl;
}

void routing(string &order) {
  if (order == "int")
    define_int();
  if (order == "vec")
    define_vector();
  if (order == "print_int")
    print_int();
  if (order == "print_vec")
    print_vector();
}

int main() {
  int N;
  cin >> N;
  for (int i = 0; i < N; i++) {
    string order;
    cin >> order;
    routing(order);
  }
  return 0;
}
