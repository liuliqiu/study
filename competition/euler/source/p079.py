##A common security method used for online banking is to ask the user for three
##random characters from a passcode. For example, if the passcode was 531278,
##they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be:
##317.
##The text file, keylog.txt, contains fifty successful login attempts.
##Given that the three characters are always asked for in order, analyse the
##file so as to determine the shortest possible secret passcode of unknown length.


def fi():
    f = open("txt\\keylog.txt")
    v = {}
    for s in f.readlines():
        s = s.strip()
        if s != "":
            for i, c in enumerate(s):
                for j in range(i + 1, len(s)):
                    if c in v:
                        v[c].append(s[j])
                    else:
                        v[c] = [s[j]]
    for i in v:
        v[i] = set(v[i])
    print(v)


fi()
