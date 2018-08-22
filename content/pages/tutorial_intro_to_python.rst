:Title: Quick Intro to Python for Econometrics
:slug: tutorial_intro_to_python

.. sectnum::

.. contents::

-----

Main Resources
--------------

#. `“Introduction to Python for Econometrics, Statistics, and Data Analysis”
   <https://www.kevinsheppard.com/Python_for_Econometrics>`__ by Kevin Sheppard
#. `“Learn Python3 the Hard Way” <https://learnpythonthehardway.org/python3/>`__


Secondary Resource (for reference)
----------------------------------

`“Learn Python in X Minutes” <https://learnxinyminutes.com/docs/python3/>`__


Reading
-------

#. Sheppard Chapter 1: Set up Anaconda (Python 3.6). Don’t worry
   about Jupyter notebooks or Spyder. Our workflow will be to put everything in
   a script to be run from the command line or in a IPython terminal.
#. Learn Python3 the Hard Way through Exercise 8.
#. `Learn Python the Hard Way video
   <https://www.youtube.com/watch?v=QH8LfS-29JE>`__  for Exercise 21 on
   Functions. Note: This was made for Python 2.7, which didn’t require
   :code:`print` to be used as a function.
#. Sheppard Chapters 3–4, 18, 5, 7, 9 (except 9.2 & 9.4), 10–13, 16. Chapters
   6, 8, 14, 15, and 17 can be skimmed quickly or skipped altogether. These
   chapters just list various useful functions.

Exercises
---------

The exercises in Sheppard are okay, but they’re set up more like trivia than
actual programming problems. Instead, I would recommend practicing on the
following problems found on `Project Euler
<https://www.projecteuler.net/archives>`__. I’ve added notes for several of the
problems. Problem 42 is especially relevant because it requires reading data
from a file and processing that data.

* 1 & 2.
* 3: The solution should have three functions: 
    * :code:`is_prime` that takes an integer :code:`n` and returns :code:`True`
      if :code:`n` is prime and :code:`False` otherwise;
    * :code:`find_factor` that takes an integer :code:`n` and finds some factor
      of that integer
    * :code:`factorize` that takes an integer :code:`n` and, using the
      functions :code:`is_prime` and :code:`find_factor`, returns a list of the
      prime factors of :code:`n` (that is, a list of prime numbers that, when
      multiplied together, equal :code:`n`).
* 4: The solution should use a function :code:`is_palindrome` that takes a
  number :code:`n` and returns :code:`True` if the number is a palindrome and
  :code:`False` otherwise.
* 6: Use a Numpy array (e.g., :code:`np.arange`) and vector dot product.
* 7: Use your :code:`is_prime` function from Problem 3.
* 8: Copy the 1000-digit number directly into your Python script.
* 9 & 10.
* 18 & 67*: Use backward induction. 67 might be harder for a beginner because
  you have to read a file from disk. If you find a general solution to 18
  that’s not brute force, you can skip 67 for now.
* 42:
    * Create a dictionary :code:`letter_score` whose keys are all the
      letters of the alphabet and whose values are the letters' letter score,
      e.g. :code:`{'A': 1, 'B': 2, ... }`. Hint: you can (and should) do this
      programmatically using :code:`from string import ascii_uppercase` and
      Python's :code:`range` builtin function.
    * Create a function :code:`word_score` that takes a word string as an
      argument and returns the word score. It should use the
      :code:`letter_score:` dictionary.
    * Come up with a way to check if a word score is a triangle number.
    * Use the pandas library (:code:`import pandas as pd`) to read in the
      file and create a DataFrame with three columns: “word”, “word_score”,
      “is_triangle”.
