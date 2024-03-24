def allvariants(s):
    for length in range(1, len(s) + 1):
        for i in range(len(s) - length + 1):
            yield s[i:i+length]

a = allvariants("abc")
for i in a:
    print(i)