# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:44:06 2020

@author: Dallin
"""

import numpy as np
import matplotlib.pyplot as plt

degree_sign= u'\N{DEGREE SIGN}'

# Create some mock data
t650 = (650,650,650,650,650,650,650,650,650,650,650,650,650,650,650)
t650h = (504,
528,
532,
545,
553,
558,
609,
623,
636,
651,
654,
654,
656,
670,
504)



t650ys = (1647.5172,
1725.9704,
1739.04593,
1781.54142,
1807.69248,
1824.0369,
1990.74995,
2036.51432,
2079.0098,
2128.04305,
2137.8497,
2137.8497,
2144.38747,
2190.15183,
1647.5172)
# data1 = np.exp(t)
# data2 = np.sin(2 * np.pi * t)

t950 = (950,
950,
950,
950,
950,
950,
950,
950,
950,
950,
950,
950,
950,
950,
950,
950,
950,
950)

t950h = (237,
239,
239,
259,
262,
266,
269,
273,
314,
321,
321,
322,
325,
340,
345,
350,
297,
300)

t950ys = (774.72535,
781.26312,
781.26312,
846.64078,
856.44743,
869.52297,
879.32962,
892.40515,
1026.42937,
1049.31155,
1049.31155,
1052.58043,
1062.38708,
1111.42033,
1127.76475,
1144.10917,
970.85835,
980.665)


hallpetchx = (650,650,950,950)
hallpetchy = (1897,654,629,547)

hallpetchxh = (650,650,950,950)
hallpetchyh = (580.3204968, 200.068321, 192.4204494, 167.3354305)

orowonx = (650,950)
orowony = (1157,374)
orowonyh = (354,115)

taylorx = (650,950)
tayloryys = (114,55)
tayloryh = (35,17)

dummypointx = (650)
dummypointh = (701)
dummypointys = (2295)

dummypointlowh = (64.2)
dummypointlowys = (190)  

fig, ax1 = plt.subplots()



font = {'family': 'serif',
        'color':  'black',
        'weight': 'bold',
        'size': 20,
        }

colorblack = 'xkcd:black'
ax1.set_xlabel('Temperature (\u2103)', fontdict = font)
plt.xticks(fontsize=17, fontweight = 'bold')
plt.yticks(fontsize=17)
ax1.set_ylabel('Hardness (HV 0.3)', fontdict = font)
ax1.scatter(t650, t650h, color=colorblack)
ax1.scatter(t950, t950h, color=colorblack)
ax1.scatter(hallpetchxh, hallpetchyh,color=colorblack, s = 150, marker = 'x' )
ax1.scatter(orowonx,orowonyh, color = colorblack, s = 150, marker = '+')
ax1.scatter(taylorx,tayloryh, color = colorblack, s = 100, marker = '3')
ax1.scatter(dummypointx, dummypointh, color = 'white')
# ax1.scatter(dummypointx, dummypointlowh, color = 'white')


ax1.tick_params(axis='y', labelcolor=colorblack)
plt.yticks(fontsize=17, fontweight = 'bold')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

fontright = {'family': 'serif',
        'color':  'black',
        'weight': 'bold',
        'size': 20,
        }

colordb = 'xkcd:darkblue'
ax2.set_ylabel('Yield Strength (MPa)', fontdict = fontright)  # we already handled the x-label with ax1
ax2.scatter(t650, t650ys, color=colorblack)
ax2.scatter(t950, t950ys, color=colorblack)
ax2.scatter(hallpetchx, hallpetchy, color=colorblack, s = 150, marker = 'x' )
ax2.scatter(orowonx, orowony, color = colorblack, s = 150, marker = '+')
ax2.scatter(taylorx,tayloryys, color = colorblack, s = 100, marker = '3')
ax2.scatter(dummypointx,dummypointys, color = 'white')
# ax2.scatter(dummypointx, dummypointlowys, color = 'white')
ax2.tick_params(axis='y', labelcolor=colordb)
plt.yticks(fontsize=17, fontweight = 'bold')



fig, ax3 = plt.subplots()


ax3.set_xlabel('Temperature (\u2103)', fontdict = font)
plt.xticks(fontsize=17, fontweight = 'bold')
plt.yticks(fontsize=17)
ax3.set_ylabel('Hardness (HV 0.3)', fontdict = font)
ax3.scatter(t650, t650h, color=colorblack)
ax3.scatter(t950, t950h, color=colorblack)
ax3.scatter(hallpetchxh, hallpetchyh,color=colorblack, s = 150, marker = 'x' )
ax3.scatter(orowonx,orowonyh, color = colorblack, s = 150, marker = '+')
ax3.scatter(taylorx,tayloryh, color = colorblack, s = 100, marker = '3')
ax3.scatter(dummypointx, dummypointh, color = 'white')
# ax1.scatter(dummypointx, dummypointlowh, color = 'white')


ax3.tick_params(axis='y', labelcolor=colorblack)
plt.yticks(fontsize=17, fontweight = 'bold')

ax4 = ax3.twinx()  # instantiate a second axes that shares the same x-axis

fontright = {'family': 'serif',
        'color':  'black',
        'weight': 'bold',
        'size': 20,
        }

colordb = 'xkcd:black'
ax4.set_ylabel('Yield Strength (MPa)', fontdict = fontright)  # we already handled the x-label with ax1
ax4.scatter(t650, t650ys, color=colorblack)
ax4.scatter(t950, t950ys, color=colorblack)
ax4.scatter(hallpetchx, hallpetchy, color=colorblack, s = 150, marker = 'x' )
ax4.scatter(orowonx, orowony, color = colorblack, s = 150, marker = '+')
ax4.scatter(taylorx,tayloryys, color = colorblack, s = 100, marker = '3')
ax4.scatter(dummypointx,dummypointys, color = 'white')
# ax2.scatter(dummypointx, dummypointlowys, color = 'white')
ax4.tick_params(axis='y', labelcolor=colordb)
plt.yticks(fontsize=17, fontweight = 'bold')

























# 

# # hide the spines between ax and ax2
# ax1.spines['bottom'].set_visible(False)
# ax2.spines['top'].set_visible(False)
# # ax.xaxis.tick_top()
# ax1.tick_params(labeltop=False)  # don't put tick labels at the top
# # ax2.xaxis.tick_bottom()








fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()


# # -*- coding: utf-8 -*-
# """
# Spyder Editor

# This is a temporary script file.
# """

