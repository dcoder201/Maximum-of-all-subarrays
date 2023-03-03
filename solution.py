#User function Template for python3
from collections import deque
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
      max_deque = deque()
      max_list = []
      for i in range(k):
        while max_deque and arr[i] >= arr[max_deque[-1]]:
            max_deque.pop()
        max_deque.append(i)
    
    # process remaining elements
      for i in range(k, n):
        max_list.append(arr[max_deque[0]])
        
        # remove elements outside current window
        while max_deque and max_deque[0] <= i-k:
            max_deque.popleft()
            
        # remove elements smaller than current element
        while max_deque and arr[i] >= arr[max_deque[-1]]:
            max_deque.pop()
        
        # add current element to deque
        max_deque.append(i)
    
    # add maximum element for last subarray
      max_list.append(arr[max_deque[0]])
    
      return max_list


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends
