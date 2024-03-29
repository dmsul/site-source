:Title: Stata to Python Equivalents
:slug: tutorial_stata_to_python

.. sectnum::

.. contents::
    :depth: 1

.. html::
    <style>
        td {
          padding: 7px;
        }
        tr:nth-child(even){background-color: #eeeeee;}
    </style>



Special thanks to John Coglianese for feedback and for supplying the list of
"vital" Stata commands. Feedback and requests for additions to the list are
always welcome!

The official Pandas documentation includes a `"Comparison with Stata"
<https://pandas.pydata.org/pandas-docs/stable/comparison_with_stata.html>`__
page which is another great resource.


Intro/Note on Notation
----------------------

Coding in Python is a little different than coding in Stata.

In Stata, you have one dataset in memory. The dataset is a matrix where each
column is a "variable" with a unique name and each row has a number (the
special variable :code:`_n`). Everything in Stata is built around this
paradigm.

Python is a general purpose programming language where a "variable" is not a
column of data. Variables can be anything, a single number, a matrix, a list, a
string, etc. The Pandas package implements a kind of variable called a
DataFrame that acts a lot like the single dataset in Stata. It is a matrix
where each column and each row has a name. The key distinction in Python is
that a DataFrame is itself a variable and you can work with any number of
DataFrames at one time. You can think of each column in a DataFrame as a
variable just like in Stata, except that when you reference a column, you also
have to specify the DataFrame.

The Stata-to-Python translations below are written assuming that you have a
single DataFrame called :code:`df`. Placeholders like :code:`<varname>` and
:code:`<dtafile>` show where user-specified values go in each language. Note
that in many cases, :code:`<varname>` will be simple text in Stata (e.g.,
:code:`avg_income`) while in Python it will be a string (:code:`'avg_income'`).
If you were to write :code:`df[avg_income]` without quotes, Python would go
looking for a variable--a list, a number, a string--that's been defined
somewhere else. Because of this, :code:`<varlist>` in Python represents a list
of variable names: :code:`['educ', 'income', 2017]`.


Note on composability
---------------------

One concept that will push your Python skills forward quickly is
"composability." That is, you can combine base-level commands to "create" whole
new commands. This is a little more difficult in Stata where each line of code
acts on an entire dataset.

For example, let's say you know two commands in Python/pandas. First,
:code:`df[<condition>]`, which returns the rows of DataFrame :code:`df` for
which the Boolean :code:`<condition>` is True. This is like :code:`keep if
<condition>` in Stata, except :code:`df[<condition>]` is itself a DataFrame
that can be acted upon independently of :code:`df` itself. *This means that you
now know the general* :code:`if <condition>` *syntax for every other pandas
command.* 

So let's say the second command you know is :code:`df.describe()` which is the
equivalent of Stata's :code:`summary`. This command doesn't have it's own
dedicated :code:`if` command. It doesn't need one. All you need is
:code:`df[<condition>].describe()`.

In this way, you can create (i.e., "compose") new commands. You may notice that
sometimes Python/pandas will require composed commands where Stata uses a
one-liner (for example, see Stata's :code:`drop varstem*` below). While it may
may annoying to type a few more characters, this is actually a good thing! It
means that there are fewer base commands to learn in pandas. It's like learning
an alphabet with 26 letters and composing millions of words instead of learning
millions of individual hieroglyphs.

This also means that sometimes there is more than one way to do things.
Sometimes, it doesn't matter which way you do it. Other times, one way of doing
things will execute more quickly. You can use the :code:`%timeit` magic command
in IPython to easily test which one is faster. But this will usually only an
issue with with larger data sets (usually several gigabytes). For example,
in large Groupby operations :code:`.shift(fillna=0)` is much, much slower than
:code:`shift().fillna(0)` even though the end result is the same.


Input/Output
------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`log using <file>`
     - Python doesn't display results automatically like Stata. You have to
       explicitly call the :code:`print` function. Using a Jupyter notebook is
       the closest equivalent.
   * - :code:`help <command>`
     - #. :code:`help(<command>)` OR
       #. :code:`<command>?` in IPython (as in :code:`pd.read_stata?`)
   * - :code:`cd some/other/directory`
     - | :code:`import os`
       | :code:`os.chdir('some/other/directory')`
       | but this is bad practice. Better practice is to use full pathnames whenever possible.
   * - :code:`use my_file`
     - | :code:`import pandas as pd`
       | :code:`df = pd.read_stata('my_file.dta')`
   * - :code:`use var1 var2 using my_file`
     - :code:`df = pd.read_stata('my_file.dta', columns=['var1', 'var2'])`
   * - :code:`import excel using <excelfile>`
     - :code:`df = pd.read_excel('<excelfile>')`
   * - :code:`import delimited using my_file.csv`
     - :code:`df = pd.read_csv('my_file.csv')`
   * - :code:`save my_file, replace`
     - #. :code:`df.to_stata('my_file.dta')` OR
       #. :code:`df.to_pickle('my_file.pkl')` for Python-native file type.
   * - :code:`outsheet using my_file.csv, comma`
     - :code:`df.to_csv('my_file.csv')`
   * - :code:`export excel using <excel_name>`
     - :code:`df.to_excel('<excel_name>')`


Sample Selection
----------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`keep if <condition>`
     - :code:`df = df[<condition>]`
   * - :code:`keep if a > 7`
     - :code:`df = df[df['a'] > 7]`
   * - :code:`drop if <condition>`
     - :code:`df = df[~(<condition>)]` where :code:`~` is the logical negation
       operator in pandas and numpy (and bitwise negation for Python more
       generally).
   * - :code:`keep if _n == 1`
     - #. :code:`df.first()` OR
       #. :code:`df.iloc[0, :]` Python is a 0-indexed language, so when counting the elements of lists and arrays, you start with 0 instead of 1.
   * - :code:`keep if _n == _N`
     - #. :code:`df = df.last()` OR
       #. :code:`df = df.iloc[-1, :]`
   * - :code:`keep if _n == 7`
     - :code:`df = df.iloc[6, :]` (Remember to count from 0)
   * - :code:`keep if _n <= 10`
     - :code:`df = df.iloc[:9, :]` (Remember to count from 0)
   * - :code:`keep var`
     - :code:`df = df['var']`
   * - :code:`keep var1 var2`
     - :code:`df = df[['var1', 'var2']]`
   * - :code:`keep varstem*`
     - :code:`df = df.filter(like='varstem')`
   * - :code:`drop var`
     - #. :code:`del df['var']` OR
       #. :code:`df = df.drop('var', axis=1)`
   * - :code:`drop var1 var2`
     - :code:`df = df.drop(['var1', 'var2'], axis=1)`
   * - :code:`drop varstem*`
     - :code:`df = df.drop(df.filter(like='varstem*').columns, axis=1)`


Data Info and Summary Statistics
--------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`describe`
     - :code:`df.info()` OR :code:`df.dtypes` just to get data types. Note that
       Python does not have value labels like Stata does.
   * - :code:`describe var`
     - :code:`df['var'].dtype`
   * - :code:`count`
     - #. :code:`df.shape[0]` OR
       #. :code:`len(df)`. Here :code:`df.shape` returns a tuple with the length and width of the DataFrame.
   * - :code:`count if <condition>`
     - #. :code:`df[<condition>].shape[0]` OR
       #. :code:`(<condition>).sum()` if the condition involves a DataFrame, e.g., :code:`(df['age'] > 2).sum()`
   * - :code:`summ var`
     - :code:`df['var'].describe()`
   * - :code:`summ var if <condition>`
     - #. :code:`df[<condition>]['var'].describe()` OR
       #. :code:`df.loc[<condition>, 'var'].describe()`
   * - :code:`summ var [aw = <weight>]`
     - Right now you have to calculate weighted summary stats manually. There
       are also some tools available in the Statsmodels package.
   * - :code:`summ var, d`
     - :code:`df['var'].describe()` plus :code:`df['var'].quantile([.1, .25,
       .5, .75, .9])` or whatever other statistics you want.
   * - :code:`tab var`
     - :code:`df['var'].value_counts()`
   * - :code:`tab var1 var2`
     - 
         #. :code:`pd.crosstab(df['var1'], df['var2'])`
         #. .. code-block:: python3

              df.groupby(['var1', 'var2'])
                .size()
                .unstack('var2')

            Note that the :code:`.unstack(<var2>)` here is purely cosmetic: it
            transforms the data from "long" to "wide" which is how crosstabs
            are usually presented.
   * - :code:`tab <var1> <var2>, summarize(<func>)`
     - .. code-block:: python3

         df.groupby(['var1', 'var2'])
           .agg(<func>)
           .unstack('var2')


Variable Manipulation
---------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`gen newvar = <expression>`
     - :code:`df['newvar'] = <expression>`
   * - :code:`gen newvar = oldvar + 7`
     - :code:`df['newvar'] = df['oldvar'] + 7`
   * - :code:`gen newvar = <expression> if <condition>`
     - :code:`df.loc[<condition>, 'newvar'] = <expression>`.  As with Stata,
       the rows of :code:`df` that don't meet the condition will be missing
       (:code:`numpy.nan`).
   * - :code:`replace var = <expression> if <condition>`
     - :code:`df.loc[<condition>, 'var'] = <expression>`
   * - :code:`rename var newvar`
     - :code:`df = df.rename(columns={'var': 'newvar'})`. You can also directly
       manipulate :code:`df.columns` like a list: :code:`df.columns = ['a',
       'b', 'c']`.
   * - :code:`inlist(var, <val1>, <val2>)`
     - :code:`df['var'].isin((<val1>, <val2>))`
   * - :code:`inrange(var, <val1>, <val2>)`
     - :code:`df['var'].between((<val1>, <val2>))`
   * - :code:`subinstr(<str>, "  ", "_", .)`
     - :code:`df['var'].str.replace(' ', '_')`
   * - :code:`egen newvar = count(var)`
     - :code:`newvar = df['var'].notnull().sum()`. NOTE: For these
       :code:`egen` commands, :code:`newvar` is a full (constant) column in Stata, while it is a scalar in Python. If you want a full constant column on your DataFrame, you can do :code:`df['newvar'] = 7` or whatever the constant is.
   * - :code:`egen <newvar> = max(var)`
     - :code:`<newvar> = df['var'].max()`
   * - :code:`egen <newvar> = mean(var)`
     - :code:`<newvar> = df['var'].mean()`
   * - :code:`egen <newvar> = total(var)`
     - :code:`<newvar> = df['var'].sum()`
   * - :code:`egen <newvar> = group(var1 var2)`
     - :code:`<newvar> = econtools.group_id(df, cols=['var1', 'var2])` Please see the documentation for :code:`group_id`.
   * - :code:`egen newvar = <stat>(var), by(groupvar1 groupvar2)`
     - :code:`df['newvar']  = df.groupby(['groupvar1', 'groupvar2'])['var'].transform('<stat>')`.
   * - | :code:`collapse (sd) var (median) var ///`
       |    :code:`(max) var (min) var, ///`
       |    :code:`by(groupvar1 groupvar2)`
     - :code:`df.groupby(['groupvar1', 'groupvar2'])['var'].agg(['std', 'median', 'min', 'max', 'sum'])`
   * - :code:`collapse (<stat>) var [iw = <weight>]`
     - Manually or maybe Statsmodels has a tool.
   * - :code:`collapse (mean) var1, var2, by(groupvar1 groupvar2)`
     - :code:`df.groupby(['groupvar1', 'groupvar2'])[['var1', 'var2']].mean()`
   * - :code:`recode var (1/5 = 1)`
     - N/A, see note below. 
   * - :code:`recode var (1/5 = 1), gen(<newvar>)`
     - N/A. 
   * - :code:`label var var <label>`
     - N/A. 
   * - :code:`label define <labelname> 1 <valuelabel>`
     - N/A.
   * - :code:`label values var <labelname>`
     - N/A. 
   * - :code:`label list <labelname>`
     - N/A. 

Python doesn't have "labels" built into DataFrames like Stata does. However,
you can use a dictionary to map data values to labels when necessary.

.. code-block:: python3

    variable_labels = {
        1: "First Category",
        2: "Second Category",
        3: "Last Category",
    }



Bysort
------

All :code:`bysort` and :code:`egen` commands will be compositions using
:code:`groupby.agg` or :code:`groupby.transform`

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`bys group_var1 group_var2: gen group_sum = sum(var)`
     - #. :code:`df['group_sum'] = df.groupby(['group_var1', 'group_var2'])['var'].transform('sum')` 
       #. :code:`df['group_sum'] = df.groupby(['group_var1', 'group_var2'])['var'].transform(np.sum)` Note that :code:`transform` can take a string name of common functions like sum, mean, etc., or an arbitrary function to be executed, including :code:`np.sum` or a function of your own creation.
   * - :code:`bys group_var1 group_var2 (sort_var): keep if _n==1`
     - #. .. code-block:: python3

             df['group_sum'] = (
                 df
                 .sort_values(['group_var1', 'group_var2', 'sort_var1'])
                 .drop_duplicates(['group_var1', 'group_var2'], keep='first')
             )

       #. .. code-block:: python3

             df['group_sum'] = (
                 df
                 .sort_values(['group_var1', 'group_var2', 'sort_var1'])
                 .groupby(['var1', 'var2'])
                 .first()
             )

   * - :code:`bys group_var1 group_var2 (sort_var): keep if _n==j` where
       :code:`j` is some arbitrary number
     - .. code-block:: python3

          df['group_sum'] = (
              df
              .sort_values(['group_var1', 'group_var2', 'sort_var1'])
              .groupby(['var1', 'var2'])
              .apply(lambda x: x.iloc[j, :])
          )

   * - :code:`bys group_var1 group_var2 (sort_var): gen jth_val = var[j]` where
       :code:`j` is some arbitrary number
     - .. code-block:: python3

          df['jth_val'] = (
              df
              .sort_values(['group_var1', 'group_var2', 'sort_var1'])
              .groupby(['var1', 'var2'])['var']
              .transform(lambda x: x.iloc[j])
          )


Note that :code:`groupby` was also used above to accomplish a :code:`collapse`.
Like, a Stata Collapse, a pandas Groupby reduces the size of the data set. If
you want to instead execute what's called a window function in SQL, which does
not reduce the shape of the original data set, you can call
:code:`df.groupby.transform(<function>)` instead of
:code:`df.groupby.agg(<function>)`.

If for some reason :code:`transform` doesn't work in your use case, you can
also re-join the collapsed data back onto your original data set:

.. code-block:: python3

    df = pd.read_csv('my_data.csv')
    state_pop_sum = df.groupby('state')['population'].sum()
    df = df.join(state_pop_sum.to_frame('state_pop_sum'),     # Give the new column a name besides 'population'
                 on='state')





Panel Data
----------

There is no general equivalent to :code:`tsset` in Python. However, you can
accomplish most if not all of the same tasks using a DataFrame's index (the
row's equivalent of columns.) In Stata, the "DataFrame" in memory always has
the observation row number, denoted by the Stata built-in variable :code:`_n`.
In Python and Pandas, a DataFrame index can be anything (though you can also
refer to rows by the row number; see :code:`.loc` vs :code:`iloc`). It can also
be hierarchical with mutiple levels. It is a much more general tool than
:code:`tsset`.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`tsset panelvar timevar`
     - :code:`df = df.set_index(['panelvar', 'timevar'])`
   * - :code:`L.var`
     - :code:`df['var'].shift()` NOTE: The index must be
       correctly sorted for :code:`shift` to work the way you want it to. You
       will also probably need to use a :code:`groupby`; see below.
   * - :code:`L2.var`
     - :code:`df['var'].shift(2)`
   * - :code:`F.var`
     - :code:`df['var'].shift(-1)`


Examples
~~~~~~~~

.. code-block:: ipythonconsole

    In [1]: import numpy as np

    In [2]: import pandas as pd

    In [3]: df0 = pd.DataFrame({'var1': np.arange(6),
       ...:                     'id': [1, 1, 2, 2, 3, 3],
       ...:                     'period': [0, 1] * 3})

    In [4]: print(df0)
       var1  id  period
    0     0   1       0
    1     1   1       1
    2     2   2       0
    3     3   2       1
    4     4   3       0
    5     5   3       1

    In [5]: df = df0.set_index(['id', 'period']).sort_index()

    In [6]: print(df)
               var1
    id period
    1  0          0
       1          1
    2  0          2
       1          3
    3  0          4
       1          5

    In [7]: df['var1_lag'] = df.groupby(level='id')['var1'].shift()

    In [8]: print(df)
               var1  var1_lag
    id period
    1  0          0       NaN
       1          1       0.0
    2  0          2       NaN
       1          3       2.0
    3  0          4       NaN
       1          5       4.0

    In [9]: df['var1_for'] = df.groupby(level='id')['var1'].shift(-1)

    In [10]: print(df)
               var1  var1_lag  var1_for
    id period
    1  0          0       NaN       1.0
       1          1       0.0       NaN
    2  0          2       NaN       3.0
       1          3       2.0       NaN
    3  0          4       NaN       5.0
       1          5       4.0       NaN


Merging and Joining
-------------------

NOTE: Merging in Python is like R, SQL, etc. See additional explanation below.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`append using <filename>`
     - :code:`df_joint = df1.append(df2)`
   * - :code:`merge 1:1 <vars> using <filename>`
     - #. :code:`df_joint = df1.join(df2)` if :code:`<vars>` are the DataFrames' indexes, or
       #. :code:`df_joint = pd.merge(df1, df2, on=<vars>)` otherwise. Beware that :code:`pd.merge` will not keep the index of either DataFrame.


Merging with Pandas DataFrames does not require you to specify "many-to-one" or
"one-to-many". Pandas will figure that out based on whether the variables
you're merging on are unique or not. However, you can specify what sub-sample
of the merge to keep using the keyword argument :code:`how`, e.g.,
:code:`df_joint = df1.join(df2, how='left')` is the default for :code:`join`
while :code:`how='inner'` is the default for :code:`pd.merge`.

.. list-table::
   :widths: 30 30 50
   :header-rows: 1

   * - Pandas :code:`how`
     - Stata :code:`, keep()`
     - Intuition
   * - :code:`how='left'`
     - :code:`keep(1, 3)`
     - Keeps all observations in the "left" DataFrame.
   * - :code:`how='right'`
     - :code:`keep(2, 3)`
     - Keeps all observations in the "right" DataFrame.
   * - :code:`how='inner'`
     - :code:`keep(3)`
     - Keeps observations that are in both DataFrames.
   * - :code:`how='outer'`
     - :code:`keep(1 2 3)`
     - Keeps all observations.


Reshape
-------

Like with merging, reshaping a DataFrame in Python is a bit different because
of the paradigm shift from the "only one data table in memory" model of Stata
to "a data table is just another object/variable" of Python. But this
difference also makes reshaping a little easier in Python.

The most fundamental reshape commands in Python/pandas are :code:`stack` and
:code:`unstack`:


.. code-block:: ipythonconsole

    In [1]: import pandas as pd

    In [2]: import numpy as np

    In [3]: long = pd.DataFrame(np.arange(8),
       ...:                     columns=['some_variable'],
       ...:                     index=pd.MultiIndex.from_tuples(
       ...:                         [('a', 1), ('a', 2),
       ...:                          ('b', 1), ('b', 2),
       ...:                          ('c', 1), ('c', 2),
       ...:                          ('d', 1), ('d', 2)]))

    In [4]: long.index.names=['unit_id', 'time']

    In [5]: long.columns.name = 'varname'

    In [6]: long
    Out[6]:
    varname       some_variable
    unit_id time
    a       1                 0
            2                 1
    b       1                 2
            2                 3
    c       1                 4
            2                 5
    d       1                 6
            2                 7

    In [7]: wide = long.unstack('time')

    In [8]: wide
    Out[8]:
    varname some_variable
    time                1  2
    unit_id
    a                   0  1
    b                   2  3
    c                   4  5
    d                   6  7

    In [9]: long2 = wide.stack('time')

    In [10]: long2
    Out[10]:
    varname       some_variable
    unit_id time
    a       1                 0
            2                 1
    b       1                 2
            2                 3
    c       1                 4
            2                 5
    d       1                 6
            2                 7

Here Input 3 creates a DataFrame, Input 4 gives each of the index columns a
name, and Input 5 names the columns. Coming from Stata, it's a little weird to
think of the column names themselves having a "name", but the columns names are
just an index like the row names are. It starts to make more sense when you
realize columns don't have to be strings. They can be integers, like years or
FIPS codes. In those cases, it makes a lot of sense to give the columns a name
so you know what you're dealing with.

Input 6 does the reshaping using :code:`unstack('time')`, which takes the index
:code:`'time'` and creates a new column for every unique value it has. Notice
that the columns now have multiple levels, just like the index previously did.
This is another good reason to label your index and columns. If you want to
access either of those columns, you can do so as usual, using a tuple to
differentiate between the two levels:

.. code-block:: ipythonconsole

    In [11]: wide[('some_variable', 1)]
    Out[11]:
    unit_id
    a    0
    b    2
    c    4
    d    6
    Name: (some_variable, 1), dtype: int32


If you want to combine the two levels (like Stata defaults to), you can simply
rename the columns:

.. code-block:: ipythonconsole

    In [13]: wide_single_level_column = wide.copy()

    In [14]: wide_single_level_column.columns = [
        ...:        '{}_{}'.format(var, time)
        ...:        for var, time in wide_single_level_column.columns]

    In [15]: wide_single_level_column
    Out[15]:
                      some_variable_1  some_variable_2
             unit_id
             a                      0                1
             b                      2                3
             c                      4                5
             d                      6                7


The :code:`pivot` command can also be useful, but it's a bit more complicated than :code:`stack` and
:code:`unstack` and is better to revisit :code:`pivot` after you are
comfortable working with DataFrame indexes and columns.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`reshape <wide/long> <stubs>, i(<i_vars>) j(<j_var>)`
     - | wide: :code:`df.unstack(<level>)`
       | long: :code:`df.stack('j_var')`
       | see also :code:`df.pivot`


Econometrics
------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`ttest var1, by(var2)`
     - | :code:`from scipy.stats import ttest_ind`
       | :code:`ttest_ind(array1, array2)`
   * - :code:`xi: i.var`
     - :code:`pd.get_dummies(df['var'])`
   * - :code:`i.var2#c.var1`
     - :code:`pd.get_dummies(df[var2]).multiply(df[var1])`
   * - :code:`reg yvar xvar if <condition>, r`
     - | :code:`import econtools.metrics as mt`
       | :code:`results = mt.reg(df[<condition>], 'yvar', 'xvar', robust=True)`
   * - :code:`reg yvar xvar if <condition>,  vce(cluster cluster_var)`
     - :code:`results = mt.reg(df[<condition>], 'yvar', 'xvar', cluster='cluster_var')`
   * - :code:`areg yvar xvar1 xvar2, absorb(fe_var)`
     - :code:`results = mt.reg(df, 'yvar', ['xvar1', 'xvar2'], fe_name='fe_var')`
   * - :code:`predict newvar, resid`
     - :code:`newvar = results.resid`
   * - :code:`predict newvar, xb`
     - :code:`newvar = results.yhat`
   * - :code:`_b[var]`, :code:`_se[var]`
     - :code:`results.beta['var']`, :code:`results.se['var']`
   * - :code:`test var1 var2`
     - :code:`results.Ftest(['var1', 'var2'])`
   * - :code:`test var1 var2, equal`
     - :code:`results.Ftest(['var1', 'var2'], equal=True)`
   * - :code:`lincom var1 + var2`
     - :code:`econtools.metrics.f_test` with appropriate parameters.
   * - :code:`ivreg2`
     - :code:`econtools.metrics.ivreg`
   * - :code:`outreg2`
     - :code:`econtools.outreg`
   * - :code:`reghdfe`
     - None (hoping to add it to Econtools soon).


Plotting
--------

Visualizations are best handled by the packages Matplotlib and Seaborn.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`binscatter`
     - :code:`econtools.binscatter`
   * - :code:`maptile`
     - No quick tool, but easy to do with Cartopy.
   * - :code:`coefplot`
     - :code:`ax.scatter(results.beta.index, results.beta)` often works. Depends on context.
   * - :code:`twoway scatter y_var x_var`
     - :code:`df.scatter('x_var', 'y_var')`
   * - :code:`twoway scatter y_var x_var if <condition>`
     - :code:`df[<condition>].scatter(x_var, y_var)`
   * - :code:`twoway <connected/line/area/bar/rarea>`
     - As above with appropriate parameters passed to :code:`df.plot` function.
       However, it is better to use :code:`matplotlib` or :code:`seaborn`
       directly and call :code:`ax.plot(df['var1'], df['var2'])`. Like with
       :code:`merge`, it's a different paradigm that needs more explanation.

Other differences
-----------------

Missing values
~~~~~~~~~~~~~~

In Python, missing values are represented by a NumPy "not a number" object,
:code:`np.nan`. In Stata, missing (:code:`.`) is larger than every number, so
:code:`10 < .` yields True. In Python, :code:`np.nan` is never equal to
anything. Any comparison involving :code:`np.nan` is always False, even
:code:`np.nan == np.nan`.

To look for missing values in DataFrame columns, use any of the following.

* :code:`df[<varname>].isnull()` returns a vector of True and False values for each
  row of :code:`df[<varname>`.
* :code:`df[<varname>].notnull()` is the complement of :code:`.isnull()`.
* The function :code:`np.isnan(<arraylike>)` takes an array and returns True or
  False for each element of the array (a DataFrame is a special type of array).

Another important difference is that :code:`np.nan` is a floating point data
type, so any column of a DataFrame that contains missing numbers will be
floats. If a column of integers gets changed so that even one element is
:code:`np.nan`, the whole column will be converted to floats.


Floating point equality
~~~~~~~~~~~~~~~~~~~~~~~

In Stata, decimal numbers are never equal to anything, e.g., :code:`3.0 == 3` is
False. In Python, the above equality check returns True as long as the floating
point error is within tolerances. However, you should be wary when
doing large-scale equality checks using floats, like when merging two data sets
using a variable/column that is a float. This is true for any language!  (Read
up on floating point error if you're curious why measuring equality of floats
is tricky.)
