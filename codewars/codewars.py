def find_needle(haystack):
  index = haystack.index('needle')
  print(f'found the needle at position {index}')

find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False])