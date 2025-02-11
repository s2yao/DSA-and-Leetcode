def solution(paragraphs, width):
    result = ["*" * (width + 2)]
    
    for paragraph in paragraphs:
        current_line_chunks = []
        current_line_length = 0
        
        for chunk in paragraph:
            chunk_len = len(chunk)
            space_needed = chunk_len + (1 if current_line_chunks else 0)
            
            if current_line_length + space_needed <= width:
                current_line_chunks.append(chunk)
                current_line_length += space_needed
            else:
                line_str = " ".join(current_line_chunks)
                leftover = width - len(line_str)
                
                if leftover % 2 == 0:
                    left_spaces = right_spaces = leftover // 2
                else:
                    left_spaces = leftover // 2
                    right_spaces = leftover // 2 + 1

                result.append(
                    "*" + (" " * left_spaces) + line_str + (" " * right_spaces) + "*"
                )
                
                current_line_chunks = [chunk]
                current_line_length = chunk_len

        if current_line_chunks:
            line_str = " ".join(current_line_chunks)
            leftover = width - len(line_str)
            if leftover % 2 == 0:
                left_spaces = right_spaces = leftover // 2
            else:
                left_spaces = leftover // 2
                right_spaces = leftover // 2 + 1
            
            result.append(
                "*" + (" " * left_spaces) + line_str + (" " * right_spaces) + "*"
            )

    result.append("*" * (width + 2))
    
    return result

            
            





paragraphs = [
    ["How", "areYou", "doing"],
    ["Please", "fit", "on", "two", "lines"]
]
width = 16
print(solution(paragraphs, width))