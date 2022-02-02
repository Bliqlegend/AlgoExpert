#include <vector>
#include <algorithm>

using namespace std;
// O(n) Time | O(1) Space

bool isValidSubsequence(vector<int> array, vector<int> sequence) {
  // Write your code here.
	int arid = 0;
	int sid = 0;
	while(arid < array.size() && sid < sequence.size()){
		if (array[arid] == sequence[sid])
			sid+=1;
		arid+=1;
	}
  return sid == sequence.size();
}
