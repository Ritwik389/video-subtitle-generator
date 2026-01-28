class Solution {
public:
    bool isValid(string s) {
     stack<char> ch;
     unordered_map <char,char> map1 = {
        {')', '('}, {'}', '{'}, {']', '['}
     };
     for(char c : s){
        if(c == '(' || c == '{' || c == '[') ch.push(c);
        else if (c == ')' || c == '}' || c == ']') {
            if(ch.empty()) return 0;
            if (map1[c]== ch.top()) ch.pop();
            else return 0;
        }
     }
     if(ch.empty()) return 1;
     return 0;

    }
};