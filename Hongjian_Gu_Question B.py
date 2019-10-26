#!/usr/bin/env python
# coding: utf-8
'''
compareVersion(string version1, string version2)
pass in two version numbers as strings, use dots to separate like "1.2" or "2.1.0"
returns 1 if version1 is greater than version2, 0 if equal, and -1 if less.
'''
def compareVersion(version1, version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    for x in range(min(len(v1),len(v2))):
        if v1[x] > v2[x]:
            return 1
        elif v1[x] < v2[x]:
            return -1
    if len(v1) > len(v2):
        return 1
    elif len(v1) < len(v2):
        return -1
    else:
        return 0

if __name__ == '__main__':
    print("compareVersion(\"2.2.1\",\"1.3.2\"): ", compareVersion("2.2.1","1.3.2"))
    print("compareVersion(\"2.2\",\"1.3.2\"): ", compareVersion("2.2","1.3.2"))
    print("compareVersion(\"1.3\",\"1.3.2\"): ", compareVersion("1.3","1.3.2"))
    print("compareVersion(\"1.3.2\",\"1.3.2\"): ", compareVersion("1.3.2","1.3.2"))
    print("compareVersion(\"133.3\",\"1.322.2\"): ", compareVersion("133.3","1.322.2"))



