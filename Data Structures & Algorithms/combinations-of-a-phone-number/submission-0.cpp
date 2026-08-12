class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        vector<string> ans;
        std::map<char, std::string> digits1 = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        
        auto backtrack = [&](auto self, int i, string currstr) -> void {
            if (currstr.length() == digits.length()) {
                ans.push_back(currstr);
                return;
            }
            for (char c : digits1[digits[i]]) {
                self(self, i + 1, currstr + c);
            }
        };

        backtrack(backtrack, 0, "");
        return ans;
    }
};