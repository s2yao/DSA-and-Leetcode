    def compress(chars):
        if (chars == ""): return 0
        posn_to_write = 0
        curr_letter = chars[0]
        curr_count = 1

        for i in range(1, len(chars)):
            if (chars[i] == curr_letter):
                curr_count += 1
            else:
                chars[posn_to_write] = curr_letter
                posn_to_write += 1
                if curr_count > 1:
                    temp = str(curr_count)
                    for digit in temp:
                        chars[posn_to_write] = digit
                        posn_to_write += 1
                curr_letter = chars[i]
                curr_count = 1
        
        chars[posn_to_write] = curr_letter
        posn_to_write += 1
        if curr_count > 1:
            temp = str(curr_count)
            for digit in temp:
                chars[posn_to_write] = digit
                posn_to_write += 1
        
        return posn_to_write


chars = ["a"]
nigger = compress(chars)
print(nigger)
print("fuck you")
for i in range(nigger):
    print(chars[i])