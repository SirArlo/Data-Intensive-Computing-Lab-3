# Data-Intensive-Computing-Lab-3
The report for this lab is available in the Documentation branch.

In order to run the code clone the repo which can be found at:

[Data-Intensive-Computng-Lab3](https://github.com/SirArlo/Data-Intensive-Computing-Lab-3)

Before the code can be run the input matricies need to be converted from sparse to a dynamic matrix, to do this the input files must be run with the Sparse-Dense script. To do this go into [Code/Matricies](Code/Matricies/Sparse-Dense.py) and run the following command in terminal for each of the files:

`python Sparse-Dense.py "FileName".list`

**To run the code enter the corresponding command in terminal in the main folder:**

For the iterative approach with a matrixA of 100x100 multiplied by matrixB of 100x100:

`python Code/AlgorithmA.py ./Code/Matricies/outA1.list ./Code/Matricies/outB1.list Output --mrs-timing-file=./Time_Results/AlgoA_small.txt`

For the iterative approach with a matrixA of 1000x500 multiplied by matrixB of 500x1000:

`python Code/AlgorithmA.py ./Code/Matricies/outA2.list ./Code/Matricies/outB2.list Output --mrs-timing-file=./Time_Results/AlgoA_medium.txt`

For the iterative approach with a matrixA of 1000x500 multiplied by matrixB of 500x1:

`python Code/AlgorithmA.py ./Code/Matricies/outA3.list ./Code/Matricies/outB3.list Output --mrs-timing-file=./Time_Results/AlgoA_large.txt`

For the Divide and Conquer approach with a matrixA of 100x100 multiplied by matrixB of 100x100:

`python Code/AlgorithmB.py ./Code/Matricies/outA1.list ./Code/Matricies/outB1.list Output --mrs-timing-file=./Time_Results/AlgoB_small.txt`

For the Divide and Conquer approach with a matrixA of 1000x500 multiplied by matrixB of 500x1000:

`python Code/AlgorithmB.py ./Code/Matricies/outA2.list ./Code/Matricies/outB2.list Output --mrs-timing-file=./Time_Results/AlgoB_medium.txt`

For the Divide and Conquer approach with a matrixA of 1000x500 multiplied by matrixB of 500x1:

`python Code/AlgorithmB.py ./Code/Matricies/outA3.list ./Code/Matricies/outB3.list Output --mrs-timing-file=./Time_Results/AlgoB_large.txt`

The time taken to complete each set of multilication can be found in the [Time_Results](Time_Results/) folder

Where the output of the results can be found in the output folder as a .mtxt file
