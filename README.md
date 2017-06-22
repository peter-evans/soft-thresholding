# Candidate Selection using Iterative Soft-Thresholding

This describes one way to use soft-thresholding to select the statistically best candidates from a sorted list. This algorithm was introduced to me as an alternative to setting a hard threshold, i.e. selecting a fixed number of the best candidates. Using an iterative soft-thresholding algorithm a variable number of candidates can be selected depending on the distribution of the values.

In the following example the best candidates are selected from a sorted list. Setting a hard threshold of three will of course always select the top three candidates. However, it's clear from looking at the distribution of the values that only the top two should be considered as candidates. This soft-thresholding algorithm allows us to select just those candidates.

![HardVsSoftThresholding](/images/hard-vs-soft-thresholding.png?raw=true)


![CompareMeanMedian](/images/compare-mean-median.png?raw=true)

