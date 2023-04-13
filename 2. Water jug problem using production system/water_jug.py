from collections import deque
def Solution(a,b,target):
  m={}
  isSolvable=False
  path=[]
  q=deque()
  #initally both the jugs in the double ended queue are empty
  q.append((0,0))
  while(len(q)>0):
    u=q.popleft()
    #now use u as an 'list iterator' of the list m
    #if m is having some data in it then continue
    #initially it will return false
    if((u[0],u[1]) in m):
      continue
    if((u[0]>a or u[1]>b or u[0]<0 or u[1]<0)):
      continue
    #keep adding the numbers to the path until we have u[0]>
    path.append([u[0],u[1]])
    m[(u[0],u[1])]=1

    #if 1st jug is at 4
    if (u[0]==target or u[1]==target):
      isSolvable=True
      if (u[0]==target):
        if(u[1]!=0):
          path.append([u[0],0])
      else:
        if(u[0]!=0):
          path.append([0,u[1]])
      size=len(path)
      for i in range(size):
        print("(",path[i][0],",",path[i][1],")")
      break
    q.append([u[0],b])
    q.append([a,u[1]])
    #doesn't work this way
    # q.append([u[1],a])#jug 1 filling till it's limit
    # q.append([u[0],b])#jug 2 with 3 limit

    for ap in range(max(a,b)+1):
      c=u[0]+ap
      d=u[1]-ap

      if(c==a or (d==0 and d>=0)):
        q.append([c,d])
      c=u[0]-ap
      d=u[1]+ap

      if((c==0 and c>=0) or d==b):
        q.append([c,d])
    q.append([a,0])
    q.append([0,b])
  if(not isSolvable):
    print('Solution not possible here!')

if __name__=='__main__':
  Jug1, Jug2, tare1get=4,3,2
  print("Path from initial state to solution state : ")
  Solution(Jug1,Jug2,target)
