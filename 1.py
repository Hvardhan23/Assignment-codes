def compress(s):
    compressed = ""
    count = 0
    for i in range(len(s)):
        count += 1
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compressed += s[i] + str(count)
            count = 0
    return compressed

# taking output of compress function as input
def secondtime_compress(s):
    compressed = ""
    count = 0
    prev_char = s[0]
    for char in s:
        if char == prev_char:
            count += 1
        else:
            compressed += prev_char
            if count > 1:
                compressed += str(count)
            prev_char = char
            count = 1
    compressed += prev_char
    if count > 1:
        compressed += str(count)
    return compressed

def decompress(s):
    decompressed = ""
    for i in range(len(s)):
        if s[i].isdigit():
            count = int(s[i])
            decompressed += s[i-1] * (count - 1)
        else:
            decompressed += s[i]
    return decompressed

def test(input_str):
    print("Input:", input_str)
    compressed = compress(input_str)
    print("Compressed:", compressed)
    secondtime_compressed = secondtime_compress(compressed)
    print("Second time Compressed:", secondtime_compressed)
    decompressed = decompress(secondtime_compressed)
    print("Decompressed:", decompressed)

if __name__ == "__main__":
    test("aabcccccaaa")  # Expected: a2b1c5a3
    
