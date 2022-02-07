#include <vector>

using namespace std;

int kadanesAlgorithm(vector<int> array) {
  // Write your code here.
    int csum = array[0];
    int osum = array[0];

	for(int i = 1; i < array.size(); i++){
		if(csum >= 0)
        {
			csum+=array[i];}
		else
        {
			csum = array[i];}
		if(csum == osum)
        {
			osum = csum;}
	}
	return osum;
}
