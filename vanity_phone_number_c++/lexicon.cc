#include "lexicon.h"

#include <map>

using namespace std;

struct Node {
  bool isWord;  // indicates whether the path <root->node> is a word
  map<char, Node*> suffixes;
  Node() { isWord = false; }
  ~Node() {
    for (auto x : suffixes) {
      delete x.second;
    }
  }
};

Lexicon::Lexicon() : root{nullptr} {}
Lexicon::~Lexicon() { delete root; }

void Lexicon::add(const string& word) { getNode(word)->isWord = true; }

bool Lexicon::containsPrefix(const string& prefix) const {
  return findNode(prefix) != nullptr;
}

bool Lexicon::containsWord(const string& word) const {
  const Node* found = findNode(word);
  return found != nullptr && found->isWord;
}

Node* Lexicon::findNode(const string& str) const {
  Node* curr = root;
  for (size_t pos = 0; pos < str.size() && curr != nullptr; pos++) {
    curr = (curr->suffixes.find(str[pos]) != curr->suffixes.end())
               ? curr->suffixes[str[pos]]
               : nullptr;
  }

  return curr;
}

Node* Lexicon::getNode(const string& str) {
  Node** currp = &root;

  size_t pos = 0;
  while (true) {
    if (*currp == nullptr) *currp = new Node;
    if (pos == str.size()) break;
    currp = &((*currp)->suffixes[str[pos]]);
    pos++;
  }
  return *currp;
}
