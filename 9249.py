long_string = input()
string = input()
# print(len(string))
dict = {}
length = []
for i in range(len(string)):
    for j in range(i, len(string)):
        a = string[i:j+1]
        if a in long_string:
            dict[len(a)] = a
            length.append(len(a))
            # array.append({len(a): a})
l = max(length)
print(l)
print(dict[l])

