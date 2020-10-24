# Summations

Congratulations on writing your first code containing a summation.  Hopefully, your code looked something like the code in main.py.  There is, however, another way that we could go about writing this code.  We can write this code by exploiting the fact that:

````
timesTable[n+1] = timesTable[n] + table
````

Your task in this exercise is to exploit the expression above to rewrite the code shown on the left without using any arrays (in other words, you can only use scalar-valued variables).  To pass the test your code will need to generate the following output:

````
0
7
14
21
28
35
42
49
56
63
70
````

Notice that you can achieve an output like the one above by putting the print statement in the loop like this:

````
for i in range(11)
    timesTable[i] = i*table
    print(timesTable[i])
````    
