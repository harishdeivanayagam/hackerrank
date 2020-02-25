def compare(x,y):
  if x=='{' and y=='}':
    return True
  elif x=='[' and y==']':
    return True
  elif x=='(' and y==')':
    return True
  else:
    return False

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
    self.stack.pop()
  def top(self):
    return self.stack[len(self.stack)-1]
  def isEmpty(self):
    if self.stack == []:
      return True
    else:
      return False
  def clean(self):
    self.stack = []


def stack(s):
  l = list(s)
  read = Stack()
  write = Stack()
  read.listConvert(l)
  write.push(read.top())
  read.pop()
  while read.isEmpty() == False:
    if write.isEmpty() == False :
      if compare(read.top(),write.top()) == True:
        write.pop()
      else:
        write.push(read.top())
    else:
      write.push(read.top())
    read.pop()

  if write.isEmpty():
    print('YES')
  else:
    print('NO')

stack('{([])}')
