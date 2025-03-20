from collections import defaultdict
violators_dict = defaultdict(int)

with open("violator_name.txt", "r") as file:
    for line in file:
        name = line.strip()
        if name:  # Ensure it's not an empty line
            if name in violators_dict:
                violators_dict[name] += 1  # Increment count if name exists
            else:
                violators_dict[name] = 1  # Initialize count if name is new

# Example output of the violators dictionary
print(violators_dict)
print(f"李映稹Helena💜: {violators_dict['李映稹Helena💜']}")
