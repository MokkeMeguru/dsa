#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

struct Node{
  int key;
  Node* next;
  Node* prev;
  // string to_str() {
  //   return to_string(key);
  // }
};

Node *head;

void init() {
  head = (Node*)malloc(sizeof(Node));
  head->key = -1;
  head->next = head;
  head->prev = head;
}
Node* search(int key) {
  Node *cursor = head->next;
  while(cursor != head && cursor->key != key)
    cursor = cursor->next;
  return cursor;
}

void deleteNode(Node* node) {
  if (node == head) return;
  node->prev->next = node->next;
  node->next->prev = node->prev;
  free(node);
}

void deleteFirst() {
  deleteNode(head->next);
}
void deleteLast() {
  deleteNode(head->prev);
}

void insert(int key) {
  Node* temp = (Node*)malloc(sizeof(Node));
  temp->key = key;
  temp->next = head->next;
  temp->prev = head;
  head->next->prev = temp;
  head->next = temp;
}

int main() {
  init();
  int N;
  cin >> N;
  char line[30];
  int key;
  rep(i, N) {
    scanf("%s%d", line, &key);
    if (line[0] == 'i')
      insert(key);
    else if (line[6] == 'F')
      deleteFirst();
    else if (line[6] == 'L')
      deleteLast();
    else
      deleteNode(search(key));
  }
  Node* current = head->next;
  bool first = true;
  while(current != head) {
    if (first) {
      cout << current->key;
      first = false;
    } else {
      cout << " " << current->key;
    }
    current = current->next;
  }
  cout << endl;
  return 0;
}
