class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int officer = 0;
        int cm = 1;
        int res = 1;//since there will be one unique element everytime
        while(cm<nums.size()){
            if(nums[cm]==nums[cm-1]){
                cm++;
                continue;
            }
            //duplicate found
            nums[officer+1] = nums[cm];
            officer++;
            cm++;
            res++;
        }
        return res;
    }
};