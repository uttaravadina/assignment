mat = [
[0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1],
[1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1],
[1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
[1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
[1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
[0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
[0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
[1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1]]

label = [[0 for j in range(len(mat[i]))] for i in range(len(mat))]
labelidx = 1

def firstPass():
  global labelidx
  for i in range(len(mat)):
    for j in range(len(mat[i])):
      if mat[i][j] != 1:
        continue
      l = labelidx
      if i-1 >= 0 and mat[i-1][j] != 0 and l > label[i-1][j]:
        l = label[i-1][j]
      if j-1 >= 0 and mat[i][j-1] != 0 and l > label[i][j-1]:
        l = label[i][j-1]
      label[i][j] = l
      if l == labelidx:
        labelidx = labelidx + 1

def secondPass():
  for i in range(len(label)):
    for j in range(len(label[i])):
      if label[i][j] == 0:
        continue
      l = label[i][j]
      if i-1 >= 0 and label[i-1][j] != 0 and l > label[i-1][j]:
        l = label[i-1][j]
      if j-1 >= 0 and label[i][j-1] != 0 and l > label[i][j-1]:
        l = label[i][j-1]
      if i+1 < len(label) and label[i+1][j] != 0 and l > label[i+1][j]:
        l = label[i+1][j]
      if j+1 < len(label[i]) and label[i][j+1] != 0 and l > label[i][j+1]:
        l = label[i][j+1]
      label[i][j] = l

def printLabel():
  for i in range(len(label)):
    label[i] = map(str,label[i])
    print(' '.join( label[i] ))


if __name__ == '__main__':
  firstPass()
  secondPass()
  printLabel()
