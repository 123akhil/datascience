corr <- function(directory, threshold = 0){
    ##'directoy' is the character vector of length 1 indicating
    ##the location of the CSV file
    
    ##'threshold' is a numeric vector of lebgth 1 indicating the number
    ##'of completely observed observations (on all variables) required 
    ##'to compute the correlation between nitrate and sulfate; default = 0
    
    ##'return a numeric vector of correlations
    
    dF1 <- complete(directory)
    ids <- dF1[dF1["nobs"] > threshold, ]$id
    crl = numeric()
    
    for (i in ids) {
        newRead <- read.csv(paste(directory,"/", formatC(i, width = 3, flag = "0"), ".csv", sep = ""))
        dF2 <- newRead[complete.cases(newRead), ]
        crl <- c(crl, cor(dF2$sulfate, dF2$nitrate))
    }
    
    return(crl)
    
}