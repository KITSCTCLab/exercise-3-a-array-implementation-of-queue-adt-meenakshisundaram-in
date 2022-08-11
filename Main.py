class Solution:
    """This class implements linear queue.
      Attributes:
          stack: A list which maintains the content of stack.
          queue: A list which maintains the content of queue.
          top: An integer which denotes the index of the element at the top of the stack.
          front: An integer which denotes the index of the element at the front of the queue.
          rear: An integer which denotes the index of the element at the rear of the queue.
          size: An integer which represents the size of stack and queue.
      """

    # Write your code here
    def __init__(self, size):
        """Inits Solution with stack, queue, size, top, front and rear.
        Arguments:
          size: An integer to set the size of stack and queue.
        """
        self.stack = []
        self.queue = []
        self.size = size
        self.top = -1
        self.rear = -1
        self.front = -1

    def is_stack_empty(self): 
        """
        Check whether the stack is empty.
        Returns:
          True if it is empty, else returns False.
        """
        # Write your code here
        if self.top==-1:
            return True
        else:
            return False

    def is_queue_empty(self):
        """
        Check whether the queue is empty.
        Returns:
          True if it is empty, else returns False.
        """
        # Write your code here
        if self.rear == self.top == -1:
            return True
        else:
            return False

    def is_stack_full(self):
        """
        Check whether the stack is full.
        Returns:
          True if it is full, else returns False.
        """
        # Write your code here
        if len(self.stack)==self.size:
            return True
        else:
            return False

    def is_queue_full(self):
        """
        Check whether the queue is full.
        Returns:
          True if it is full, else returns False.
        """
        # Write your code here
        if self.rear==(self.size-1):
            return True
        else:
            return False


    def push_character(self, character):
        """
        Push the character to stack, if stack is not full.
        Arguments:
            character: A character that will be pushed to the stack.
        """
        # Write your code here
        if self.is_stack_full()==False:
            self.stack.append(character)
            self.top+=1

    def enqueue_character(self, character):
        """
        Enqueue the character to queue, if queue is not full.
        Arguments:
            character: A character that will be enqueued to queue.
        """
        # Write your code here
        if self.is_queue_full()==False:
            self.queue.append(character)

    def pop_character(self):
        """
        Do pop operation if the stack is not empty.
        Returns:
          The data that is popped out if the stack is not empty.
        """
        # Write your code here
        if self.is_stack_empty()==False:
            data = self.stack.pop()
            self.top-=1
            return data

    def dequeue_character(self):
        """
        Do dequeue operation if the queue is not empty.
        Returns:
          The data that is dequeued if the queue is not empty.
        """
        # Write your code here
        if self.is_queue_empty()==False:
            data_= self.queue.pop(0)
            return data_


# read the string text
text = input()

# find the length of text
length_of_text = len(text)

if len(text)%2==0:
    c = len(text)
else:
    c = (len(text)//2)+1

# Create the Solution class object
solution = Solution(length_of_text)

# push/enqueue all the characters of string text to stack
for char in text:
    solution.push_character(char)
    solution.enqueue_character(char)

is_palindrome = False
'''
pop the top character from stack
dequeue the first character from queue
compare both characters
If the comparison fails, set is_palindrome as False.
'''
# Write the necessary logic
for x in range(c):
    a=solution.pop_character()
    b=solution.dequeue_character()

    if a==b:
        is_palindrome=True
    else:
        is_palindrome=False
        break
# finally print whether string text is palindrome or not.
if is_palindrome:
    print("The word, " + text + ", is a palindrome.")
else:
    print("The word, " + text + ", is not a palindrome.")
