def tournamentWinner(competitions, results):
    # Write your code here.
    currentBest = ""
    scores = {currentBest: 0}

    for i,compi in enumerate(competitions):
        result = results[i]
        home, away = compi
        win = home if result==1 else away
        updateScore(win,3,scores)
        if scores[win] > scores[currentBest]:
            currentBest = win

    return currentBest

def updateScore(team,points,scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points


