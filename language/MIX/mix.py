#!/usr/bin/env python
#-*- coding:utf-8 -*-

LINE_HALT = 0

class Byte(object):
    pass

class ABL(list):
    @property
    def p(self):
        return self[0]

    @p.setter
    def p(self, value):
        self[0] = value

    @property
    def val(self):
        v = 0
        for i in range(self.length):
            v = v * 64 + self[i + 1]
        if self[0]:
            return v
        else:
            return -v

    @val.setter
    def val(self, v):
        if v > 0:
            self[0] = True
        else:
            self[0] = False
        v = abs(v)
        i = self.length 
        while i > 0:
            self[i] = v % 64
            v = v / 64
            i -= 1


class Address(ABL):
    length = 2
    def __init__(self, l=(False, 0, 0)):
        super(Address, self).__init__(l)

class Char(ABL):
    length = 5
    def __init__(self, l=(False, 0, 0, 0, 0, 0)):
        super(Char, self).__init__(l)


class Compare(object):
    less = -1
    equal = 0
    great = 1

class MIX(object):
    def __init__(self, m, reg, j):
        self.J = j
        self.Memmory = m
        self.Reg = reg
        self.A, self.I1, self.I2, self.I3, self.I4, self.I5, self.I6, self.X = self.Reg

        self.overflow = False
        self.compare = Compare.equal

    @staticmethod
    def load(fr, to, f, p):
        a, b = f / 8, f % 8
        if a == 0:
            if p:
                to.p = fr.p
            else:
                to.p = not fr.p
        else:
            to.p = p
        to[max(a, 1)+to.length-b:to.length+1] = fr[max(a, 1):b+1]

    @staticmethod
    def save(fr, to, f):
        a, b = f / 8, f % 8
        if a == 0:
            to.p = fr.p
        to[max(a, 1):b+1] = fr[max(a, 1)+fr.length-b:fr.length+1]

    def comp(self, reg, m, f):
        if f == 5:
            v = reg.val - m.val
            if v > 0:
                self.compare = Compare.great
            elif v == 0:
                self.compare = Compare.equal
            else:
                self.compare = Compare.less
        else:
            raise NotImplementedError()

    def getM(self, command):
        if command.I == 0:
            return command.A
        else:
            return self.Reg[command.I].val + command.A

    def start_from(self, line):
        print "mix start:"
        while line != LINE_HALT and line in self.Memmory:
            command = self.Memmory[line]
            if DEBUG:
                print line,
                print command.OP, command.ADDRESS,
                print command
            line = self.execute(command)
            if DEBUG:
                self.print_status()

    def print_status(self):
        print "*" * 10, "print_status", "*" * 10
        print "A:", self.A, "X:", self.X, "J:", self.J
        print "I:", 
        for i in range(1, 7):
            print self.Reg[i],
        print ""
        for line, m in self.Memmory.items():
            if not isinstance(m, Command):
                print line, m,
        print ""
        print "*" * 10, "print_status end", "*" * 10

    def execute(self, command):
        if command.C in range(8, 16):
            self.load(self.Memmory[self.getM(command)], self.Reg[command.C - 8], command.F, True)
        elif command.C in range(16, 24):
            self.load(self.Memmory[self.getM(command)], self.Reg[command.C - 16], command.F, False)
        elif command.C in range(24, 32):
            self.save(self.Reg[command.C - 24], self.Memmory[self.getM(command)], command.F)
        elif command.C == 32:
            self.save(self.J, self.Memmory[self.getM(command)], command.F)
        elif command.C == 33:
            self.save(Char(), self.Memmory[self.getM(command)], command.F)
        elif command.C in range(48, 56):
            reg = self.Reg[command.C - 48]
            if command.F == 0:
                reg.val += self.getM(command)
            elif command.F == 1:
                reg.val -= self.getM(command)
            elif command.F == 2:
                reg.val = self.getM(command)
            elif command.F == 3:
                reg.val = - self.getM(command)
        elif command.C == 39:
            if command.F == 0 or \
                    (command.F == 2 and self.overflow) or \
                    (command.F == 3 and not self.overflow) or \
                    (command.F == 4 and self.compare == Compare.less) or \
                    (command.F == 5 and self.compare == Compare.equal) or \
                    (command.F == 6 and self.compare == Compare.great) or \
                    (command.F == 7 and self.compare != Compare.less) or \
                    (command.F == 8 and self.compare != Compare.equal) or \
                    (command.F == 9 and self.compare != Compare.great):
                self.J.val = command.line + 1
                return self.getM(command)
            elif command.F == 1:
                return self.getM(command)
        elif command.C in range(40, 48):
            reg = self.Reg[command.C - 40]
            if (command.F == 0 and reg.val < 0) or \
                    (command.F == 1 and reg.val == 0) or \
                    (command.F == 2 and reg.val > 0) or \
                    (command.F == 3 and reg.val >= 0) or \
                    (command.F == 4 and reg.val != 0) or \
                    (command.F == 5 and reg.val <= 0):
                self.J.val = command.line + 1
                return self.getM(command)
        elif command.C in range(56, 64):
            reg = self.Reg[command.C - 56]
            self.comp(reg, self.Memmory[self.getM(command)], command.F)
        else:
            print command
            raise NotImplementedError()
        return command.line + 1

import re

