class Solution:
    def decodeString(self, s):
        # There is always a "[" and "]"
        # Use it as a benchmark

        # s = "3[a]2[bc]"
        # aaabcbc
        # we need a stack
        # ]: we multiply the current string in the temp_str and mult it by the number before it
        # then we "".join(stack)

        # s = "3[a2[c]]"
        # We need to both the repetition and the current built characters into stack
        # if number: we add to the temp_number
        # [: we record the current number, current string
        # ]: we pop the stored number, stored string, then we append the:  stored_string + stored_number * temp_string
        # remember to reset
        # make sure to add the left over temp_string

        # s = "2[abc]3[cd]ef"
        
        StackNumStr = []
        curr_str = ''
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == "[":
                # record, number first and string next
                StackNumStr.append(curr_num)
                StackNumStr.append(curr_str)
                # we are ready to record new character and number
                curr_str = ''
                curr_num = 0
            elif char == "]":
                stored_str = StackNumStr.pop()
                stored_int = StackNumStr.pop()
                curr_str = stored_str + stored_int * curr_str  # since "[" has to happen before every ']'
            else:  # if it's a character
                curr_str += char

        return curr_str