class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        int st = 0 , end = n - 1;
        int idx = n - 1;
        vector<int> res(n);

        while(st <= end) {
            int stSq = nums[st] * nums[st];
            int endSq = nums[end] * nums[end];

            if (stSq > endSq) {
                res[idx] = stSq;
                st++;
            }
            else {
                res[idx] = endSq;
                end--;
            }
            idx--;
        }
        return res;
    }
};