class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n=nums.size();
        int l=1,r=1;
        int count=1;
        int atmost=1;
        while(r<n){
            if(nums[r]==nums[r-1]){
                if(atmost<2){
                    count++;
                    nums[l++]=nums[r++];
                    atmost++;
                }else{
                    r++;
                }
            }else{
                atmost=1;
                nums[l++]=nums[r++];
                count++;
            }
        }
        return count;
    }
};