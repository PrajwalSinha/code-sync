class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0; //starting
        int j = numbers.size()-1; //end of the array
        while (i<j){ //stop the program when it i crosses j or become equal
            int sum = numbers[i] + numbers [j]; // declare the sum variable
            if (sum==target){
                return {i+1,j+1};
            }
            else if (sum<target){
                i++;
            }
            else{
                j--;
            }
        }
         return {};//all cases failed the sum is not there in the array given
    }
   
};