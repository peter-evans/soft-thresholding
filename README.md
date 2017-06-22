# Candidate Selection using Iterative Soft-Thresholding

This describes one way to use soft-thresholding to select the statistically best candidates from a sorted list. This algorithm was introduced to me as an alternative to setting a hard threshold, i.e. selecting a fixed number of the best candidates. Using an iterative soft-thresholding algorithm a variable number of candidates can be selected depending on the distribution of the values.

In the following example the best candidates are selected from a sorted list. Setting a hard threshold of three will of course always select the top three candidates. However, it's clear from looking at the distribution of the values that only the top two should be considered as candidates. This soft-thresholding algorithm allows us to select just those candidates.

![HardVsSoftThresholding](/images/hard-vs-soft-thresholding.png?raw=true)

# How the algorthim works

In each iteration the algorithm compares the mean and the median for the values remaining in the list. Any values higher than the minimum of the mean and median are discarded. The process is repeated until exit conditions are satisfied or until there is only one value remaining.

![CompareMeanMedian](/images/compare-mean-median.png?raw=true)

# Sample code

The sample python code [here](soft_thresholding.py) is a simple example to demonstrate how iterative soft-thresholding can be implemented. The sorted list values are randomly generated on each execution of the script. Executing the script a number of times shows how the number of selected candidates varies based on the distribution.

One candidate is selected:
```bash
~$ python soft_thresholding.py
Sorted list of candidates: [2, 10, 11, 20, 22, 23, 27, 29, 35, 39, 43, 44, 49, 57, 58, 61, 65, 66, 68, 83, 83, 91, 94, 94, 99]
Remaining candidates: 25
Remaining candidates: 13
Remaining candidates: 7
Remaining candidates: 3
========================
Selected candidates: [2]
```
Two candidates are selected:
```bash
~$ python soft_thresholding.py
Sorted list of candidates: [1, 1, 2, 3, 4, 7, 8, 10, 14, 16, 17, 26, 29, 39, 44, 45, 50, 58, 61, 68, 77, 81, 96, 99, 99]
Remaining candidates: 25
Remaining candidates: 13
Remaining candidates: 7
Remaining candidates: 4
Remaining candidates: 2
========================
Selected candidates: [1, 1]
```
Three candidates are selected:
```bash
~$ python soft_thresholding.py
Sorted list of candidates: [2, 3, 4, 5, 5, 6, 12, 12, 16, 17, 20, 21, 26, 27, 32, 34, 41, 53, 55, 58, 59, 61, 72, 86, 96]
Remaining candidates: 25
Remaining candidates: 13
Remaining candidates: 6
Remaining candidates: 3
========================
Selected candidates: [2, 3, 4]
```

# Fine tuning



## License

MIT License - see the [LICENSE](LICENSE) file for details
