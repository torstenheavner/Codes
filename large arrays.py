array = [[[[[[[[x for x in range(3)] for y in range(3)] for z in range(3)] for w in range(3)] for v in range(3)] for q
           in range(3)] for p in range(3)] for o in range(3)]

i = 0

for o in array:
    for p in o:
        for q in p:
            for v in p:
                for w in v:
                    for z in w:
                        for y in z:
                            for x in y:
                                i += 1
                                print(x)
                                print(i)
