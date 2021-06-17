#include <algorithm>
#include <vector>

using namespace std;

vector<int> sortedarray(vector<int> array){
	vector<int> newarr(array.size(),0);
	int small = 0;
	int large = array.size()-1;

	for(int i = array.size()-1;i>=0;i--){
		int smallval = array[small];
		int largeval = array[large];

		if (abs(smallval) > abs(largeval)) {
			newarr[i] = smallval*smallval;
			small++;
		}else{
			newarr[i] = largeval*largeval;
			large--;
		}
	}
	return newarr;
}