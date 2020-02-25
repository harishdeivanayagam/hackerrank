x = [1,2,3,4,5,2,1,2]
y = [11,11,10,10,10]
z = [1,3,2,1,2]
f = [9,4,6,5,7,3,5,7,2,1]
m = [6320,6020,6098,1332,7263,672,9472,2838,3401,9494]

class Stack:
  def __init__(self):
    self.stack = []
  def listConvert(self,l):
    self.stack = l
  def getLength(self):
    return len(self.stack)
  def push(self,n):
    self.stack.append(n)
  def pop(self):
    temp = self.top()
    self.stack.pop()
    return temp
  def top(self):
    return self.stack[len(self.stack)-1]
  def isEmpty(self):
    if self.stack == []:
      return True
    else:
      return False
  def clean(self):
    self.stack = []


def code(l):
  position = Stack()
  max_score = 0
  i=0
  while i < len(l):
    if position.isEmpty() == True or l[position.top()] <= l[i]:
      position.push(i)
      i+=1
    else:
      temp = position.pop()
      if position.isEmpty() == True:
        area = l[temp] * i
      else:
        area = l[temp] * (i-position.top()-1)
      if max_score < area:
        max_score = area


  while position.isEmpty() == False:
    temp = position.pop()
    if position.isEmpty() == True:
      area = l[temp] * i
    else:
      area = l[temp] * (i-position.top()-1)
    if max_score < area :
      max_score = area

  return max_score


print(code(m))
