#a x + b = cy
import math
def cal_a_b(p1,p2):
    if p1[0] - p2[0]!=0:
        a = (p1[1] - p2[1])/(p1[0] - p2[0]) 
        c = 1
        b = p1[1] - a*p1[0]
    else:
        a = 1
        c = 0
        b = -p1[0]
    return (a,b,c)

def main(points):
    lens = len(points)
    i = 0
    result = {}
    max_int = 0
    while i<lens-1:
        j=i+1
        while j<lens:
            index = cal_a_b(points[i], points[j])
            if index in result:
                result[index] += 1
            else:
                result[index] = 1
            max_int = max(max_int, result[index])
            j+=1
        i+=1
    return int(((max_int*8 +1)**0.5 +1 )/2)

if __name__ == '__main__':
    p = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,1]]
    s = main(p)
    print(s)