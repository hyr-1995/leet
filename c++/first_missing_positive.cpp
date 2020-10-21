class Solution:
    # 将对应的数值放在对应的数组位置上

    @staticmethod
    def swap(nums, a, b):
        temp = nums[a] 
        nums[a] = nums[b] 
        nums[b] = temp 


    def firstMissingPositive(self, nums):
        
        lens = len(nums)
        for i in range(lens):
            while(nums[i]>0 and nums[i]<=lens and nums[i]!=nums[nums[i]-1]):
                self.swap(nums, i, nums[i]-1)

        for i in range(lens):
            if nums[i] != i + 1:
                return i+1

        return lens + 1

if __name__ == '__main__':
    nums = [4,5,6,7,8]
    s = Solution()
    print(s.firstMissingPositive(nums)) 