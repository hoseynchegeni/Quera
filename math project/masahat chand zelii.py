from math import tan
pi = 22/7
n_sides = (float(input('enter number of sides ')))
s_lentgh = (float(input('enter lengh of side ')))
erea = (n_sides * s_lentgh ** 2)/(4 * tan(pi / n_sides))
print(erea)
