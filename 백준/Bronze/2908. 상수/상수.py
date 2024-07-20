import sys
input = sys.stdin.read
data = input().split()



def comparisonFnc(data):
    number_arr = []
    for item in data:
        # number = []
        reversed_item = "".join(reversed(item))
        number_arr.append(reversed_item)

    if number_arr[0] > number_arr[1]: 
        return number_arr[0]
    else:
        return number_arr[1]
    

result = comparisonFnc(data)

print(result)