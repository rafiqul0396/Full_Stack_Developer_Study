#### what is memoization in dp?
- memoization is a technique of storing the results of expensive function calls and returning the cached result when the same inputs occur again.
- Memoization is a technique used in computer science and programming to optimize the execution time of a function by caching its results. The idea behind memoization is to store the output of expensive function calls and return the cached result when the same inputs occur again, instead of recomputing the result.

When a function is called with a particular set of inputs, the memoization technique first checks whether the function has already been called with those inputs before. If so, it returns the cached result, avoiding the need to perform the expensive computation again. If the function has not been called with those inputs before, it executes the function normally, computes the result, and stores it in a cache for future use.

Memoization can be implemented using various data structures, such as arrays, hash tables, or dictionaries, where the function's inputs serve as the keys, and the corresponding outputs are stored as values. This caching mechanism allows subsequent calls to the function with the same inputs to be retrieved quickly from the cache, significantly improving the performance and efficiency of the program.

Memoization is commonly used with recursive functions, where the same inputs can be encountered multiple times during the recursive calls. By memoizing the results, unnecessary recursive calls can be avoided, reducing the time complexity of the algorithm.

Overall, memoization is a powerful technique to optimize function execution by eliminating redundant computations and reusing previously computed results. It is particularly useful when dealing with functions that have expensive or time-consuming computations, improving the overall performance of the program.

Memoization is a technique used in computer science and programming to optimize the execution time of a function by caching its results. The idea behind memoization is to store the output of expensive function calls and return the cached result when the same inputs occur again, instead of recomputing the result.

When a function is called with a particular set of inputs, the memoization technique first checks whether the function has already been called with those inputs before. If so, it returns the cached result, avoiding the need to perform the expensive computation again. If the function has not been called with those inputs before, it executes the function normally, computes the result, and stores it in a cache for future use.

Memoization can be implemented using various data structures, such as arrays, hash tables, or dictionaries, where the function's inputs serve as the keys, and the corresponding outputs are stored as values. This caching mechanism allows subsequent calls to the function with the same inputs to be retrieved quickly from the cache, significantly improving the performance and efficiency of the program.

Memoization is commonly used with recursive functions, where the same inputs can be encountered multiple times during the recursive calls. By memoizing the results, unnecessary recursive calls can be avoided, reducing the time complexity of the algorithm.

Overall, memoization is a powerful technique to optimize function execution by eliminating redundant computations and reusing previously computed results. It is particularly useful when dealing with functions that have expensive or time-consuming computations, improving the overall performance of the program.

#### give me one examples?
- fibonacci series
- 1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987
  


## how we solve the dynamic programming problem

- 1. identify if it is a dp problem
- 2. recursively solve the dynamic programming problem
-  3. solve the dynamic programming problem


## top down approach
- 1. identify if it is a dp problem
- 