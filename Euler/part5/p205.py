##Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
##Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
##
##Peter and Colin roll their dice and compare totals: the highest total wins. The
##result is a draw if the totals are equal.
##
##What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer
##rounded to seven decimal places in the form 0.abcdefg

from itertools import product,groupby
def P(l,re):
    result={}
    for  i in [sum(i) for i in product(l,repeat=re)]:
        if i not in result:
            result[i]=1
        else:
            result[i]=result[i]+1
    return result
    
def p205():
    Peter=P([1,2,3,4],9)
    Colin=P([1,2,3,4,5,6],6)
    result=0
    for i in Peter:
        for j in Colin:
            if j<i:
                result=result+Peter[i]*Colin[j]
    return result/((4**9)*(6**6))
print(p205())
