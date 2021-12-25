# You are given an array of n unique integers a = a[0], a[1], ... , a[n - 1] and an integer value k. Find and print the number of pairs (a[i], a
# [j]) where i < j and a[i] + a[j] = k.

'''
input:
6 2 1 4 5 3

output:
2
'''

import sys


def get_sum_count(a, k):
    count = 0
    array_size = len(a)

    for i in range(0, array_size):
        for j in range(i + 1, array_size):
            if a[i] + a[j] == k:
                count += 1
    return count


def main():
    stdin_list = sys.stdin.readlines()
    input_list = []
    for item in stdin_list:
        val = item.strip()
        if val:
            int_val = int(val)
            input_list.append(int_val)

    a = input_list[1:]
    k = input_list[0]
    output = get_sum_count(a, k)
    print('---- output ----')
    print(output)


if __name__ == "__main__":
    main()
