class Stack:
    def __init__(self):
        self.lst = []

    def is_empty(self):
        if len(self.lst) == 0:
            return True
        else:
            return False

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        if self.is_empty():
            # We don't have to write else after this line because when an exception
            # is thrown, we don't continue to the lines after it - we stop the functions
            # and bubble up the exception until it stops at a relevant try-except or block
            # shuts down the program.

            raise ValueError('The stack is empty, you cannot pop item.')
        # # lst.pop removes the las item from the list and returns it to the caller..
        # y = self.lst.pop()

        # Second alternative
        # Getting the last item from the list.
        y = self.lst[-1]
        # Deleting the last item from the list.
        del self.lst[-1]
        return y

    def top(self):
        if self.is_empty():
            raise Exception('The stack is empty, you cannot top item.')
        return self.lst[-1]


# Creating object of type stack and using it.
stack1 = Stack()

for i in range(1, 5):
    stack1.push(i)

for i in range(1, 5):
    print(stack1.pop())
try:
    print(stack1.pop())
except:
    print('The stack is empty...')


# Accepts equation and returns True if valid brackets else False.
def is_valid_brackets(equation):
    stack = Stack()
    for letter in equation:
        if letter == '(':
            stack.push('(')
        elif letter == ')':
            try:
                stack.pop()
            except ValueError:
                # Im going to enter this except if the stack was empty.
                # and therefore the equation is not valid!
                return False

    return stack.is_empty()


# print(is_valid_brackets('(1+5)+(3+4)'))

print(is_valid_brackets('(()'))
