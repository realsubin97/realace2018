<<<<<<< HEAD
from matplotlib import pyplot as plt
import math
# 한국 GDP 상승률        #중국 GDP 상승률     #미세먼지평균
# 2012 2.3%              # 7.9%               #2012 40.3
# 2013 2.9%              # 7.8%               #2013 60.0
# 2014 3.3%              # 7.3%               #2014 49.9
# 2015 2.8%              # 6.9%               #2015 48.9
# 2016 2.8%              # 6.7%               #2016 47.5
# 2017 3.1%              # 6.9%               #2017 46


pm12 = (-0.001 + 4.32*math.log(2.3) + 3.32*math.log(7.9))
pm13 = (-0.001 + 4.32*math.log(2.9) + 3.32*math.log(7.8))
pm14 = (-0.001 + 4.32*math.log(3.3) + 3.32*math.log(7.3))
pm15 = (-0.001 + 4.32*math.log(2.8) + 3.32*math.log(6.9))
pm16 = (-0.001 + 4.32*math.log(2.8) + 3.32*math.log(6.7))
pm17 = (-0.001 + 4.32*math.log(3.1) + 3.32*math.log(6.9))

x = [2011, 2012, 2013, 2014, 2015, 2016]
y = [pm12,pm13,pm14,pm15,pm16, pm17]

plt.xlabel('year')
plt.ylabel('pm25')
plt.plot(x,y)

plt.show()
=======
from matplotlib import pyplot as plt
import math
# 한국 GDP 상승률        #중국 GDP 상승률     #미세먼지평균
# 2012 2.3%              # 7.9%               #2012 40.3
# 2013 2.9%              # 7.8%               #2013 60.0
# 2014 3.3%              # 7.3%               #2014 49.9
# 2015 2.8%              # 6.9%               #2015 48.9
# 2016 2.8%              # 6.7%               #2016 47.5
# 2017 3.1%              # 6.9%               #2017 46
# 2018 3.0%              # 6.6%               #2018
# 2019 2.9%              # 6.4%               #2019
# 2020 2.8%              # 6.3%               #2020
# 2021 2.8%              # 6.0%               #2021

#공식 lnEXP = -0.001 +4.32lnGDPk +3.32lnGDPc
#GDPk : korea GDP 증가율 GDPc: china GDP 증가율
#EXP = 미세먼지 농도 증가율
#기준이 될 미세먼지 평균 2012년의 40.3 , 0.96 9.6 - >78.988
# 

GDP = [(2.3,7.9),(2.9,7.8), (3.3,7.3), (2.8,6.9), (2.8,6.7), (3.1,6.9),(3.0,6.6),(2.9,6.4),(2.8,6.3),(2.8,6.0)]

expP = {}
count = 12
y1 = []

sta = 40.3

for (k,c) in GDP :
        expP[count]=round(-0.001 +4.32*math.log(k)+3.32*math.log(c),2)
        print(str(count)+":"+str(expP[count]))
        count = count+1


y1.append(49.9)
y1.append(48.9)
y1.append(47.5)
y1.append(46)

count = 4
for c in range(18,21):
        if(expP[c]>expP[c+1]):
                if(c==18):
                        y1.append(46 * (1-(expP[c]/100)))
                else:
                        y1.append(y1[count] * (1-(expP[c]/100)))
                        count = count+1;
        else:
                if(c==18):
                        y1.append(46 * (1+(expP[c]/100)))
                else:
                        y1.append(y1[count] * (1+(expP[c]/100)))
                        count = count+1;

print(y1)

x = [2014, 2015, 2016, 2017, 2018,2019,2020]

plt.ylim(20,70)
plt.plot(x,y1)
plt.show()

>>>>>>> deeplearning
