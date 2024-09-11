def number(bus_stops):
  result = [i[0] - i[1] for i in bus_stops]
  print(sum(result))
  pass

number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])