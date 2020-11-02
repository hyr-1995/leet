def multiply(num1, num2):
    len1 = len(num1)
    len2 = len(num2)
    result = [0]*(len1+len2)
    # tmp = 0
    
    for i,char1 in enumerate(reversed(num1)):

        for j,char2 in enumerate(reversed(num2)):
            res = int(char1) * int(char2)
            # index, mods = divmod(res, 10)
            result[i+j] += res
            if result[i+j]>9:
                result[i+j+1] += result[i+j]//10
                result[i+j] = result[i+j]%10
        #     tmp = index 

        # if tmp > 0:
        #     result[i+len2] += tmp 
        #     tmp = 0
        print(result)
    strs = ""
    for intval in reversed(result):
        strs += str(intval)

    start = 0
    while start < len(strs) -1 and strs[start]=="0":
        start += 1

    return strs[start:]
    # return strs 

if __name__ == '__main__':
    print(multiply("123", "456"))
