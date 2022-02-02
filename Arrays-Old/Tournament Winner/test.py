comp = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]

result = [0,0,1]

# itcomp = iter(comp)
# itres = iter(result)

for i, compi in enumerate(comp):
    print(i)
    print(compi)


currentbest = ""
scores = {currentbest: 0}

print(type(scores))
# dic = dict(zip(itcomp, itres))
# print(dic)

# winner = []
# for i in range(len(result)):
#     if result[i] == 0:
#         winner.append(comp[i][1])
#     else:
#         winner.append(comp[i][0])
        
# # it = iter(winner)
# # count = 0
# # dic = dict.fromkeys(winner, count for winner in winner)
# # print(dic)
