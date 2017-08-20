dfFaz2 = pd.read_table(FazFile1,decimal=",", skipinitialspace=True)

dfFaz2[dfFaz2.columns[-2]] = dfFaz2[dfFaz2.columns[-2]].astype(float)*1000000000
dfFaz2[dfFaz2.columns[0]] = pd.to_datetime(dfFaz2[dfFaz2.columns[0]], format = "%d-%b-%Y %H:%M:%S.%f")

dfFaz2 = dfFaz2[[dfFaz2.columns[i] for i in FazColToCopy]].copy()
dfFaz2 = dfFaz2.rename(columns={dfFaz2.columns[0]: 'FazTime', dfFaz2.columns[1]: 'FazWL'})

########################################################
# 2017-Apr-13
########################################################

# Pandas apply floating slope (slope of the linear regression) on last n values
dfMerge["linreg_Templog"] = pd.rolling_apply(dfMerge.TempVal,40,func= lambda x: slope(x)) # This is obsolete
# The same using lambda function call
dfMerge["linreg_Templog"] = dfMerge.TempVal.rolling(window=40,min_periods=1).apply(lambda x: slope(x))
# Without lambda, just simply calling slope
dfMerge["linreg_Templog"] = dfMerge.TempVal.rolling(window=40,min_periods=1).apply(slope)

# The slope function calculates the slope from the linear regression
# This can be done by scipy as well
def slope(Y):
    #print Y, type(Y)
    A = np.array([ np.arange(0,len(Y)), np.ones(len(Y))])
    return np.linalg.lstsq(A.T,Y)[0][0]
    
# Check this
# http://stackoverflow.com/questions/14300768/pandas-rolling-computation-with-window-based-on-values-instead-of-counts
# http://pandas.pydata.org/pandas-docs/stable/computation.html

# renaming columns
dfMerge.rename(columns={'-50,54205': 'Faz_int','-49,88_x': 'Exfo_int','-49,88_y': 'Moi_int','-42,87': '400_int'}, inplace=True)

#Matplotlib formatting
plt.figure(figsize=(15,15))
ax = plt.gca()
ax.ticklabel_format(useOffset=False)

dfMerge.ix[dfMerge.sel_rows < 4,"sel_rows"] = 0

########################################################
# 2017-Apr-14
########################################################

# Count consecutive characters
# http://stackoverflow.com/questions/34443946/count-consecutive-characters

# Join list multidimensional lists into one-dimensional list
from itertools import chain
list(chain.from_iterable((i, i**2) for i in xrange(1, 6)))


# How to use itertools groupby
# https://matthewmoisen.com/blog/itertools-groupby-example/


# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sorted(xs.items(), key=lambda x: x[1])
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:

import operator
sorted(xs.items(), key=operator.itemgetter(1))
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]


########################################################
# 2017-Apr-15
########################################################

# Python object-oriented programming
# "C:\Users\admin\Documents\Patex\Programming\oop-in-python-best-resources.pdf"
# https://dbader.org/blog/abstract-base-classes-in-python
# https://dbader.org/blog/6-things-youre-missing-out-on-by-never-using-classes-in-your-python-code
# https://www.tutorialspoint.com/python/python_classes_objects.htm
# https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/


# Tree and Trie data structure
# http://pythonfiddle.com/python-trie-implementation/
# https://nickstanisha.github.io/2015/11/21/a-good-trie-implementation-in-python.html

# How to use Flake8

# Useful Jupyter-Notebooks
# https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks

########################################################
# 2017-Apr-16
########################################################

# The method setdefault() is similar to get(), but will set dict[key]=default 
# if key is not already in dict.

dict.setdefault(key, default=None)

########################################################
# 2017-Apr-17
########################################################

# Data Structures and Algorithms with Python
# http://knuth.luther.edu/~leekent/CS2Plus/index.html

########################################################
# 2017-Apr-29
########################################################

# Markdown cheatsheet. E.g. for github readme.md files
# https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links

