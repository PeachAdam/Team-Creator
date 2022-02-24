# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    skimoc_5v5_takim_kurma(inputlu).py                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yaysu <yaysu@student.42istanbul.com.tr>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/27 11:38:07 by yaysu             #+#    #+#              #
#    Updated: 2022/01/27 11:38:12 by yaysu            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

#list = ['yusuf', 'ooz  ', 'kermi', 'ergey', 'berge', 'merd ', 'sebo ', 'emo  ', 'emirh', 'emre ']

i = 0
j = 1
u = 0
list = ['', '', '', '', '', '', '', '', '', '']
while i != 10:
    k = str(input("oyuncu " + str(j) +":"))
    list[u] = str(k)
    i = i + 1
    j = j + 1
    u = u + 1  

o1 = random.randrange(1,9)
o2 = random.randrange(1,9)
o3 = random.randrange(1,9)
o4 = random.randrange(1,9)
o5 = random.randrange(1,9)

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
while o5:
    o5 = random.randrange(1,9)
    if (o1 != o5) and (o2 != o5) and (o3 != o5) and (o4 != o5):
        break
    

blue_team = [list[o1-1], list[o2-1], list[o3-1], list[o4-1], list[o5-1]]

list_of_num = [o1-1, o2-1, o3-1, o4-1, o5-1]
list_of_num.sort(reverse=True)

a1 = list_of_num[0]
a2 = list_of_num[1]
a3 = list_of_num[2]
a4 = list_of_num[3]
a5 = list_of_num[4]

list.pop(a1)
list.pop(a2)
list.pop(a3)
list.pop(a4)
list.pop(a5)

print("Mavi Takım  ---  Kırmızı Takım")
print(blue_team[0] + "       ---  " + list[0])
print(blue_team[1] + "       ---  " + list[1])
print(blue_team[2] + "       ---  " + list[2])
print(blue_team[3] + "       ---  " + list[3])
print(blue_team[4] + "       ---  " + list[4])
