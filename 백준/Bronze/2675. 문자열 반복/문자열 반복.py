test_case_index = int(input())

def repeat(r, char_list):
    for char in char_list:
        print(char * int(r), end="")
    print()
    
for idx in range(test_case_index):
    r, string = (input().split())
    char_list = list(string)
    repeat(r, char_list)



