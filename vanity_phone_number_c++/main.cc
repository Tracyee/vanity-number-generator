#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#include "lexicon.h"
#include "vanityGen.h"

using namespace std;

int main(int argc, char** argv) {
  // read from an English word file to a lexicon tree
  Lexicon* lexicon = new Lexicon;
  cout << "Loading word file..." << endl;
  ifstream wordFile{"wiki-100k.txt"};
  string word;
  cout << "Adding words to the lexicon tree..." << endl;
  while (getline(wordFile, word)) {
    lexicon->add(word);
  }
  cout << "Complete!" << endl;

  long long phoneNumber = 2222222222;
  cin.exceptions(ios::eofbit | ios::failbit);
  while (true) {
    cout << "Enter a phone number: ";
    string s;
    try {
      cin >> s;
      phoneNumber = stol(s, nullptr, 0);
    } catch (const invalid_argument&) {
      cout << "Please enter a valid phone number!" << endl;
      continue;
    } catch (ios::failure&) {
      if (cin.eof()) {
        cout << "\nProgram Terminated!" << endl;
        exit(0);
      }
    }
    // cin >> phoneNumber;
    VanityGen vanityGen{to_string(phoneNumber), lexicon};
    try {
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
    } catch (InvalidNumber ex) {
      cout << "Oops! The phone number " << ex.getNumber()
           << " does not have a corresponding 10-letter English word." << endl;
      continue;
    }
  }

  return 0;
}
