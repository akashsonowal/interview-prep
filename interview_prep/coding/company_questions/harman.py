# Data Scientist (NLP) 
# Round 1 (28/08/2023)

# swap two numbers without using a third variable
def swap(a, b):
    a = a + b 
    b = a - b 
    a = a - b 
    return a, b

# sort using lambda
def sorting_with_lambda(x):
    return sorted(x, key=lambda x: x["model"], reverse=True)

if __name__ == "__main__":
    assert 2, 3 == swap(3, 2)
    assert [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}] == sorting_with_lambda([{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}])