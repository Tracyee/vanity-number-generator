#include <string>

using namespace std;

struct Node;

class Lexicon {
  Node* root;
  Node* findNode(const string& str) const;
  Node* getNode(const string& str);

 public:
  Lexicon();
  ~Lexicon();
  void add(const string& word);
  bool containsWord(const string& word) const;
  bool containsPrefix(const string& prefix) const;
};