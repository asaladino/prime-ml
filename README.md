# Prime ML

## The question
Would a ML model be any good a at predicting prime numbers?

The training set will consist of numbers with an upper limit of 20 digits and be able to predict
numbers with 21 digits.

The lower training boundary will be `00000000000000000003`
upper training limit is `09999999999999999999` but should be able to predict up to `99999999999999999999`.

## Successful model
A successful model should predict:
1. Numbers ending with `0, 2, 4, 5, 6, 8` are not prime.

## Encoding
The number will be:
1. Converted to a character array.
1. Encoded by character index.
1. Then each encoded character will be converted to a one hot array.

The characters we will encode are:
```
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```
and will correspond to the the index starting at zero.
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Initial number
```
09876543219876543219
```

1 Character array
```
['0', '9', '8', '7', '6', '5', '4', '3', '2', '1', '9', '8', '7', '6', '5', '4', '3', '2', '1', '9']
```

2 Encoded index.
```
[0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9]
```

3 One hot array
```
[
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]
```

The final output will be a binary classification of:
```
[0] # not prime
[1] # is prime 
```

## Training Set
For the training set, we will use all the primes between the upper an lower bounds,
mixed with random numbers that are not prime. 