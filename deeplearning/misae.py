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
