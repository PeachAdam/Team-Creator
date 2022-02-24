# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    skimoc_4v4_takim_kurma.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yaysu <yaysu@student.42istanbul.com.tr>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/25 13:49:18 by yaysu             #+#    #+#              #
#    Updated: 2022/01/25 14:03:11 by yaysu            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

#list = ['yusuf', 'ooz  ', 'kermi', 'ergey', 'berge', 'merd ', 'sebo ', 'emo  ']

i = 0
j = 1
u = 0
list = ['', '', '', '', '', '', '', '']
while i != 8:
    k = str(input("oyuncu " + str(j) +":"))
    list[u] = str(k)
    i = i + 1
    j = j + 1
    u = u + 1  

o1 = random.randrange(1,9)
o2 = random.randrange(1,9)
o3 = random.randrange(1,9)
o4 = random.randrange(1,9)

while o2:
    o2 = random.randrange(1,9)
    if (o1 != o2):
        break
while o3:
    o3 = random.randrange(1,9)
    if (o1 != o3) and (o2 != o3):
        break
while o4:
    o4 = random.randrange(1,9)
    if (o1 != o4) and (o2 != o4) and (o3 != o4):
        break

blue_team = [list[o1-1], list[o2-1], list[o3-1], list[o4-1]]

list_of_num = [o1-1, o2-1, o3-1, o4-1]
list_of_num.sort(reverse=True)

a1 = list_of_num[0]
a2 = list_of_num[1]
a3 = list_of_num[2]
a4 = list_of_num[3]

list.pop(a1)
list.pop(a2)
list.pop(a3)
list.pop(a4)  

print("Mavi Takım --- Kırmızı Takım")
print(blue_team[0] + "      ---  " + list[0])
print(blue_team[1] + "      ---  " + list[1])
print(blue_team[2] + "      ---  " + list[2])
print(blue_team[3] + "      ---  " + list[3])
