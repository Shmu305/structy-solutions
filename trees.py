#037 depth first values

def depth_first_values(root): #iterative
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

def depth_first_values(root): #recursive
  if not root:
    return []
  left_values = depth_first_values(root.left)
  right_values = depth_first_values(root.right)
  return [root.val] + left_values + right_values
  
