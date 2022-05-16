data = input()
ordered = []
data = data.split(",")
data = map(float,data)
for i in data:
  min = data[0]
  for j in data:
    if j < min:
      min = j
  data.remove(min)
  ordered.append(min)
print(ordered)

mid = len(ordered)/2
if mid % 1 == 0:
  median = (ordered[int(mid-1)] + ordered[int(mid)])/2
else:
  median = ordered[int(mid-0.5)]

print(median)