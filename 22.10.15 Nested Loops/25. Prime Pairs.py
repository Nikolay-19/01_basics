first_num = int(input())
second_num = int(input())
dif_f_num = int(input())
dif_s_num = int(input())
last_f = first_num + dif_f_num
last_s = second_num + dif_s_num
 
for a in range(first_num, last_f + 1):
    for c in range(second_num, last_s + 1):
        if a in [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
            if c in [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
                print(f"{a}{c}")
 