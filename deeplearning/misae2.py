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
# 2021 2.8%              # 6.0%               #2018

#공식 lnEXP = -0.001 +4.32lnGDPk +3.32lnGDPc
#GDPk : korea GDP 증가율 GDPc: china GDP 증가율
#EXP = 미세먼지 농도 증가율 

GDP = [(2.3,7.9),(2.9,7.8), (3.3,7.3), (2.8,6.9), (2.8,6.7), (3.1,6.9),(3.0,6.6)]

expP = {}
count = 12
y1 = []
y2 = [49.9, 48.9, 47.5, 46]

for (k,c) in GDP :
        expP[count]=round(-0.001 +4.32*math.log(k)+3.32*math.log(c),2)
        print(str(count)+":"+str(expP[count]))
        count = count+1

        

count = 0
for c in range(14,18):
        if(expP[c]>expP[c+1]):
                if(c==14):
                        y1.append(60 * (1-(expP[c]/100)))
                else:
                        y1.append(y1[count] * (1-(expP[c]/100)))
                        count = count+1;
        else:
                if(c==14):
                        y1.append(60 * (1+(expP[c]/100)))
                else:
                        y1.append(y1[count] * (1+(expP[c]/100)))
                        count = count+1;
                        
x = [2014, 2015, 2016, 2017]

plt.plot(x,y1)
plt.plot(x,y2)

plt.show()

