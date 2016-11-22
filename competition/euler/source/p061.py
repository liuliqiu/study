##Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are
##all figurate (polygonal) numbers and are generated by the following formulae:
##
##Triangle	 	P3,n=n*(n+1)/2	 	1, 3, 6, 10, 15, ...
##Square	 	P4,n=n^2	 	1, 4, 9, 16, 25, ...
##Pentagonal	 	P5,n=n*(3n-1)/2	 	1, 5, 12, 22, 35, ...
##Hexagonal	 	P6,n=n*(2n-1)	 	1, 6, 15, 28, 45, ...
##Heptagonal	 	P7,n=n*(5n-3)/2	 	1, 7, 18, 34, 55, ...
##Octagonal	 	P8,n=n*(3n-2)	 	1, 8, 21, 40, 65, ...
##The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three
##interesting properties.
##
##The set is cyclic, in that the last two digits of each number is the first two
##digits of the next number (including the last number with the first).
##Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and
##pentagonal (P5,44=2882), is represented by a different number in the set.
##This is the only set of 4-digit numbers with this property.
##Find the sum of the only ordered set of six cyclic 4-digit numbers for which
##each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and
##octagonal, is represented by a different number in the set.

def P(a):
    return lambda n:(n*((a-2)*n-(a-4)))>>1
def All():
    return [[str(P(a)(i)) for i in range(150) if 1000<P(a)(i)<10000 and str(P(a)(i))[2]!='0'] for a in range(3,9)]
def fi():
    v=All()
    z=[[i,5]for i in v[5]]
    s=[]
    for t in range(5):
        for i in range(5):
            for j in v[i]:
                for k in z:
                    if i not in k and k[0][:2]==j[2:]:
                        temp=k[:]
                        temp[0]=j[:2]+temp[0]
                        temp.append(i)
                        s.append(temp)
        z=s
        s=[]
    for i in z:
        if i[0][:2]==i[0][-2:]:
            print(i[0])
            return sum(int(i[0][2*j:2*j+2]) for j in range(6))*101
print(fi())