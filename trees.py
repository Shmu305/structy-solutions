#037 depth first values
def depth_first_values(root):
  if not root:
    return []
  res = []
  stack = [root]
  while stack:
    curr = stack.pop()
    res.append(curr.val)
    if curr.right:
      stack.append(curr.right)
    if curr.left:
      stack.append(curr.left)
  return res
