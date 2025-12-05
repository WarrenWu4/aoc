filename = '5_ex_input.txt'
filename = '5_input.txt'

with open(filename) as f:
  ranges, _ = [l.split('\n') for l in f.read().strip('\n').split('\n\n')]

ranges = [(int(nums.split('-')[0]), int(nums.split('-')[1])) for nums in ranges]
ranges.sort()

existing_ranges = []
for start, end in ranges:
  # if range intersects with existing range
  # update to combine into 1 range
  # if start is within an existing range, update end bound
  # if end is within an existing range, update start bound
  # otherwise must be unique range
  i = 0
  while (i < len(existing_ranges)):
    start2, end2 = existing_ranges[i]
    if (start2 <= start <= end2): 
      existing_ranges[i] = (start2, max(end, end2))
      break
    if (start2 <= end <= end2):
      existing_ranges[i] = (min(start, start2), end)
      break
    i += 1
  if (i == len(existing_ranges)):
    existing_ranges.append((start, end))

# sum up distance for all ranges in existing ranges
res = sum([end-start+1 for start, end in existing_ranges])
print(res)

