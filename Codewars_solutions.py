# Collection of my Codewars solutions

# Can you get the loop?
# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863

def loop_size(node):
    nextNode = Node()
    lstA = [hex(id(node))]
    nextNode = node
    position = 0
    while True:
        nextNode = nextNode.next
        if hex(id(nextNode)) in lstA:
            position = lstA.index(hex(id(nextNode)))
            break
        lstA.append(hex(id(nextNode)))
    #print lstA, position, len(lstA)-position
    output = len(lstA)-position
    return output
    
# Strip Comments
# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

import re

def solution(string,markers):
    lstRows = string.split("\n")
    lstRes = list()
    for row in lstRows:
        #lstPos = [m.start() for marker in markers for m in re.finditer(marker, row)]
        lstPos = [row.find(x) for x in markers if row.find(x)!=-1]
        print lstPos
        pos = len(row)
        if lstPos:
            pos = min(lstPos)
        lstRes.append(row[:pos].rstrip())        
    return "\n".join(lstRes)
    
# IP Validation
# https://www.codewars.com/kata/515decfd9dcfc23bb6000006

def is_number(s):
    if " " in s:
        return False
    if "-" in s:
        return False
    if len(s)>1 and s[0]=="0":
        return False
    try:
        x = int(s)
        if x>255:
            return False
        return True
    except ValueError:
        return False

def is_valid_IP(strng):
    print strng
    lstBool = ([is_number(x) for x in strng.split(".")])
    if all(lstBool) and len(lstBool)==4:
        return True
    else:
        return False
        
        
# Roman Numerals Encoder
# https://www.codewars.com/kata/51b62bf6a9c58071c600001b

def solution(n):
    tplConv = (("I","V"),("X","L"),("C","D"),("M",""))
    strRes = ""    
    for c, digit in enumerate(str(n)):
        strAct=""
        if int(digit) in (1,2,3):        
            strAct = tplConv[len(str(n))-(c+1)][0]*int(digit)
        elif int(digit) in (4,):
            strAct = tplConv[len(str(n))-(c+1)][0] + tplConv[len(str(n))-(c+1)][1]        
        elif int(digit) in (5,):
            strAct = tplConv[len(str(n))-(c+1)][1]      
        elif int(digit) in (6,7,8):
            strAct = tplConv[len(str(n))-(c+1)][1]+tplConv[len(str(n))-(c+1)][0]*(int(digit)-5)
        elif int(digit) in (9,):
            strAct = tplConv[len(str(n))-(c+1)][0] + tplConv[len(str(n))-(c+1)+1][0]
        strRes += strAct
    return strRes
    
    
# Snail
# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(array):
    lstDirections = ("Right","Down","Left","Up")
    
    dctMoves = {"Right":(1,0),
    "Down":(0,1),
    "Left":(-1,0),
    "Up":(0,-1)}
    
    dctNextMove = {"Right":"Down",
    "Down":"Left",
    "Left":"Up",
    "Up":"Right"}
    
    lstMatrix = array
    
    curDirection = lstDirections[0]
    curPosition = (0,0)
    xLen = len(lstMatrix[0])
    yLen = len(lstMatrix)
    intSteps = xLen * yLen
    bWall = False
    lstSteps = list()
    
    while len(lstSteps) != intSteps:
        if curPosition not in lstSteps:
            lstSteps.append(curPosition)
        nextMove = (curPosition[0]+dctMoves[curDirection][0],curPosition[1]+dctMoves[curDirection][1])
        if nextMove in lstSteps or nextMove[0]>=xLen or nextMove[0] < 0 or nextMove[1]>=yLen or nextMove[1]<0:
            curDirection = dctNextMove[curDirection]
            continue
        curPosition = nextMove
        
    return [lstMatrix[step[1]][step[0]] for step in lstSteps]
