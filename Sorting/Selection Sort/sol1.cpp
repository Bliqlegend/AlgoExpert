#include <vector>
#include <algorithm>


using namespace std;

vector<int> selectionSort(vector<int> array) {
  // Write your code here.
  if(array.empty())
    return {};

  for(int i = 0; i < array.size()-1; i++){
      int minindex = i;
      for(int j =i+1; j < array.size();j++){
          if(array[j] < array[minindex])
            minindex = j;
      }
      swap(array[minindex], array[i]);
  }
  return array;

}
