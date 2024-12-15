class Solution {
    public int mySqrt(int x) {

        if(x==0 || x==1)
        return x;

        int i=2;
        
        while(true)
        {
            if(i*i>x)
            {
                i--;
                break;
            }

            else if(i*i==x)
            break;

            i++;
        }
        return i;
    }
}