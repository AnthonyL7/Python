def past(h, m, s):
  hour_conversion = h * 3600000
  minute_conversion = m * 60000
  second_conversion = s * 1000
  print(hour_conversion + minute_conversion + second_conversion)
  pass

past(0,1,1)