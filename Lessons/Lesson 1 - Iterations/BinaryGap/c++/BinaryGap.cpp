int solution(int N) {
    
    string binNum = "";
    while (N > 0) {
        if (N % 2 == 0) {
            binNum = '0' + binNum;
        }
        else {
            binNum = '1' + binNum;
        }
        N /= 2;
    }

    int res = 0;
    int temp = 0;
    bool flag = false;

    for (int i = 0; i < binNum.length(); i++) {
        
        if (binNum[i] == '1' && flag == false) {
            flag = true;
        }
        else if (binNum[i] == '0' && flag == false) {
            continue;
        }
        else if (binNum[i] == '0' && flag == true) {
            temp++;
        }
        else {          // binNum[i] == '1' && flag == true
            if (temp > res) {
                res = temp;
            }
            temp = 0;
        }
    }
    return res;
}