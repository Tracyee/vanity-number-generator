#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "lexicon.h"
#include "vanityGen.h"

using namespace std;

int main(int argc, char** argv) {
  // read from an English word file to a lexicon tree
  Lexicon* lexicon = new Lexicon;
  ifstream wordFile{"wiki-100k.txt"};
  string word;
  while (getline(wordFile, word)) {
    lexicon->add(word);
  }

  long long phoneNumber = 2222222222;
  while (true) {
    cout << "enter a phone number: ";
    cin >> phoneNumber;
    VanityGen vanityGen{to_string(phoneNumber), lexicon};
    vector<string> vanities = vanityGen.getMyVanity();
    if (vanities.size() > 0) {
      cout << "phone number: " << phoneNumber << " vanity: ";
      for (auto vanity : vanities) {
        cout << vanity << " ";
      }
      cout << endl;
    }
    // ++phoneNumber;
    // if (phoneNumber == 9999999999) break;
  }

  return 0;
}
