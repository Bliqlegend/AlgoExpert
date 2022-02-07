#include <vector>
#include <algorithm>
using namespace std;

int kadanesAlgorithm(vector<int> array) {
  // Write your code here.
    int csum = array[0];
    int osum = array[0];
    for(int i = 1; i < array.size(); i++){
        int num = array[i];
        csum = max(num, csum + num);
        osum = max(osum, csum);
    }
    return osum;
}
