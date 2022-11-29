mem = {}

def staircaseTraversal2(height, maxSteps):
  result = [0] * (height + 1)
  result[0] = 1
  for h in range(1, height + 1):
    total = 0
    for step in range(1, maxSteps + 1):
      if h - step >= 0:
        total += result[h - step]
    result[h] = total
    
  return result[height]


def staircaseTraversal(height, maxSteps):
    # Write your code here.
    if height in mem:
      return mem[height]
    if height <= 0:
      return 1
	
    mem[height] = 0
    for step in range(1, maxSteps + 1):
        if step > height:
          break
        mem[height] += staircaseTraversal(height - step, maxSteps)

    return mem[height]

print(staircaseTraversal2(4,3))