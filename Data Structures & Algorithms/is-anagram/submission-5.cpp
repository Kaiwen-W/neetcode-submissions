class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        vector<int> char_list(26);

        for (int i = 0; i < s.size(); i++) {
            char_list[s[i] - 'a']++;
            char_list[t[i] - 'a']--; 
        } 

        for (int i = 0; i < 26; i++) {
            if (char_list[i] != 0) {
                return false;
            }
        }

        return true;
    }
};
