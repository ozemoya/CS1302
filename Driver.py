from TernarySearch import *

def main():
  nums = [443,339,333,231,202,17,11,9,8,7,6,5,4,1]
  for target in [11,111]:
    print(ternarySearch(target,nums,0,len(nums)-1))  # should print 6 and -1

  nums = [10*i for i in range(100,0,-1)]
  for target in [460,466]:
    print(ternarySearch(target,nums,0,len(nums)-1))  # should print 54 and -1

main()