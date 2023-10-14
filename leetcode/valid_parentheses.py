class Solution:
    def isValid(s: str) -> bool:
        stack = []
        # Dictionary to hold the mapping of open and close brackets
        bracket_mapping = {')': '(', '}': '{', ']': '['}
        
        # Iterate through the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_mapping:
                # Pop the top element from stack if it's not empty; otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the corresponding opening bracket
                if bracket_mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, then the brackets were balanced
        return not stack

# Test cases
print(Solution.isValid("()"))  # Output: True
print(Solution.isValid("()[]{}"))  # Output: True
print(Solution.isValid("(]"))  # Output: False
