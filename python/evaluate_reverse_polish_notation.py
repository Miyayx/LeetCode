class Solution:
    # @param tokens, a list of string
    # @return an integer

    def evalRPN(self, tokens):
        op = {
                "+":lambda x,y:x+y,
                "-":lambda x,y:y-x,
                "*":lambda x,y:x*y,
                "/":lambda x,y:int(y*1.0/x)
                }
        a = []
        for t in tokens:
            if t in op.keys():
                a.append(op[t](a.pop(),a.pop()))
            else:
                a.append(int(t))
        return a.pop()

#Accepted

