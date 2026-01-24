class Solution {
public:
    bool isHappy(int n) {
        int slow = n;
        int fast = next(n);
        while(fast != 1 && slow != fast){
            slow = next(slow);
            fast = next(next(fast));
        }
        return fast==1;

    }

private:
 int next(int a){
    int sum = 0;
    while(a != 0){
    int digit = a%10;
    sum += digit*digit;
    a = a/10;
    }
    return sum;
 }
};