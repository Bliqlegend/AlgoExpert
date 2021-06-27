#include <vector>
#include <algorithm>
using namespace std;

vector<int> bubbleSort(vector<int> array) {
  // Write your code here.
  for(int i=1; i < array.size(); i++){
      for(int j=0;j < array.size()-i;j++){
          if(array[j]>array[j+1]){
						swap(array[j], array[j+1]);
					}
      }
  }
  return array;
}
