/* Kadane's Algorithm */
int solution(int A[], int N) {
    int res = A[0];
    int temp = A[0];
    for (int i = 1; i < N; i++) {
        if (A[i] > temp + A[i]) {
            temp = A[i];
        } else {
            temp = temp + A[i];
        }
        if (temp > res) {
            res = temp;
        }
    }
    return res;
}