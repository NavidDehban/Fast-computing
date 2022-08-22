
def lef_and_right(arr):
    s1,s2 = [],[]
    left,right = [],[]
    n = len(arr)
    for i in range(n) :
        while (s1 != [] and arr[s1[-1]] <= arr[i]) :
            s1.pop()
        if (s1 == []) :
            left.append(-1)
        else :
            left.append(s1[-1])
        s1.append(i)   
    for i in range (n-1,-1,-1) :
        while (s2 != [] and arr[s2[-1]] < arr[i]) :
            s2.pop()
        if (s2 == []) :
            right.append(n)
        else :
            right.append(s2[-1])
        s2.append(i)
    right = right[::-1]
    return [left, right]
def result(n, arr):
    left, right = lef_and_right(arr)
    total = 0
    n = int(n)
    Len = [0] * n
    ans = [0] * n
    for k in range (n) :
        r = right[k] - 1
        l = left[k] + 1
        Sum = (r-k+1)*(r-k+2)//2
        ans[k] = (arr[k]*((((k-l)*(k-l+1)//2)*(r-k+1)) + ((k-l+1)*Sum)))
    for k in range (n) :
        total = (total + ans[k])%(10**9 + 7)
    return total
def input_():
    n = input()
    arr = input()
    arr = arr.split()
    n = int(n)
    for i in range(n):
        arr[i] = int(arr[i])
    print(result(n, arr))
input_()



