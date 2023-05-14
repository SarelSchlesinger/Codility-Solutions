// Kadane's Algorithm
class Solution {
    public int solution(int[] A) {
        int res = A[0];
        int temp = A[0];
        for (int i = 1; i < A.length; i++) {
            temp = Math.max(A[i], temp + A[i]);
            if (temp > res) {
                res = temp;
            }
        }
		return res;
    }
}