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
  def findHeight(self):
    temp = 0
    for i in self.stack:
      temp += i
    return temp


def equalStacks(h1,h2,h3):
  s1 = Stack()
  s2 = Stack()
  s3 = Stack()
  s1.listConvert(list(reversed(h1)))
  s2.listConvert(list(reversed(h2)))
  s3.listConvert(list(reversed(h3)))
  s1_height = s1.findHeight()
  s2_height = s2.findHeight()
  s3_height = s3.findHeight()
  while s1_height != s2_height or s2_height != s3_height or s1_height != s3_height:
    temp = max(s1_height,s2_height,s3_height)
    if temp == s1_height:
      s1_height -= s1.pop()
    elif temp == s2_height:
      s2_height -= s2.pop()
    else:
      s3_height -= s3.pop()
  return s1_height


x = [3,2,1,1,1]
y = [4,3,2]
z = [1,1,4,1]
print(equalStacks(x,y,z))
