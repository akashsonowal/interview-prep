# Python

1. Lambda, map, filter, reduce
The lambda keyword is used to create inline functions. The functionssquare_fn and square_ld below are identical.
```
def square_fn(x):
  return x * x
 
square_ld = lambda x: x * x

for i in range(10):
  assert square_fn(i) == square_ld(i)
```
