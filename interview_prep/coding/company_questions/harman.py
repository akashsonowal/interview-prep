# swap two numbers without using a third variable
def swap(a, b):
    a = a + b 
    b = a - b 
    a = a - b 
    return a, b

if __name__ == "__main__":
    assert 2, 3 == swap(3, 2)