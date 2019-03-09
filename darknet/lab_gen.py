ls = []
i = 0
while i < 415:
    ls.append(i)
    i += 2
while i < 2322:
    ls.append(i)
    i += 8
with open('test.txt', 'w') as wf:
    for i in range(0, 2322):
        if i in ls:
            pass
        else:
            wf.write(str(i)+'.jpg\n')
