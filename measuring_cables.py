
def classify(cable_length):
    if cable_length < 48:
        return "Below range"
    elif cable_length <= 52:
        return "In range"
    else:
        return "Above range"

def calculate_average(total, count):
    return total / count



num_cables = int(input("Enter the number of cables: "))

total_length = 0
below_count = 0
in_count = 0
above_count = 0



for i in range(num_cables):
    length = int(input("Enter the cable length: "))
    
    classification = classify(length)
    print(classification)
    
    total_length += length
    
    if classification == "Below range":
        below_count += 1
    elif classification == "In range":
        in_count += 1
    elif classification == "Above range":
        above_count += 1



average_length = calculate_average(total_length, num_cables)

print(f"Total length: {total_length} cm")
print(f"Average length: {average_length:.1f} cm")
print(f"Below range: {below_count}")
print(f"In range: {in_count}")
print(f"Above range: {above_count}")
