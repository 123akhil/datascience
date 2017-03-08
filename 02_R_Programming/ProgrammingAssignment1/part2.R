complete <- function(directory, id = 1:332){
    ##'directoy' is the character vector of length 1 indicating
    ##the location of the CSV file
    
    ##'id' integer vector indication the monitor ID numbers to be used
    
    filesList <- list.files(path = directory, pattern = "*.csv") #read all files
    subFiles <- filesList[id] #subset file list to id set
    nobs <- numeric() #creates the number of observations variable
    
    for (i in seq_along(subFiles)){ #loops through the subset number of elements
        singleFile <- read.csv(file.path(directory, subFiles[i]))
        nobs <- c(nobs, sum(complete.cases(singleFile))) # adds the sum of complete cases to the nobs vector
    }
    
    data.frame(id, nobs) #creates the data.frame with the ID and nobs vectors

}