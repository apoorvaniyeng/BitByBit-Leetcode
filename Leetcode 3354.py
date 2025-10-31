class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr= nums
        valid= 0
        
        
        n= len(arr)
        
        
        zeroindexes= []
        for i in range(n):
            if arr[i]== 0:
                zeroindexes.append(i)
        
        
        for val in zeroindexes:
            
            # if you chose to move right first
            arr1= arr[:]#lleet not acepting copy()?
            i= val
            direc= 1 # for right
            
            while 0 <= i and i < n: 
                if arr1[i] == 0:
                    i += direc 
                else:
                    arr1[i] -= 1
                    direc *= -1 # turn left
                    i += direc # move one step 

            if all(x== 0 for x in arr1):
                valid += 1
            
            # if you chose to move left first
            arr2 = arr[:]
            i = val
            direc = -1 # facing left dir
            
            while 0 <= i and i < n: 
                if arr2[i]== 0:
                    i += direc
                else:
                    arr2[i] -= 1
                    direc *= -1 
                    i += direc 

            if all(x== 0 for x in arr2):
                valid += 1

        return valid



        


    
