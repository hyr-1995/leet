def judge_range(nums, n, target):
    if sum(nums[:n]) > target or sum(nums[-n:]) < target:
        return True 
    else:
        return False

def two_sum(nums, target):
    lens = len(nums)
    low = 0
    high = lens - 1
    result = list()
    while low < high:
        temp_res = nums[low] + nums[high]
        if temp_res < target or (low>0 and nums[low]==nums[low-1]):
            low += 1
        elif temp_res> target or (high < lens -1 and nums[high]==nums[high+1]):
            high -= 1
        elif temp_res == target:
            result.append([nums[low], nums[high]])
            low += 1
            high -= 1
    return result


def n_sum(nums, n, target):
    result = []
    lens = len(nums)
    # print("in n", nums, n, target)
    if n < 2 or lens < 2 or judge_range(nums, n, target):
        return result

    if n == 2:    # 2-sum   nums has be sorted
        res = two_sum(nums, target)
        return res
    else:
        for i in range(lens-n+1):
            # print('in',i)
            if i>0 and nums[i] == nums[i-1]:
                continue
            sset = n_sum(nums[i+1:], n-1, target-nums[i])
            for item in sset:
                result.append([nums[i]] + item)
    return result





def main():
    # a = [7,8]
    # print(two_sum(a, 15))
    s = [-2,-1,-1,1,1,2,2]
    s.sort()
    print(n_sum(s,4,0))

if __name__ == '__main__':
    main()