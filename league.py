def quicksort(li, pos):
    if len(li) == 0:
        return []
    else:
        pivot = li[0]
        less = []
        great = []
        for i in li[1:]:
            if i[pos] > pivot[pos]:
                less.append(i)
            else:
                great.append(i)
        less = quicksort(less,pos)
        great = quicksort(great,pos)
        return less + [pivot] + great

def add_standing(standing, standings):
    for i in range(len(standings)):
        if standings[i][0] == standing[0]:
            standings[i][1:] = [sum(x) for x in zip(standings[i][1:],standing[1:])]
            break
    else:
        standings.append(standing)

with open('LEAGUE.DAT','r') as f:
    results = f.readlines()

standings = []
for result in results:
    if int(result[16])>int(result[34]):
        win_a = 1
        win_b = 0
        draw = 0
    elif int(result[16])==int(result[34]):
        win_a = 0
        win_b = 0
        draw = 1
    else:
        win_a = 0
        win_b = 1
        draw = 0
    standing = [result[0:15].strip(),\
                win_a, draw, win_b,\
                int(result[16]), int(result[34]),\
                win_a*3 + draw]
    add_standing(standing, standings)
    standing = [result[18:33].strip(),\
                win_b, draw, win_a,\
                int(result[34]), int(result[16]),\
                win_b*3 + draw]
    add_standing(standing, standings)
    
standings = quicksort(standings,-1)
for i in standings:
    print('{0:15}{1:2}{2:2}{3:2}{4:3}{5:3}{6:3}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
