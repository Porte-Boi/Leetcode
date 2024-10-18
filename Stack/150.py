from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        real_nums = []
        for num in tokens:

            if num == "+":
                real_nums.append(real_nums.pop() + real_nums.pop())

            elif num == "-":
                a, b = real_nums.pop(), real_nums.pop()
                real_nums.append(b - a)

            elif num == "*":
                real_nums.append(real_nums.pop() * real_nums.pop())

            elif num == "/":
                a, b = real_nums.pop(), real_nums.pop()
                real_nums.append(int(b / a))

            else:
                real_nums.append(int(num))
                
        return real_nums[0]