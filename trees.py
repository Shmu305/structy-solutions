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
  
#038 breadth first values
from collections import deque
def breadth_first_values(root):
  if not root:
    return []
  res = []
  queue = deque([root])
  while queue:
    current = queue.popleft()
    res.append(current.val)
    
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return res

#041 fomd tree min value

def tree_min_value(root):
  
  if not root:
    return float('inf')
  min_left = tree_min_value(root.left)
  min_right = tree_min_value(root.right)
  return min(root.val, min_left, min_right)
