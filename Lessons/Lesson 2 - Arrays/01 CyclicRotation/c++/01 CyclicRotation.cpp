vector<int> solution(vector<int> &A, int K) {
    if (A.empty()) {
        return A;
    }
	for (int i = 1; i <= K; i++) {
		int lastNum = A[A.size() - 1];
		for (int j = A.size() - 1; j > 0; j--) {
			A[j] = A[j-1];
		}
		A[0] = lastNum;
	}
	return A;
}