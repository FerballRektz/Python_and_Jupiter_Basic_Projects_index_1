
import math as mh


hx = -(9/14)*mh.log(9/14,2)-(5/14)*mh.log(5/14,2)

# information gain off humidity 
hhum = (7/14)*(-(3/7)*mh.log(3/7,2)-(4/7)*mh.log(4/7,2)) + (7/14)*(-(6/7)*mh.log(6/7,2)-(1/7)*mh.log(1/7,2)) 
humfin = hx - hhum
print(f'the value of gain(humidity) is: {round(humfin,3)}')


# information gain of wind 
hwind = (8/14)*(-(6/8)*mh.log(6/8,2)-(2/8)*mh.log(2/8,2)) + (6/14)*(-(3/6)*mh.log(3/6,2)-(3/6)*mh.log(3/6,2)) 
winfin = hx - hwind 
print(f'the value of gain(wind) is: {round(winfin,3)}')



# information gain of heat
humheat = (4/14)*(-(2/4)*mh.log(2/4,2)-(2/4)*mh.log(2/4,2)) + (6/14)*(-(4/6)*mh.log(4/6,2)-(2/6)*mh.log(2/6,2)) + (4/14)*(-(3/4)*mh.log(3/4,2)-(1/4)*mh.log(1/4,2))
heatf = hx - humheat
print(f'the value of gain(wind) is: {round(heatf,3)}')