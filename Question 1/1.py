import numpy as np
import pandas as pd

am = 9
an = 9
asummedNums = [65, 72, 90, 110]

amat = np.random.randint(10, size=(am, an))

class PathFinder:
  def __init__(self, mat, m, n, summedNums):
    self.allPaths = []
    self.summedNumsPaths = []
    self.mat = mat
    self.m = m
    self.n = n
    self.tnop = 0
    self.nop = 0
    self.summedNums = summedNums
    self._summedNumsPaths = [0 for i in range(len(self.summedNums))]

  def calcPath(self, i, j, path, summedNumPath, pi):
      #print("i= %s, j= %s, path= %s, pi= %s" % ( i, j, str(path), pi))
      if (i == self.m - 1):
        summedNumPath[pi-1] = 'D'
        t = pi
        for k in range(j, self.n):
          path[pi]= self.mat[i][k]
          if((pi-1) >= 0 and not(i-1 == 0 and k-1 == 0)):
            if(i-1 >= 0 and path[pi-1] == self.mat[i][k-1]):
              summedNumPath[t] = 'R'
              t = t + 1
          pi = pi + 1
        self.allPaths.append(path)
        self.summedNumsPaths.append(summedNumPath)
        if(sum(path) in self.summedNums):
          while 0 in summedNumPath:
            summedNumPath.remove(0)
          print("%s %s"%(sum(path), ''.join(summedNumPath)))
        return
      elif (j == self.n - 1):
        summedNumPath[pi-1] = 'R'
        t = pi
        for k in range(i, self.m):
          path[pi]= self.mat[k][j]
          if((pi-1) >= 0 and not(k-1 == 0 and j-1 == 0)):
            if(j-1 >= 0 and path[pi-1] == self.mat[k-1][j]):
              summedNumPath[t] = 'D'
              t = t + 1
          pi = pi + 1
        self.allPaths.append(path)
        self.summedNumsPaths.append(summedNumPath)
        if(sum(path) in self.summedNums):
          while 0 in summedNumPath:
            summedNumPath.remove(0)
          print("%s %s"%(sum(path), ''.join(summedNumPath)))
        return

      path[pi]= self.mat[i][j]
      if(pi-1 >= 0 and not(i-1 == 0 and j-1 == 0)):
        if(i-1 >= 0 and path[pi - 1] == self.mat[i-1][j]):
          summedNumPath[pi-1] = 'D'
        elif(j-1 >= 0 and path[pi - 1] == self.mat[i][j-1]):
          summedNumPath[pi-1] = 'R'
      self.calcPath(i + 1, j, path, summedNumPath, pi + 1)
      self.calcPath(i, j + 1, path, summedNumPath, pi + 1)

  def calcAllPaths(self):
    path = [0 for i in range(self.m+self.n)]
    summedNumPath = [0 for i in range(self.m+self.n)]
    self.calcPath(0, 0, path, summedNumPath, 0)

  def numberOfPaths(self, m, n):
    if(m == 1 or n == 1):
      return 1
    return self.numberOfPaths(m-1, n) + self.numberOfPaths(m, n-1)

  def init(self):
    self.nop = self.numberOfPaths(self.m, self.n)
    self.tnop = self.nop -1
    self.calcAllPaths()

if __name__ == '__main__':
  pathFind = PathFinder(amat, am, an, asummedNums)
  pathFind.init()
