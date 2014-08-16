################################################################################################################
#                                                                                                              #
# Copyright (C) {2014}  {Ambuj Kumar, Kimball-Braun lab group, Biology Department, University of Florida}      #
#                                                                                                              #
# This program is free software: you can redistribute it and/or modify                                         #
# it under the terms of the GNU General Public License as published by                                         #
# the Free Software Foundation, either version 3 of the License, or                                            #
# (at your option) any later version.                                                                          #
#                                                                                                              #
# This program is distributed in the hope that it will be useful,                                              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of                                               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                                                #
# GNU General Public License for more details.                                                                 #
#                                                                                                              #
# This program comes with ABSOLUTELY NO WARRANTY;                                                              #
# This is free software, and you are welcome to redistribute it                                                #
# under certain conditions;                                                                                    #
#                                                                                                              #
################################################################################################################

f = open('test.txt', 'r')
data = f.readlines()
f.close()

dictV = dict()
values = []
counter = 1

for lines in data:
    if lines == '\n':
        dictV['T' + str(counter)] = (values)
        counter = counter + 1
        values = []
    else:
        values.append(lines.rstrip())

dictV['T1'].insert(0, '"')

for key, list in dictV.items():
    dictV[key] = list[1:-1]

for key, val in dictV.items():
    for i, inval in enumerate(val):
        if inval.startswith('"') and inval.endswith('"'):
            newval = inval[1:-1].split(',')
            for j, x in enumerate(newval):
                newval[j] = x.strip()
            val[i] = newval
    dictV[key] = val


for key, val in dictV.items():
    list1 = val
    list2 = val[1]
    for i, inval in enumerate(val):
        if i <= 1:
            continue
        else:
            nl = []
            list3 = inval
            nl.append([x for x in list2 if x not in list3])
            if nl[0] in list1:
                if len(nl[0]) > len(list3):
                    list1.remove(nl[0])
                else:
                    list1.remove(list3)
    dictV[key] = ([x for x in list1 if x != list1[1]])

unpDict = dict()

for key, val in dictV.items():
    counter = 1
    unpList =[]
    while counter < len(val):
        st = ''
        for inval in val[counter]:
            st = st + '_' + val[0][int(inval)-1]
        unpList.append(st)
        unpDict[key] = (unpList)
        counter = counter + 1

for key, val in unpDict.items():
    for i, inval in enumerate(val):
        x1 = inval.split('_')[1:]
        x1.sort()
        newInval = '_'.join(x1)
        val[i] = newInval
    unpDict[key] = val

unpAll = []
counterUB = 1

while counterUB <= len(unpDict):
    for val in unpDict['T' + str(counterUB)]:
        if val not in unpAll:
            unpAll.append(val)
    counterUB = counterUB + 1

matrixData = dict()
for i, val in enumerate(unpAll):
    st = []
    newCounter = 1
    while newCounter <= len(unpDict):
        if val in unpDict['T' + str(newCounter)]:
            f = 1
        else:
            f = 0
        st.append(f)
        newCounter = newCounter + 1
    matrixData['bipart' + str(i)] = (st)


with open('outMat.txt', 'w') as fp:
    outCounter = 0
    while outCounter < len(matrixData['bipart1']):
        inCounter = 0
        while inCounter < len(matrixData):
            fp.write(str(matrixData['bipart' + str(inCounter)][outCounter]) + '\t')
            inCounter = inCounter + 1
        fp.write('\n')
        outCounter = outCounter + 1
    









