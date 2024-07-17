def hero(bullets, dragons):

  required_bullets = dragons * 2

  if bullets < required_bullets:
    print(False)
  else: 
    print(True)
  pass

hero(100, 40)