// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

import java.util.LinkedList;
import java.util.List;

class Solution {
    public int solution(int N) {
        List<Integer> binNum = new LinkedList<>();
        while (N > 0) {
            if (N % 2 == 1) {
                binNum.add(1);
            }
            else {
                binNum.add(0);
            }
            N /= 2;
        }
        boolean flag = false;
        int result = 0;
        int temp = 0;
        for (int i = 0; i < binNum.size(); i++) {
            if (flag == false && binNum.get(i) == 1) {
                flag = true;
            }
            else if (flag == true && binNum.get(i) == 1) {
                if (temp > result) {
                    result = temp;
                }
                temp = 0;                
            }
            else if (flag == true && binNum.get(i) == 0) {
                temp++;
            }
        }
        return result;
    }
}