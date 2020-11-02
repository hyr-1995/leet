def sum(s):
    sums = 0
    pow_ind = len(s) -1
    for char in s:
        multi = 26 ** pow_ind
        nums = ord(char) - ord('A') +1
        sums += multi*nums
        pow_ind -=1

    return sums

if __name__ == '__main__':
    print(sum("AA"))