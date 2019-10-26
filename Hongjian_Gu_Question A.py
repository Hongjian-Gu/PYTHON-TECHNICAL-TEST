#!/usr/bin/env python
# coding: utf-8
'''
overlap((number, number), (number, number))
pass in two pairs of numbers, each represents a line on the x-axis
returns whether they overlap
'''
def overlap(line1, line2):
#     test_range(n, lower, upper) test whether number n is in the range of (lower, upper)
    def test_range(n, lower, upper):
        if (n <= max(lower,upper)) and (n >= min(lower,upper)):
            return True
        else :
            return False
    return test_range(line1[0], line2[0], line2[1]) or test_range(line1[1], line2[0], line2[1])


if __name__ == "__main__":
    print("check overlap: (1,5) and (2,6)")
    print(overlap((1,5), (2,6)))