RLIST = "A123456X"
class Command(Char):
    VADD = lambda k:lambda m:k + RLIST.index(m.group(1))
    CONST = lambda k:lambda m:k
    C = lambda x:x
    LDC = lambda x:5
    LDC2 = lambda x:2
    op_dict = {
        "^LD([A1-6X])$" : (VADD(8), LDC),
        "^LD([A1-6X])N$" : (VADD(16), LDC),
        "^ST([A1-6X])$" : (VADD(24), LDC),
        "^STJ$": (CONST(32), LDC2),
        "^STZ$": (CONST(33), LDC),
        "^ENT([A1-6X])$" : (VADD(48), CONST(2)),
        "^ENN([A1-6X])$" : (VADD(48), CONST(3)),
        "^INC([A1-6X])$" : (VADD(48), CONST(0)),
        "^DEC([A1-6X])$" : (VADD(48), CONST(1)),
        "^CMP([A1-6X])$" : (VADD(56), LDC),
        "^ADD$": (CONST(1), LDC),
        "^SUB$": (CONST(2), LDC),
        "^MUL$": (CONST(3), LDC),
        "^DIV$": (CONST(4), LDC),
        "^JMP$": (CONST(39), CONST(0)),
        "^JSJ$": (CONST(39), CONST(1)),
        "^JOV$": (CONST(39), CONST(2)),
        "^JNOV$": (CONST(39), CONST(3)),
        "^JL$": (CONST(39), CONST(4)),
        "^JE$": (CONST(39), CONST(5)),
        "^JG$": (CONST(39), CONST(6)),
        "^JGE$": (CONST(39), CONST(7)),
        "^JNE$": (CONST(39), CONST(8)),
        "^JLE$": (CONST(39), CONST(9)),
        "^J([A1-6X])N$": (VADD(40), CONST(0)),
        "^J([A1-6X])Z$": (VADD(40), CONST(1)),
        "^J([A1-6X])P$": (VADD(40), CONST(2)),
        "^J([A1-6X])NN$": (VADD(40), CONST(3)),
        "^J([A1-6X])NZ$": (VADD(40), CONST(4)),
        "^J([A1-6X])NP$": (VADD(40), CONST(5)),
        "^SLA$": (CONST(6), CONST(0)),
        "^SRA$": (CONST(6), CONST(1)),
        "^SLAX$": (CONST(6), CONST(2)),
        "^SRAX$": (CONST(6), CONST(3)),
        "^SLC$": (CONST(6), CONST(4)),
        "^SRC$": (CONST(6), CONST(5)),
        "^MOVE$": (CONST(7), C),
        "^NOP$": (CONST(0), CONST(0)),
        "^HLT$": (CONST(5), CONST(2)),
        "^NUM$": (CONST(5), CONST(0)),
        "^CHAR$": (CONST(5), CONST(1)),
        "^IN$": (CONST(36), C),
        "^OUT$": (CONST(37), C),
        "^IOC$": (CONST(35), C),
        "^JRED$": (CONST(38), C),
        "^JBUS$": (CONST(34), C),
    }

    def __init__(self, line, OP, ADDRESS):
        self.line = line
        lst = self.parse(OP, ADDRESS)
        super(Command, self).__init__([True] + list(lst))
        self.OP = OP
        self.ADDRESS = ADDRESS

    @property
    def A(self):
        return self[1] * 64 + self[2]

    @property
    def I(self):
        return self[3]

    @property
    def F(self):
        return self[4]

    @property
    def C(self):
        return self[5]

    def __str__(self):
        #return "{0} : {1} : {2}".format(self.line, self.OP, self.ADDRESS)
        return "{0:5} {1:3} {2} {3:3} {4}".format(self.A, self.I, self.F, self.C, self.OP)

    def parse(self, OP, ADDRESS):
        for op, (getc, getf) in self.op_dict.items():
            match = re.match(op, OP)
            if match:
                if isinstance(ADDRESS, tuple):
                    A, I = ADDRESS
                else:
                    A, I = ADDRESS, 0
                C = getc(match)
                F = getf(ADDRESS)
                print A, I, F, C, OP, ADDRESS
                return A / 64, A % 64, I, F, C


def value(ADDRESS, env, line):
    if ADDRESS == "*":
        return line
    elif ADDRESS.isdigit():
        return int(ADDRESS)
    elif ADDRESS in env:
        return env[ADDRESS]
    elif "," in ADDRESS:
        return tuple(value(ad, env, line) for ad in ADDRESS.split(","))
    elif "+" in ADDRESS:
        return sum(value(ad, env, line) for ad in ADDRESS.split("+"))
    else:
        return ADDRESS

def trans(L):
    env = {}
    line = 0
    L2 = []
    m = {}
    for LOC, OP, ADDRESS in L:
        if OP == 'EQU':
            env[LOC] = value(ADDRESS, env, line)
        elif OP == 'ORIG':
            line = value(ADDRESS, env, line)
        else:
            if LOC:
                env[LOC] = line
            L2.append((line, OP, ADDRESS))
            line += 1
    for line, OP, ADDRESS in L2:
        command = Command(line, OP, value(ADDRESS, env, line))
        m[line] = command
    return m
    print env

import sys
import string

def load_mal():
    if len(sys.argv) == 2:
        f = open(sys.argv[1])
        L = []
        for line in f:
            line = line.rstrip()
            if line.startswith(tuple(string.whitespace)):
                LOC = None
                OP, ADDRESS = line.split(None, 2)
            else:
                LOC, OP, ADDRESS = line.split(None, 3)
            L.append((LOC, OP, ADDRESS))
        return trans(L)

DEBUG = False
def main():
    m = {
        1001:Char((True, 0, 1, 2, 3, 4)),
        1002:Char((True, 0, 2, 1, 3, 4)),
        1003:Char((True, 0, 1, 2, 2, 3)),
        1004:Char((True, 0, 0, 0, 3, 4)),
    }
    m_code = load_mal()
    m.update(m_code)
    reg = [Char(), Address((True, 0, 4)), Address(), Address(), Address(), Address(), Address(), Char()]
    mix = MIX(m, reg, Address())
    mix.start_from(3000)
    mix.print_status()

if __name__ == "__main__":
    main()