# Eclipse Egit, Git workaround
# http://stackoverflow.com/questions/19474186/egit-rejected-non-fast-forward

# Introduction to pytest
# https://www.youtube.com/watch?v=LdVJj65ikRY&ab_channel=EuroPython2014

########################################################
# 2017-May-12
########################################################

# How to check if a list is a subset of another list
def counterSubset(list1, list2):
    c1, c2 = Counter(list1), Counter(list2)
    print c1
    print c2
    for k, n in c1.items():
        if n > c2[k]:
            return False
    return True

# Another solution
def test_subset(seq_1, seq_2):
    inner_list_1 = list(seq_1)
    inner_list_2 = list(seq_2)
    for elem in inner_list_1:
        if elem not in inner_list_2:
            return False
        else:
            inner_list_2.remove(elem)
    return True

########################################################
# 2017-Jun-4
########################################################

# How can I find the number of arguments of a Python function?
# https://stackoverflow.com/questions/847936/how-can-i-find-the-number-of-arguments-of-a-python-function

########################################################
# 2017-Jun-26
########################################################

# How to list all subfolders

# https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory
import os
os.walk(directory)

########################################################
# 2017-Jul-10
########################################################

# pickle and shelve - object serialization and deserialization

import pickle
with open('entry.pickle', 'wb') as f:
    pickle.dump(entry, f)   # entry is the structure to serialize, dump writes the entry to the output file
    
# Once the data is saved, this is a way how to load it
import pickle
with open('entry.pickle', 'rb') as f:
    entry = pickle.load(f)

# What if, if we dont want to store the data in a file:
b = pickle.dumps(entry)
type(b)
#<class 'bytes'> - stores it as bytes

# Very good article about this topics
# http://www.diveintopython3.net/serializing.html
entry3 = pickle.loads(b)

# Read this about bytes and strings
# http://www.diveintopython3.net/strings.html#byte-arrays

# python disasembler
# https://docs.python.org/3.5/library/dis.html#module-dis
import dis

# Video on pickle
# https://www.youtube.com/watch?v=2Tw39kZIbhs&ab_channel=sentdex

# What is shelve, whats the relation between pickle and shelve

# pickle is for serializing some object (or objects) as a single bytestream in
# a file.

# shelve builds on top of pickle and implements a serialization dictionary
# where objects are pickled, but associated with a key (some string), so you
# can load your shelved data file and access your pickled objects via keys.
# This could be more convenient were you to be serializing many objects.

import shelve

integers = [1, 2, 3, 4, 5]

# If you're using Python 2.7, import contextlib and use
# the line:
# with contextlib.closing(shelve.open('shelf-example', 'c')) as shelf:
with shelve.open('shelf-example', 'c') as shelf:
    shelf['ints'] = integers

# Reading the object from shelve
import shelve

# If you're using Python 2.7, import contextlib and use
# the line:
# with contextlib.closing(shelve.open('shelf-example', 'r')) as shelf:
with shelve.open('shelf-example', 'r') as shelf:
    for key in shelf.keys():
        print(repr(key), repr(shelf[key])))

# https://stackoverflow.com/questions/4103430/what-is-the-difference-between-pickle-and-shelve

# If we load the object from shelve, and updated the methods in the meantime, it can work with the updates

# What is the difference between __getattr__ and __getattribute__
# https://stackoverflow.com/questions/3278077/difference-between-getattr-vs-getattribute

# getattr(), setattr(), __getattr__(), __setattr()

# __getattr__()
# https://stackoverflow.com/questions/4295678/understanding-the-difference-between-getattr-and-getattribute


########################################################
# 2017-Aug-20
########################################################

# How to make compound labels in tkinter gui
# compound - text and image are overlaying

from Tkinter import *

root = Tk()
logo = PhotoImage(file="../images/python_logo_small.gif")
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""
w = Label(root, 
          compound = CENTER,
          text=explanation, 
          image=logo).pack(side="right")

root.mainloop()