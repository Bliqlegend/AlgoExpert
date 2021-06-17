#include <vector>
using namespace std;

bool isValidSubsequence(vector<int> array, vector<int> sequence) {
  // Write your code here.
	int arid = 0;
	int sid =0;
	for (auto value : array) {
		if (sid == sequence.size())
			break;
        if (value == sequence[sid])
            sid+=1;
	}
  return sid == sequence.size();
}
