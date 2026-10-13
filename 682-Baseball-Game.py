class Solution:
    def calPoints(self, operations: list[str]) -> int:
        ans = []
        for operation in operations:
            match (operation):
                case "+":
                    ans.append(ans[-1] + ans[-2])
                case "D":
                    ans.append(ans[-1] * 2)
                case "C":
                    ans.remove(ans[-1])
                case _:
                    ans.append(int(operation))
        return sum(ans)

# In this soliution, we use a stack/array to keep track of scores
# We add new scores based on the operatoin rules and whatever is in the top of the stack
# In our default case, we convert the string of the score to an integer
# We add the sum of the stack to get our total score