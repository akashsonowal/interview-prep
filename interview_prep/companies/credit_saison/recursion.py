class Solution:
  def __init__(self):
    self.op = {}
  
  def modify_input(self, ip, prefix=""):
    for k, v in ip.items():
      parent_k = "_".join((prefix, k))

      if type(v) == dict:
        self.modify_input(v, parent_k)
      else:
        self.op[parent_k] = v


if __name__ == "__main__":
    ip = {
      'a': 1,
      'b': {
            'c': 2,
            'd': {
                  'e': 3
                  },
           }
     }
    op = {
       '_a': 1, 
       '_b_c': 2, 
       '_b_d_e': 3
    }

    s = Solution()
    s.modify_input(ip)
    assert s.op == op