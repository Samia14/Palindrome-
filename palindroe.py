def reverse(x):
        y=0
        while(x!=0):
            if x<0:
                x = abs(x)
            if x>0:   
                z= x%10
                x = x/10
                y = y*10
                y = y+z 
        return y
def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """""
        reverse_data = reverse(x)
        newx = abs(x)
        if (reverse_data==newx):
            return True
        else:
            return False
