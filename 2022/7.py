class Node:
  def __init__(self, path, size):
    self.parent = None
    self.path = path
    self.children = []
    self.files = []
    self.size = 0


def getNode(s):
  for node in nodes:
    if node.path == s:
      return node
  sys.exit(0)


if __name__ == '__main__':
  f = open("7.in", "r")
  lines = f.read().splitlines()

  R = Node('/', 0)
  nodes =[R]
  cd = [R]

  for line in lines:
    if line[0] == "$":
      # split to get command
      spl = line.split("$ ")[1]
      cmdsplit = spl.split(" ")
      cmd = cmdsplit[0]

      if cmd == "cd":
        where = cmdsplit[1]
        # go to home directory
        if where == "/":
          cd = [R]
        # one dir back
        elif where == "..":
          cd.pop()
        # get full path for this directory and move there
        else:
          if not (len(cd) == 1 and cd[0].path == "/"):
            fp = cd[-1].path + "/%s" % where
          else:
            fp = "/%s" % where
          cd.append(getNode(fp))

    # add directory to children with a full path
    elif "dir" in line:
      which = line.split("dir ")[1]
      if not (len(cd) == 1 and cd[0].path == "/"):
        fp = cd[-1].path + "/%s" % which
      else:
        fp = "/%s" % which

      # add a new node
      newNode = Node(fp, 0)
      nodes.append(newNode)
      curr = cd[-1]
      curr.children.append(newNode)
      newNode.parent = curr

    # add files to current child along with sizes
    else:
      fsplit = line.split(" ")
      fsize = fsplit[0]
      fname = fsplit[1]
      curr = cd[-1]
      curr.files.append({
        "size": int(fsize),
        "name": fname
      })
      curr.size += int(fsize)

  # propagate sums of subdirectories
  N = [node.path for node in nodes]
  for npath in sorted(N, key=len, reverse=True):
    node = getNode(npath)
    # add this node's size if it is in someone else's children
    for inner in nodes:
      for c in inner.children:
        if node.path == c.path:
          inner.size += node.size

  # part 1
  S = 0
  for npath in N:
    node = getNode(npath)
    if node.size <= 100000:
      S += node.size
  print("p1: %d" % S)

  # part 2
  S = []
  unused = 70000000 - 49199225
  for npath in N:
    node = getNode(npath)
    if node.path != "/" and unused + node.size >= 30000000:
      S.append(node.size)
  print("p2: %d" % min(S))

