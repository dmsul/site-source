:Title: Best Practices when Writing Python
:slug: tutorial_workflow_3python

.. sectnum::

Writing Code in Econ:

* `Overview <tutorial_workflow_0overview.html>`__
* Previous: `Project Organization <tutorial_workflow_2project_org.html>`__

.. contents::

-----

    Indeed, the ratio of time spent reading versus writing is well over 10 to
    1. We are constantly reading old code as part of the effort to write new
    code. ...[Therefore,] making it easy to read makes it easier to write.

    ~ Robert C. Martin, Clean Code: A Handbook of Agile Software Craftsmanship

Writing code clearly is important, especialy when you're working with a team.
Code that's easy to read improves everyone's productivity, even when the
"other" person reading the code is you two months from now after you've
forgotten everything you wrote.


No copying and pasting
----------------------

Variables and algorithms should be defined in exactly one place. This is a
cardinal rule. If you copy and paste code to use it in multiple places, it is
difficult to make sure any changes you make later also get copied and pasted.
If a file name is defined in only one place and imported everywhere it's used,
you can change the file name in a single place and you know for certain and all
of your code will use the new file name. 


Write self-documenting code
---------------------------

Give variables, functions, and files descriptive names. Err on the side of
names being too long and too descriptive. Part of the reason you should be
using tools like a good text editor and a good console like CMDer is that they
have lots of predictive text and auto-completion functions to help with long
variable and file names. Use comments to clarify why a particular coding
choice was made. A few examples:

* The filename :code:`reg_sale_price.py` is beter than :code:`reg.py`.
  A name like :code:`table1.py` is completely forbidden.
* It is helpful to name functions or variables that only take on True/False
  values with :code:`is_` or :code:`has_`. See :code:`is_triangle` in the
  example code below.

A few other naming conventions we tend to follow:

* If a function only deals with a single Pandas DataFrame, call it :code:`df`.
* Indexes in loops should still be descriptive. However, the index inside a
  list comprehension can be something short like :code:`i` or :code:`x`,
  provided there is only one variable being looped over.
* Degrees longitude and latitude will tend to be called :code:`x` and :code:`y`
  respectively. This is not a requirement but we have found that it's easy to
  mix up "latitude" and "longitude".


Use functions like paragraphs
-----------------------------

The main unit of code should be functions. Even if you think you're only going
to use a function once, breaking the code into functions makes it easier to
read the code.


Scripts should only contain functions and an "if-main" block
------------------------------------------------------------

When you import something from another Python file, the entire file is executed
first. Suppose you want to import a function called
:code:`computation_that_takes_forever` which is used in script
:code:`cleandata.py` that looks like this

.. code-block:: python3
    :linenos: table

    import pandas as pd

    def computation_that_takes_forever(df):
        """ This takes a long time """
        df = df ** df ** df
        # Other stuff
        return df

    df = pd.read_csv('giant_dataset.csv')
    df = computation_that_takes_forever(df)

When you run :code:`from cleandata import computation_that_takes_forever`, the
entire :code:`cleandata.py` script gets run, **including the data loading and
processing on lines 9 and 10!!** We don't want to run this whole data cleaning
process every time we import the function.

The solution is to put that execution in a different function or in an
"if-main" block like so:


.. code-block:: python3
    :linenos: table

    import pandas as pd

    def computation_that_takes_forever(df):
        """ This takes a long time """
        df = df ** df ** df
        # Other stuff
        return df

    if __name__ == '__main__':
        df = pd.read_csv('giant_dataset.csv')
        df = computation_that_takes_forever(df)

Any code inside the :code:`if __name__ == '__main__'` block will only be
executed if the script is called directly from the command line or via
:code:`%run` in IPython. It is *not* run if the script is imported by another
script. So in our new version of :code:`cleandata.py`, lines 10 and 11 only get
executed if we run :code:`python cleandata.py` from the command line or
:code:`%run cleandata.py` inside IPython.


