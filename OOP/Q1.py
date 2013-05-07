class Bowler():
    def __init__(self,pid,score):
        self.__pid = pid
        self.__score = score

    def get_score(self):
        return self.__score
    
    def display(self):
        print('ID:', self.__pid, 'Score:', self.__score)

def UpdateID(pid):
    weights = [7,4,2,8]
    checkmap = {0:4,1:6,2:3,3:5,4:1,5:9,6:0,7:7,8:2,9:8}
    checksum=0
    for i in range(len(pid)):
        checksum+= int(pid[i])*weights[i]
    checksum = checksum%10
    return pid + str(checkmap[checksum])

#main
#input
n=-1
while not 1<=n<=10:
    try:
        n = int(input("Enter number of bowlers(max 10): "))
    except ValueError:
        print("Number must be integer")
        continue
    if not 1<=n<=10:
        print("Number must be from 1 to 10")
bowlers = []
for i in range(n):
    pid = ''
    score = -1
    while not (pid.isdigit() and len(pid)==4):
        pid = input("Please enter 4-digit ID: ")
        if len(pid)!=4:
            print("ID must be 4-digit")
        if not pid.isdigit():
            print("ID only contains numbers")
    while not 0<=score<=300:
        try:
            score = int(input("Please enter score: "))
        except ValueError:
            print("Score must be number")
            continue
        if not 0<=score<=300:
            print("Score must be between 0 to 300 inclusive")
    bowlers.append(Bowler(pid,score))

#find top scorer
highscore = -1
for i in bowlers:
    if i.get_score()>highscore:
        highscore = i.get_score()
        high = i

print("Top Scorer: ")
high.display()
