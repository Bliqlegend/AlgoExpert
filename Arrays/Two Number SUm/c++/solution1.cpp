#include <vector>
#include <algorithm>
using namespace std;

// O(n2) Time Complexity | O(1) Complexity

vector<int> twoNumberSum(vector<int> array, int targetSum) {
  // Write your code here.
	for(int i =0;i< array.size()-1;i++){
		int first = array[i];
		for (int j = i +1; j< array.size();j++) {
			int second = array[j];
			if(first + second == targetSum){
				return vector<int>{first,second};
			}
		}
	}
  return {};
}
