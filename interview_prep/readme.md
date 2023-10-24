# ML Engineering Foundations

## Project Design

## Data Engineering

## Model Development

## Model Deployment

## Continual Learning

Stacks
A stack is a data structure that contains a collection of elements where you can add and delete elements from just one end (called the top of the stack). In the physical world, a stack can be conceptualized by thinking of plates at a dinner party buffet. When you go to take a plate, you can only remove from the top and similarly when you finish your meal, the stack of plates can only be built by adding them on top of each other — this is exactly what a stack in the software world does.

Stacks are a dynamic data structure that operate on a LIFO (Last In First Out) manner. The last element placed inside is the first element that comes out. The stack supports three operations - push, pop, peek.

Push
Push operation adds an element to the top of the stack, which in dynamic array terms would be appending an element to the end. This is an efficient 
�
(
1
)
O(1) operation as discussed in the previous chapters. It helps to visualize a stack as an array that is vertical. The pseudocode demonstrates the concept, along with the visual where we add numbers from 
1
1 to 
4
4 to the top. The top pointer updates to point at the last item added. The following pseudocode and visual demonstrates this.

def push(self, n):
    # using the pushback function from dynamic arrays to add to the stack
    self.stack.append(n)


Stack, as a data structure, is just an abstract interface and it does not really matter how you implement it - the characteristics are just that you should be able to add and remove elements from the same end.
Since a stack will remove elements in the reverse order that it inserted them in, it can be used to reverse sequences - such as a string, which is just a sequence of characters.
Pop
Pop operation removes the last element from top of the stack, which in dynamic array terms would be retrieving the last element. This is also an efficient 
�
(
1
)
O(1) operation as discussed in the previous chapters. Taking the previous example, let's say we wish to pop 
4
4 and 
5
5. The pseudocode below demonstrates the concept, along with the visual where we remove 
4
4 and 
5
5 from the top. Again, the top pointer updates to point at the last item.

def pop(self):
    return self.stack.pop()


In most languages, before popping, it is a good measure to check if the stack is empty to avoid errors.
Peek
Peek is the simplest of three. It just returns, without removing, the top most element.

def peek(self):
    return self.stack[-1]
Closing Notes
Operation	Big-O Time Complexity	Notes
Push	
�
(
1
)
O(1)	
Pop	
�
(
1
)
O(1)*	Check if the stack is empty first
Peek/Top	
�
(
1
)
O(1)*	Retrieves without removing
