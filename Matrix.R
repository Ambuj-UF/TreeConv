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

n = 1
for (val in bootTree){
    valDict[[paste("T", n, sep="")]] = prop.part(val, check.labels=TRUE)
    n = n + 1
}

counter = 1

while (counter <= length(valDict)){
    d<-c()
    for (inval in bootTree[counter]){data <- inval}
    write.table(toString(data$tip.label), file='test.txt', row.names = FALSE, col.names = FALSE, append = TRUE)
    for (val in valDict[[paste("T", counter, sep="")]]){d <- union(d, list(val))}
    for (val in d){
        write.table(toString(val), file='test.txt', append=TRUE, row.names = FALSE, col.names=FALSE)
        
    }
    
    write.table('\n\n', file='test.txt', append=TRUE, row.names = FALSE, col.names=FALSE)
    
    counter = counter + 1
}
