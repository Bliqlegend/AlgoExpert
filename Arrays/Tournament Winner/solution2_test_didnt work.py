def tournamentWinner(competitions, results):
    winner = ""
    scores = {winner: 0}
    points = 3
    for i in range(len(results)):
        home,away = competitions[i][0],competitions[i][1]
        winner = home if results[i]==1 else away
        scores[winner]+=1
    print(scores)


comp = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]

result = [0,0,1]

tournamentWinner(comp,result)