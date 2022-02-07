#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

// O(n) Time complexity | O(n) Space complexity
vector<int> twoNumberSum(vector<int> array,int targetSum){
    unordered_set<int> nums; // nums = {} like a dictionary in python
    for (int num : array){ // iterating over the whole 
        int match = targetSum - num;
        if (nums.find(match) != nums.end()){
            return vector<int>{match,num};
        } else {
            nums.insert(num);
        }
    }
    return {};
}


