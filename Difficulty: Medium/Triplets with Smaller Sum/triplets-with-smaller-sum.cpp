class Solution {
  public:
    int countTriplets(int sum, vector<int>& arr) {
        // code here
        sort(arr.begin(), arr.end());
        int n = arr.size();
        int left;
        int right;
        int ans = 0;
        for(int i=0;i<n-2;i++){
            left = i + 1; // i se ek aage
            right = n - 1; // last mai rhega initially
            
            while(left<right){
                int s = arr[i] + arr[left] + arr[right];
                if(s>=sum){
                    right--;
                }
                else{
                    ans = ans + (right-left);
                    left++;
                }
            }
            
        }
        return ans;
    }
};