Use the IPython terminal and a text editor
------------------------------------------

Jupyter and Spyder are great tools for analyzing data in Python. However, it
is hard to keep perfect track of your computing environemnt (which versions of
packages are loaded, etc.) while using these tools. Our preferred solution is
to use a robust text editor (Atom, Vim, Emacs) alongside a CMDer window running
the IPython terminal. You can then use the :code:`%run` command inside IPython
to run your code.


Incrementally build your code in a script
-----------------------------------------

It's pretty common for data work in social science to look like this: You open
STATA, R, Python, etc. and start poking around on the command line, interacting
with the data until you get where you want. Then you use the command history
(or your memory) to reconstruct what you did and put it in a script.

This is a bad way to work. Reconstructing exactly what you did is often
difficult. At best, you're doing everything twice. Jupyter notebooks were
designed in part to address this problem. However, as mentioned above, our
work doesn't always play nice with Jupyter notebooks.

You can avoid duplicating your work and introducing bugs by incrementally
writing your script. Start with a script that's empty except for the if-main
block. Write the beginnings of your first function in the if-main block:

.. code-block:: python3

    import pandas as pd

    if __name__ == '__main__':
        # Prep data for regression
        df = pd.read_csv('data.csv')
        df = df[df['state'] == 'TX']    # Restrict to Texas
        # Do other cleaning

Now run your script using :code:`%run` in IPython. Use some basic interactivity
to figure out any bugs (e.g., maybe the state variable isn't called "state").
After you fix a problem in your script, :code:`%run` it again. Keep doing this
until you're done with the given task (e.g., prepping the data for a
regression), then move that code into a function.

.. code-block:: python3

    import pandas as pd

    def prep_data_for_reg():
        """ Prep data for regression """
        df = pd.read_csv('data.csv')
        df = df[df['state'] == 'TX']    # Restrict to Texas
        # Do other cleaning...
        return df

    if __name__ == '__main__':
        df = prep_data_for_reg()

Now you can start work on your next task in the if-main block in the same way.
This is also a good time to commit your changes in Git if you haven't already
done so.

When you're done, there should be a very simple if-main block or no if-main
block at all.


Use a consistent style
----------------------

Just like for writing prose, there are style guides for writing code. Python as
an official style guide called PEP8 that contains more rules than I'll go over
here. However, there is a create Python tool called Flake8 that will
automatically check your code for PEP8 errors and syntax errors. It can be
integrated into the Atom editor using the :code:`linter-flake8` plugin.

A few examples of important PEP8 rules that we'll follow:

Lines should be less than 80 characters wide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lines of code should be less than 80 characters wide. Fortunately in Python
  line wrapping is very easy. Anything within parentheses can be broken across
  lines, including function calls:

.. code-block:: python3

    std_dev = find_std_dev(dataset1,
                           dataset2,
                           dataset3)

Even if a line of code won't break 80 characters, it's often easier to break it
into several lines for clarity.

.. code-block:: python3

    bad_seconds_per_year = 60 * 60 * 24 * 365

    good_seconds_per_year = (
        60 *     # seconds per minute
        60 *     # minutes per hour
        24 *     # hours per day
        365      # days per year
    )

    bad_dataframe_chain = df.rename(columns={'Yearly Avg': 'mean'}).drop('dumb_var', axis=1)
    bad_dataframe_chain = bad_dataframe_chain.set_index('state_id')

    good_dataframe_chain = (df
                            .rename(columns={'Yearly Avg': 'mean'})
                            .drop('dumb_var', axis=1)
                            .set_index('state_id'))

Long strings can be wrapped in parenthesis as well and will automatically be
concatenated. Just don't forget to add spaces where necessary.

