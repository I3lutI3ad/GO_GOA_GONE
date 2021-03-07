class Solution():
    def __init__(self):
        self.answer=0
        
    
    def planTrip(self, moneyDistributed,numPairs,coldWarMembers):
        #write the solution here. 
        go = [[0]*10 for _ in range(10)]
        
        for i in coldWarMembers:
            go[i[0]-1][i[1]-1] = 1
            go[i[1]-1][i[0]-1] = 1
        #print(go)
        for i in range(1,(1<<8)):
            good = 1
            for j in range(0, 8):
                if (i & (1 << j))>0:
                    for k in range(0,8):
                        if (i & (1 << k))>0:
                            if go[j][k]==1:
                                good = 0
            if good==1:
                s = 0
                for j in range(0,8):
                    if (i & (1 << j))>0:
                        s += moneyDistributed[j]
                        
                self.answer = max(self.answer, s)
        return self.answer

def main():
    moneyDistributed = [int(i) for i in input().strip().split()] 
    numPairs = int(input())
    coldWarMembers = []
    for i in range(numPairs):
        pairs = [int(i) for i in input().strip().split(" ")]
        coldWarMembers.append(pairs)
        
    print(Solution().planTrip(moneyDistributed,numPairs,coldWarMembers), end ="")
    
if __name__ == '__main__':
    main()
