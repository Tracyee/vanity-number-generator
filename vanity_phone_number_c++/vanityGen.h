#include <string>
#include <vector>

using namespace std;

class Lexicon;
class InvalidNumber {
 private:
  string number;

 public:
  InvalidNumber(string number) : number{number} {}
  string getNumber() const { return number; }
};

class VanityGen {
  string number;
  vector<string> results;
  Lexicon *lexicon;
  void vanityRec(string prefix, int depth);

 public:
  VanityGen(string number, Lexicon *lexicon);
  vector<string> getMyVanity();
};