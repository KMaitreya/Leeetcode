class Solution {
    public int[] plusOne(int[] digits) {

        int carry=0;
        int n=digits.length;
        
        for(int i=n-1; i>=0; i--)
        {
            if(digits[i]+1>=10)
            {
                digits[i]=digits[i]-9;
                carry=1;
            }
            else
            {
                digits[i]+=1;
                return digits;
            }
        }

        if(carry==1)
        {
            int[] res=new int[n+1];

            res[0]=1;

            for(int i=0; i<n; i++)
            res[i+1]=digits[i];

            return res;
            
        }
        return digits;
    }
}