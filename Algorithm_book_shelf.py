from collections import deque

# Read the number of instructions
num_instructions = int(input())

# Initialize a deque to represent the bookshelf
bookshelf = deque()

# Process each instruction
for _ in range(num_instructions):
    instruction = input().split()
    action, book_id = instruction[0], int(instruction[1])
    
    if action == 'L':
        # Place the book to the left of the leftmost existing book
        bookshelf.appendleft(book_id)
    elif action == 'R':
        # Place the book to the right of the rightmost existing book
        bookshelf.append(book_id)
    elif action == '?':
        # Calculate the minimum number of books to pop from both sides
        left_count = bookshelf.index(book_id)
        right_count = len(bookshelf) - left_count - 1
        # Print the result
        print(min(left_count, right_count))


''' 2---> According to LLM Chatbot tool :

To analyze the time complexity of the provided code, we can break it down into its main operations:

Looping through the boss's instructions: This operation takes O(n) time, where 'n' is the number of instructions.
For each instruction, we perform the following operations:
For 'L' or 'R' instructions, we append to the deque, which takes O(1) time.
For '?' instructions, we use the index method to find the position of the book, which takes O(k) time, where 'k' is the position of the book in the deque. 
In the worst case, 'k' could be equal to the length of the deque, making it O(n).
Printing the result in each '?' instruction takes O(1) time.

Given these considerations, the overall time complexity of the code is O(n^2) in the worst case, 
as the worst-case scenario occurs when each '?' instruction has to search through the entire deque, and there are 'n' such instructions.
'''

'''We believe the instructions given by the LLM Chatbot tool is correct and 
upon observation with different input sizes  we can see that the most expensive operation in the code is to calculate the ? instructions.'''

''' NO the code provided above is not the optimal code , we can reduce the time complexity of the above code by using a different data structure called dictionary. The time complexity for it can be reduced to O(n)
    
    Algorithm: 

    Initialize an empty dictionary called book_positions
Initialize an empty list called bookshelf

Read num_instructions

For i in range(num_instructions):
    Parse the instruction into action and book_id
    
    If action is 'L':
        Insert book_id at the beginning of bookshelf
        Store the position of book_id in book_positions
    
    If action is 'R':
        Append book_id to the end of bookshelf
        Store the position of book_id in book_positions
    
    If action is '?':
        Retrieve book_id's position from book_positions
        Calculate left_count as min(book_id's position, length of bookshelf - book_id's position - 1)
        Print left_count


efficient O(1) time complexity for the '?' instructions.
'''

