"# Loading_Data_Benchmark" 

Haki Benita's article "Fastest Way to Load Data Into PostgreSQL Using Python" is very interesting. I was able to replicate what's explained in the article and learned a few things.

Fib.ipynb has a generator-function which generate Fibonacci numbers
work.py defines a function to measure time and memory usage used by a function call. (packages time, functools, memory_profiler)

notebook beers_data_from_API: use generator function to obtain data from a public API, then save data to a JSON file

notebook Benchmark: use different methods to import data from a JSON file to PostgreSQL table. Measuring time and memory usage. 
(1) Insert record one by one
(2) Execute Many From Iterator
(3) Execute Batch From Iterator
(4) Execute Batch From Iterator with Page Size
(5) Copy
(6) Copy data from a string iterator (a file-like object acts as a buffer between the source and the copy command)
(7) Copy Data From a String Iterator with Buffer Size