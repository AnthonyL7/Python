

def domain_name(url):
  if url.startswith('http://'):
    url = url[len("http://"):]
  elif url.startswith("https://"):
    url = url[len("https://"):]
  
  if url.startswith("www."):
    url = url[len("www."):]
  
  domain_part = url.split("/")[0]
  domain = domain_part.split(".")[0]

  print(domain_part)

domain_name("www.xakep.ru")