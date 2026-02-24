class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        unordered_map<char, string> map1 = {
            {'2',"abc"}, {'3',"def"}, {'4',"ghi"}, {'5',"jkl"},
            {'6',"mno"}, {'7',"pqrs"}, {'8',"tuv"}, {'9',"wxyz"}
        };
        vector<string> result = {""};
        for (char digit : digits) {
            vector<string> temp;
            for (string s : result) {
                for (char c : map1[digit]) {
                    temp.push_back(s + c);
                }
            }
            
            result = temp;
        }
        
        return result;
    }
};