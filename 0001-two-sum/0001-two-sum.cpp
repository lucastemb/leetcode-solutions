class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> vals;
        std::vector<int> result; 
        for(int i = 0; i < nums.size(); ++i){
            if(vals.find(target-nums.at(i)) != vals.end()){
                result.push_back(vals[target-nums.at(i)]);
                result.push_back(i);
            }
            vals[nums[i]]=i;
        }
        return result;
    };
};