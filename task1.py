class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        for i in range(numRows):
            if(i == 0):
                l= [1]
                output.append(l)
            else:
                curr = [1]
                j = 1
                while(j < i):
                    
                    curr.append(l[j-1] + l[j])
                    j+=1
               
                curr.append(1)
               
                output.append(curr)
               
                l = curr
        return output      
         

        