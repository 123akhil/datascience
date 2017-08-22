library(readr)
pollutantmean <- function(directory, pollutant, id = 1:332){
    ##'directoy' is the character vector of length 1 indicating
    ##the location of the CSV file
    
    ##'pollutant is a character vector of length 1 indicating
    ##the name of the pollutant 
    
    ##'id' integer vector indication the monitor ID numbers to be used
    
        # testCase
        # source("pollutantmean.R")
        # pollutantmean("specdata", "sulfate", 1:10)
        # ## [1] 4.064
        # pollutantmean("specdata", "nitrate", 70:72)
        # ## [1] 1.706
        # pollutantmean("specdata", "nitrate", 23)
        # ## [1] 1.281
    
    filesList <- list.files(path = directory, pattern = "*.csv") #read all files
    subFiles <- filesList[id] #subset file list to id set
    mergeData <- c() #creates the mergeMeans vector
    
    for (i in seq_along(subFiles)){ #loops through the subset number of elements
        singleFile <- read.csv(file.path(directory, subFiles[i]))
        mergeData <- c(mergeData, singleFile[[pollutant]])
    }
    
    return(mean(mergeData, na.rm = TRUE))
}