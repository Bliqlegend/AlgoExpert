#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>

using namespace std;

string tournamentWinner(vector<vector<string>> competitions,
                        vector<int> results) 
{

      string currentBest = "";
      unordered_map<string, int> scores= {{currentBest,0}};
      for(int i =0; i< competitions.size(); i++){
            auto result = results[i];
            auto competition = competitions[i];
            auto home = competition[0];
            auto away = competition[1];
            
            auto winner =  result == 1 ? home : away;
            updateScore(winner,3,scores);

            if(scores[winner] > scores[currentBest])
                  currentBest = winner;
      }
      return currentBest;
}

void updateScore(string team,int points,unordered_map<string,int> &scores){
      if (scores.find(team) == scores.end()){
            scores[team] = 0;
      }
      scores[team] += points;
}