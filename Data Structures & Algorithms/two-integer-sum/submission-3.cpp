class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // value, index
        unordered_map<int, int> seen; 
        for (int i = 0; i < nums.size(); i++) {
            int d = target - nums[i];

            if (seen.contains(d)) {
                return {seen[d], i};
            }

            seen[nums[i]] = i;
        }
        
    }
};
