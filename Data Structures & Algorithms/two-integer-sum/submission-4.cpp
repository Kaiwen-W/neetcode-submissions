class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // value, index
        unordered_map<int, int> seen; 

        for (int i = 0; i < nums.size(); i++) {
            int n = nums[i];
            int d = target - n;

            if (seen.contains(d)) {
                return {seen[d], i};
            }

            seen[n] = i;
        }
    }
};
