#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

// O(nlogn) Time Complexity | O(1) Space

vector<int> twoNumberSum(vector<int> array,int targetSum){

    sort(array.begin(),array.end());
    int left = 0;
    int right = array.size()-1;
    while(left < right){
        int current = array[left] + array[right];
        if (current == targetSum) 
            return {array[left],array[right]};
        else if (current < targetSum)
            left++;
        else if (current > targetSum)
            right--;
    }
    return {};
}