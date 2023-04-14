class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(math.sqrt(area))
        l = int(math.ceil(area / w))
        
        
        while w* l != area:
            
            if w* l < area:
                l += 1
            
            else:
                w -= 1
        
      
        return [l, w]      

           