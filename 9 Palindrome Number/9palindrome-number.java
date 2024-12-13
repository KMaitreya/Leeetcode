class Solution {
    public boolean isPalindrome(int x) {
        
        String s=Integer.toString(x);
        int n=s.length();
        
        for(int i=0; i<=n/2; i++)
        if(s.charAt(i)!=s.charAt(n-i-1))
        return false;
        
        return true;
        // rev+=s.charAt(i);

        // System.out.println(rev);
        // System.out.println(s);

        // return s.equals(rev);
    }
}