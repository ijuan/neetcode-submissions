
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rpn = []
        for i in tokens:
            if i == "+":
                b = rpn.pop()
                a = rpn.pop()
                rpn.append(int(a) + int(b))
            elif i == "-":
                b = rpn.pop()
                a = rpn.pop()
                rpn.append(int(a) - int(b))
            elif i == "*":
                b = rpn.pop()
                a = rpn.pop()
                rpn.append(int(a) * int(b))
            elif i == "/":
                b = rpn.pop()
                a = rpn.pop()
                rpn.append(int(int(a) / int(b)))
            else:
                rpn.append(int(i))
        return rpn.pop()

        