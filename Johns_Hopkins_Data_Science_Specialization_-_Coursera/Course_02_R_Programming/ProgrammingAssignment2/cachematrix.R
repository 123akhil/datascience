### Assignment 2: Caching the Inverse of a Matrix

# Matrix inversion is usually a costly computation and there may be some
# benefit to caching the inverse of a matrix rather than computing it
# repeatedly (there are also alternatives to matrix inversion that we will
# not discuss here). Your assignment is to write a pair of functions that
# cache the inverse of a matrix.
# 
# `makeCacheMatrix`: This function creates a special "matrix" object
# that can cache its inverse.


makeCacheMatrix <- function(x = matrix()) {
    inv <- NULL
    
    set <- function(y) {
        x <<- y
        inv <<- NULL
    }
    
    get <- function() x
    
    setInv <- function(inverse) inv <<- inverse
    
    getInv <- function() inv
    
    list(set = set, get = get, setInv = setInv, getInv = getInv)
}

# `cacheSolve`: This function computes the inverse of the special
# "matrix" returned by `makeCacheMatrix` above. If the inverse has
# already been calculated (and the matrix has not changed), then
# `cacheSolve` should retrieve the inverse from the cache.

cacheSolve <- function(x, ...) {
    ## Return a matrix that is the inverse of 'x'
    inv <- x$getInv()
    if(!is.null(inv)){ #if inverse exists due to previous calculation
        message("Found in cache: getting inverse matrix data...")
        return(inv) #return cached inverse
    }
    
    data <- x$get() 	#gets matrix data from element x
    inv <- solve(data) 	#solves the inverse
    x$setInv(inv) 		#sets the inverse into element x
    inv					#returns inverse
}
