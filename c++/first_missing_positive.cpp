#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    void ssswap(vector<int>& nums, int i, int j) {
        int temp;
        temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
    int firstMissingPositive(vector<int>& nums) {
        int lens;
        lens = size(nums);
        for(int i=0; i<lens; i++){
            while(nums[i]>0 && nums[i]<lens && nums[i]!=nums[nums[i]-1]){
                swap(nums[i], nums[nums[i]-1]);
            }
        }

        for(int i=0; i<lens; i++){
            if (nums[i]!=i+1){
                return i+1;
            }
        }

        return lens+1;
    }
};

int main(){
    Solution s;
    int b[7] = {3,4,5,6,87,9,10};
    std::vector<int> v(b, b+7);
    t = s.firstMissingPositive(v);
    std::cout<<t;
}