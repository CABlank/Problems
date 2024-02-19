


class Node {
    constructor() {
        this.count = 0;
        this.children = {};      
    }
}

class Trie {
    constructor(){
        this.root = new Node()
    }

    insert(word) {
        let current = this.root;
        
        for (let i = 0; i < word.length; i++) {
            let char = word.charAt(i);

            if (!current.children[char]) {
                current.children[char] = new Node()
            }

            current = current.children[char]
            current.count += 1
        }
    }

    find(word){
        let current = this.root
        let prefix= '';
        
        for (let i = 0; i < word.length; i++) {
            let char = word.charAt(i);
            prefix += char

            if (current.children[char].count == 1){
                return prefix
            } 
        
            current = current.children[char]
        }
        return prefix
    }
}


function shortest_unique_prefix(words) {
    
    let trie = new Trie()

    for (let i = 0; i < words.length; i++) {
        let word = words[i]
        trie.insert(word)
    }

    result = []

    for (let i = 0; i < words.length; i++){
        let word = words[i]
        result.push(trie.find(word))
    }

    return result;

}

console.log(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))