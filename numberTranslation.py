def blockify(number:str):
    n = len(number)
    remainder = n % 3
    block_size = 3 if remainder == 0 else remainder

    blocks = []
    count = 0
    while count != n:
        num = number[count:count+block_size]
        blocks.append(num)
        count += block_size
        block_size = 3

    blocks.reverse()

    return blocks, len(blocks)

# Up to 9_999_999_999 (billion digit)
def translation(number: str) -> str:
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tenth_sc = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tenth = ["","","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    magnitude_lst = ["", "thousand", "million", "billion"]

    if len(number) > 10:
        print("Too large to handle")
        return None
    if len(number) < 1:
        print("Too few to handle")
        return None
    
    if len(number) == 1:
        return numbers[int(number)]
    
    blocks, blocks_number = blockify(number)

    result = ""
    for i in range(blocks_number - 1, -1, -1):
        current_block = blocks[i]
        current_block = current_block.zfill(3)
        if current_block == "000":
            continue 
        
        hundreds, tens, ones = int(current_block[0]), int(current_block[1]), int(current_block[2])

        # Handling hundreds
        if hundreds:
            result += numbers[hundreds] + " hundred "

        # Handling tens and ones
        if tens:
            if tens == 1:
                result += tenth_sc[ones] + " "
            elif tens > 1:
                result += tenth[tens] + " "
        
        # Handling ones
        if ones:
            result += numbers[ones] + " "
        
        # Add magnitude if not empty
        if magnitude_lst[i]:
            result += magnitude_lst[i] + " "

    # Remove any extra spaces at the end
    return result.strip()

# n = "90_124_145"
# expected = "ninety million one hundred thousand twenty four one hundred forty five "

n = input("Enter a number: ")
# if isinstance(n, str) and n.lower() == "exit":
#     exit()
# try:
#     n = int(n)
#     n = str(n)
# except ValueError:
#     print("Please enter a valid number")
#     n = input("Enter a number: ")

# if n:
result = translation(n)
print(result)


def blockify(number:str):
    n = len(number)
    remainder = n % 3
    block_size = 3 if remainder == 0 else remainder

    blocks = []
    count = 0
    while count != n:
        num = number[count:count+block_size]
        blocks.append(num)
        count += block_size
        block_size = 3

    blocks.reverse()
    return blocks, len(blocks)

n = 90124145
n = str(n)
blocks, size = blockify(n)
print(blocks)