.. code-block:: python3

    one_long_string = (
        "When in the course of human events "
        "it becomes necessary for one "
        "people to dissolve the political "
        "bands which have connected them "
        "with another and to assume among "
        "the powers of the earth, the "
        "separate and equal station to which "
        "the Laws of Nature and of Nature's "
        "God entitle them, a decent respect "
        "to the opinions of mankind requires "
        "that they should declare the causes "
        "which impel them to the separation."
    )

This also holds for imports, which can also be broken across lines using parens

.. code-block:: python3

    from datasource import (load_data_1, load_data_2, load_data_3, load_data_4,
                            load_data_5)


Indentation
~~~~~~~~~~~

Whitespace is important in Python and screwing up indentation can cause your
code to crash.

* Do not use tabs to indent. Use 4 spaces. Your editor should have a setting
  for this, so that when you hit the tab key the editor inserts 4 spaces
  instead of a tab code (:code:`\t`).
* When you break a line using parentheses, the next line should line up with
  the open parenthesis on the line above. If the open parenthesis is the alone
  on that line, indent once.

.. code-block:: python3

    # This is good
    from datasource import (load_data_1, load_data_2, load_data_3, load_data_4,
                            load_data_5)
    # This is bad
    from datasource import (load_data_1, load_data_2, load_data_3, load_data_4,
                                load_data_5)

    # This is good
    good_seconds_per_year = (
        60 *     # seconds per minute
        60 *     # minutes per hour
        24 *     # hours per day
        365      # days per year
    )
    # This is bad
    bad_seconds_per_year = (
                60 *     # seconds per minute
                60 *     # minutes per hour
                24 *     # hours per day
                365      # days per year
    )


Imports
~~~~~~~

* Imports go at the top of the file.
* *NEVER* import an entire package like this: :code:`from numpy import *`.
* Separate and order imports like so

.. code-block:: python3

    import re               # Standard library (come with Python)
    import os

    import numpy as np      # Third-party packages
    import pandas as pd     

    from drillinginfo import clean_wells    # Packages developed by our team

    from util.env import data_path          # Imports from *this* project


Other stuff
~~~~~~~~~~~

* Spaces around assignments: :code:`x = 7` not :code:`x=7`.
* Name functions and variables with lowercase letters and underscores.
* Functions meant to be local (subroutines not meant to be imported by other
  scripts) should start with an underscore, e.g., :code:`_drop_missings()`.
* Two lines between unrelated functions. One line between auxiliary functions:

.. code-block:: python3
    :linenos: table

    def primary_func1():
        # Stuff

    def _aux_to_1():
        # Stuff

    def _another_aux_to_1():
        # Stuff


    def primary_func2():
        # Stuff

    def _aux_to_2():
        # Stuff




Example Code
------------

.. code-block:: python3
    :linenos: table

    """
    Task: read the words from the file `tmp.txt` and calculate each word's score
    based on the "value" of its letters, where A=1, B=2, etc. Then calculate how
    many words in the file are "triangle" numbers. A number T is a triangle number
    if there is an integer n such that T = n * (n + 1) / 2. Solution to Project
    Euler Problem 42.
    """
    from string import ascii_uppercase

    import numpy as np
    import pandas as pd


    LETTER_SCORE = {ascii_uppercase[x - 1]: x for x in range(1, 27)}


    def word_score(word):
        """ Calculate total letter score for `word` """
        score = 0
        for letter in word:
            score += LETTER_SCORE[letter]
        return score


    def is_triangle(x):
        """
        Use definition of triangle number and the quadratic formula to see if
        `x` is a triangle number.
        """
        positive_root = _positive_quadratic_root(x)
        return positive_root == int(positive_root)

    def _positive_quadratic_root(x):
        a = 1
        b = 1
        c = -2 * x

        positive_root = (-1 * b + np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

        return positive_root


    if __name__ == '__main__':
        df = pd.read_csv('tmp.txt', header=None)
        df.columns = ['word']

        df['word_score'] = df['word'].apply(word_score)
        df['is_triangle'] = df['word_score'].apply(is_triangle)

        print(df['is_triangle'].sum())
