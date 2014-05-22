################################################################################################################
# Program creates a matrix of presence/absence of unique bipartitions compiled from bootstrap trees            #
#                                                                                                              #
# Copyright (C) {2014}  {Ambuj Kumar, Kimball-Brain lab group, Biology Department, University of Florida}      #
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


library(ape)
bootTree <- read.tree("tree.nex")

valDict <- new.env()

for (val in bootTree){listL <- val$tip.label}

n = 1
for (val in bootTree){
    valDict[[paste("T", n, sep="")]] = prop.part(val, check.labels=TRUE)
    n = n + 1
    }

numVal <- data.frame(valDict[['T1']][1])


uniqueVectorDict <- new.env()

counter = 1

while (counter <= length(valDict)) {
    uniqueVectorList <- c()
    for (v1 in valDict[[paste("T", counter, sep="")]]){
        newpart = ""
        for (v2 in v1){
            newpart = paste(newpart, listL[[v2]], sep="_")}
        uniqueVectorList <- union(uniqueVectorList, newpart)
    }
    uniqueVectorDict[[paste("T", counter, sep="")]] <- uniqueVectorList
    counter = counter + 1
}

newVector <- c()

counter = 1

while (counter <= length(valDict)) {
    newVector <- union(newVector, setdiff(uniqueVectorDict[[paste("T", counter, sep="")]], newVector))
    counter = counter + 1
}


counter = 1

dfAll <- c()

dfAll <- data.frame(matrix(NA, (nrow=length(uniqueVectorDict))))

for (val in newVector){
    var <- c()
    counter = 1
    while (counter <= length(uniqueVectorDict)){
        for (inval in uniqueVectorDict[[paste("T", counter, sep="")]])
        {
            
            if (val == inval){
                flag = 1
                break
            }
            else {flag = 0}
        }
        var <- rbind(var, flag)
        counter = counter + 1
    }
    dfAll <- data.frame(var, dfAll)
}

dfAll = dfAll[,colMeans(is.na(dfAll)) == 0]
dfAll['var.1'] <- NULL

write.table(dfAll, file="outMat.txt", sep="\t", row.names = FALSE, col.names = FALSE)





