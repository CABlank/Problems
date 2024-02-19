#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

class Node {
public:
    int count;
    unordered_map<char, Node*> children;

    Node() : count(0) {}
};

class Trie {
private:
    Node* root;

public:
    Trie() {
        root = new Node();
    }

    void insert(const string& word) {
        Node* current = root;
        for (char ch : word) {
            if (current->children.find(ch) == current->children.end()) {
                current->children[ch] = new Node();
            }
            current = current->children[ch];
            current->count++;
        }
    }

    string find(const string& word) {
        Node* current = root;
        string prefix;
        for (char ch : word) {
            prefix += ch;
            if (current->children[ch]->count == 1) {
                return prefix;
            }
            current = current->children[ch];
        }
        return prefix;
    }
};

vector<string> shortest_unique_prefix(const vector<string>& words) {
    Trie trie;
    for (const string& word : words) {
        trie.insert(word);
    }

    vector<string> result;
    for (const string& word : words) {
        result.push_back(trie.find(word));
    }
    return result;
}

int main() {
    vector<string> words = {"joma", "john", "jack", "techlead"};
    vector<string> prefixes = shortest_unique_prefix(words);

    for (const string& prefix : prefixes) {
        cout << prefix << " ";
    }

    return 0;
}
