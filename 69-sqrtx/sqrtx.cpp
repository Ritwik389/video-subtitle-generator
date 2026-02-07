class Solution {
public:
    int mySqrt(int x) {
        long long r = x;
        if (x<2) return x;
        while(r*r>x){
            r = (r+x/r)/2;
        }
        return r;
        
    }
};