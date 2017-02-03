#!/bin/python3
import sys
print("Enter number of staircases below")
n = int(input().strip()) #enter number of staircases

for i in range(0,n):
    print('#'.rjust(n-i)+('#'*i)) #padding and print stairs
