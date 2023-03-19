# python3

#Julija Sokolova 221RDB058
def heap(data,a, j, swaps):
len1=j*2+1
len2=j*2+2
res=j
if len1<a and data[len1]<data[res]:
    res=len1
if len2<a and data[len2]<data[res]:
    res=len2
if res!=a:
    swaps.append((a,res))
    data[a], data[res]=data[res],data[a]
    heap(data, a, res, swaps)


def build_heap(data, a):
    swaps = []
    a=len(data)
    for i in range(a//2-1,-1,-1):
        heap(data, a, j, swaps)
 
    return swaps    
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
