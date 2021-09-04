#include "vanityGen.h"

#include <string>
#include <vector>

#include "lexicon.h"

const vector<string> digit2letter = {"",    "",    "abc",  "def", "ghi",
                                     "jkl", "mno", "pqrs", "tuv", "wxyz"};

VanityGen::VanityGen(string _number, Lexicon* _lexicon)
    : number(_number), lexicon(_lexicon) {}

void VanityGen::vanityRec(string prefix, int depth) {
  if (depth == 10) {
    if (lexicon->containsWord(prefix)) results.push_back(prefix);
    return;
  }
  for (auto letter : digit2letter[number[depth] - '0']) {
    if (lexicon->containsPrefix(prefix + letter))
      VanityGen::vanityRec(prefix + letter, depth + 1);
  }
}

vector<string> VanityGen::getMyVanity() {
  vanityRec("", 0);
  return results;
}
