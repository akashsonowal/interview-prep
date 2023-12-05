ip = "avdcfsd3212ad123ad"

op = ["3212", "123"]

i = 0
res = []

while i < len(ip):
  if ip[i].isdigit():
    l = r = i
    while l >= 0 and ip[l].isdigit():
      l -= 1
    while r < len(ip) and ip[r].isdigit():
      r += 1
    res.append(ip[l + 1: r])
    i = r
  else:
    i += 1 

assert res == op