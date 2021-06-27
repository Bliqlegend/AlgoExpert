#include <vector>
#include <algorithm>
using namespace std;

vector<int> insertionSort(vector<int> array) {
  // Write your code here.
  for(int i=1; i < array.size(); i++){
      int FocusValue = array[i];
      int FocusPosition = i;
      while(FocusPosition> 0 && array[FocusPosition-1] > FocusValue){
         swap(array[FocusPosition],array[FocusPosition-1]);
		 FocusPosition--;
      }
      array[FocusPosition] = FocusValue;
  }
  return array;
}


