def better_than_average(class_points, your_points):
    # Your code here
  if (sum(class_points)/len(class_points)) < your_points:
    print(True)
  else:
    print(False)

  pass

better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50)