def encode_string(istring):
    initval = [0]*26

    for char in istring:
        index = ord(char) - ord('a')
        initval[index] += 1

    s = ""
    for i in range(26):
        s += chr(ord('a')+i)*initval[i]

    return s

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    result = dict()
    for item in strs:
        s_code = "".join(sorted(item))
        if s_code not in result:
            result[s_code]= [item]
        else:
            result[s_code].append(item) 
    return list(result.values())


def main():
    # print(encode_string("aabbdd"))
    # print(encode_string("badbda"))
    s = ["bdddddddddd", "bbbbbbbbbbc"]
    for ss in s:
        print(sorted(ss))
        print(encode_string(ss))

if __name__ == '__main__':
    main()