def convert(w):
    for c in w:
        if c in "aoieu":
            w = w.replace(c,"")
    return w

word = input("Input: ")
word = convert(word)
print("Output:",word)