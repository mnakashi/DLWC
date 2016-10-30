# coding: utf-8
import numpy as np


print np.array([1,2,3])
print np.array(range(10))
print np.arange(10)
print np.array([[0,1,2],[3,4,5]])
print np.arange(6).reshape(2,3)

a = np.arange(6).reshape(2,3)
print a
print a.reshape(3,2)

print np.arange(27).reshape(3,3,3)
a = np.arange(60).reshape(10,6)
print a.shape, a.size
nrow, ncol = a.shape
print nrow, ncol

print np.zeros(5), np.ones(5)
print np.empty(5)
print np.random.randn(5)

print np.random.uniform(0,1,3)
print np.random.normal(1.5,2.0,3)
print np.random.permutation(range(6))
print np.random.permutation(6)

print np.identity(5)
