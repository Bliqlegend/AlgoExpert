#include <vector>
#include <algorithm>
using namespace std;

vector<int> sortedSquaredArray(vector<int> array) {
    vector<int> newArray(array.size(),0);
    for(int i=0; i<array.size();i++){
        int val = array[i];
        newArray[i] = val*val;
    }
    sort(newArray.begin(),newArray.end());
    return newArray;
}