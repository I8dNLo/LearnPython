l = list(range(2, 8))
print([i for i in l])

l.append('Python')
print(len(l))

print(l[0])
print(l[-1])

print([l[i] for i in range(2, 5)])
l.pop()
