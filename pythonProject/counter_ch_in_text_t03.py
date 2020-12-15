def text_analyzer(argv):
    counter = [0, 0, 0, 0]

    for i in (str(argv)):
        if i.isupper():
            counter[0] += 1
        elif i.islower():
            counter[1] += 1
        elif i == '.' or i == ',':
            counter[2] += 1
        elif i == ' ':
            counter[3] += 1
    print("ch = ", len(argv))
    print("ch(up) = ", counter[0])
    print("ch(low) =", counter[1])
    print("ch(mark) = ", counter[2])
    print("ch(space) = ", counter[3])