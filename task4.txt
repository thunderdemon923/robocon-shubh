class Solution(object):
    def judgeCircle(self, moves):

        """
        :type moves: str
        :rtype: bool
        """
        xPos = 0
        yPos = 0
        for i in range(0,len(moves)):
            if (moves[i]=='L'):
                xPos-=1
                continue
            if (moves[i]=='R'):
                xPos+=1
                continue
            if (moves[i]=='D'):
                yPos-=1
                continue
            if (moves[i]=='U'):
                yPos+=1
                continue
        if (xPos==0 and yPos==0):
            return True
        return False