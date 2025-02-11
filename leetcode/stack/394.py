class Solution:
    def decodeString(s: str):
        stack = []
        curr_mult = 0
        curr_str = ""

        for c in s:
            if c.isdigit():
                curr_mult = curr_mult * 10 + int(c)
            elif c == "[":
                stack.append(curr_str)
                stack.append(curr_mult)
                curr_mult = 0
                curr_str = ""
            elif c == "]":
                stored_len = stack.pop(-1)
                stored_str = stack.pop(-1)
                curr_str = stored_str + stored_len * curr_str
            else:
                curr_str += c
        
        return curr_str



s = "2[abc]3[cd]ef"
print(Solution.decodeString(s))