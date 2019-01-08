:Title: Translating Stata to Python
:slug: tutorial_stata_to_python

.. sectnum::

.. contents::
    :depth: 1

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
   * - :code:`cd <directory>`
     - | :code:`import os`
       | :code:`os.chdir('<directory>')`
       | but this is bad practice. Better practice is to use full pathnames whenever possible.
   * - :code:`use <dtafile>`
     - | :code:`import pandas as pd`
       | :code:`df = pd.read_stata('<dtafile>')`
   * - :code:`import excel using <excelfile>`
     - :code:`df = pd.read_excel('<excelfile>')`
   * - :code:`import delimited using <csvfile>`
     - :code:`df = pd.read_csv('<csvfile>')`
   * - :code:`save <filename> [, replace]`
     - | :code:`df.to_stata(<filename>)` OR
       | :code:`df.to_pickle(<filename>)` for Python-native file type.
   * - :code:`outsheet using <csv_name>, comma`
     - :code:`df.to_csv(<csv_name>)`
   * - :code:`export excel using <excel_name>`
     - :code:`df.to_excel(<excel_name>)`


Sample Selection
----------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`keep if <condition>`
     - :code:`df = df[<condition>]`
   * - :code:`drop if <condition>`
     - :code:`df = df[~(<condition>)]`
   * - :code:`keep <var>`
     - :code:`df = df['var']`
   * - :code:`keep varstem*`
     - :code:`df = df.filter(like='varstem*')`
   * - :code:`drop <var>`
     - :code:`del df['var']` OR :code:`df = df.drop('var', axis=1)`
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
   * - :code:`describe <var>`
     - :code:`df[<var>].dtype`
   * - :code:`count`
     - :code:`df.shape[0]` OR :code:`len(df)`. Here :code:`df.shape` returns a
       tuple with the length and width of the DataFrame.
   * - :code:`count if <condition>`
     - :code:`df[<condition>].shape[0]` OR :code:`(<condition>).sum()` if the
       condition involves a DataFrame, e.g., :code:`(df['age'] > 2).sum()`
   * - :code:`summ <var>`
     - :code:`df['<var>'].describe()`
   * - :code:`summ <var> if <condition>`
     - :code:`df[<condition>][<var>].describe()` OR :code:`df.loc[<condition>, <var>]. describe()`
   * - :code:`summ <var> [aw = <weight>]`
     - Right now you have to calculate weighted summary stats manually. There
       are also some tools available in the Statsmodels package.
   * - :code:`summ <var>, d`
     - :code:`df[<var>].describe()` plus :code:`df[<var>].quantile([.1, .25,
       .5, .75, .9])` or whatever other statistics you want.


Variable Manipulation
---------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`gen <newvar> = <expression>`
     - :code:`df[<newvar>] = <expression>`
   * - :code:`gen <newvar> = <expression> if <condition>`
     - :code:`df.loc[<condition>, 'var'] = <expression>`.  As with Stata, the
       rows of :code:`df` that don't meet the condition will be missing
       (:code:`numpy.nan`).
   * - :code:`replace <var> = <expression> if <condition>`
     - :code:`df.loc[<condition>, <var>] = <expression>`
   * - :code:`rename <var> <newvar>`
     - :code:`df = df.rename(columns={<var>: <newvar>})`
   * - :code:`<var>*`
     - Depends on context
   * - :code:`egen <newvar> = count(<var>)`
     - :code:`<newvar> = df[<var>].notnull().sum()`
   * - :code:`egen <newvar> = group(<varlist>)`
     - :code:`<newvar> = econtools.group_id(df, cols=<varlist>)`
   * - :code:`egen <newvar> = max(<var>)`
     - :code:`<newvar> = df[<var>].max()`
   * - :code:`egen <newvar> = mean(<var>)`
     - :code:`<newvar> = df[<var>].mean()`
   * - :code:`egen <newvar> = total(<var>)`
     - :code:`<newvar> = df[<var>].sum()`
   * - :code:`inlist(<var>, <val1>, <val2>)`
     - :code:`<var_name> = df[<var>].isin((<val1>, <val2>))`
   * - :code:`inrange(<var>, <val1>, <val2>)`
     - :code:`<var_name> = df[<var>].between((<val1>, <val2>))`
   * - :code:`subinstr(<str>, "  ", "_", .)`
     - :code:`df[<var>] = df[<var>].str.replace(' ', '_')`
   * - :code:`egen <newvar> = <total/mean/max>(<var>), by(<groupvars>)`
     - :code:`df.groupby(<groupvars>)[<var>].<stat>()`
   * - | :code:`collapse (sd) <var> (median) <var> ///`
       |    :code:`(max) <var> (min) <var>, ///`
       |    :code:`by(<groupvars>)`
     - :code:`df.groupby(<groupvars>)[<var>].agg(['std', 'median', 'min', 'max', 'sum'])`
   * - :code:`collapse (<stat>) <var> [iw = <weight>]`
     - Manually or maybe through Statsmodels tool.
   * - :code:`collapse (<stat>) <stat_vars>, by(<groupvars>)`
     - :code:`df.groupby(<groupvars>)[<stat_vars>].<stat>()`
   * - :code:`recode <var> (1/5 = 1)`
     - N/A. 
   * - :code:`recode <var> (1/5 = 1), gen(<newvar>)`
     - N/A. 
   * - :code:`label var <var> <label>`
     - N/A. 
   * - :code:`label define <labelname> 1 <valuelabel>`
     - N/A.
   * - :code:`label values <var> <labelname>`
     - N/A. 
   * - :code:`label list <labelname>`
     - N/A. 


Panel Data
----------

There is no general equivalent to :code:`tsset` in Python. The equivalent
functionality is provided by a DataFrame's index, the row's equivalent of
columns. A DataFrame index can have arbitrary contents and can be hierarchical
with mutiple levels. It is a much more general tool than :code:`tsset`.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`tsset <panelvar> <timevar>`
     - :code:`df = df.set_index([<panelvar>, <timevar>])`
   * - :code:`L.<var>`
     - :code:`df.shift()`
   * - :code:`L2.<var>`
     - :code:`df.shift(2)`
   * - :code:`F.<var>`
     - :code:`df.shift(-1)`

Examples
~~~~~~~~~~~~

.. code-block:: ipython
    :linenos: table

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

    In [5]: df = df0.set_index(['id', 'period'])

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

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`merge 1:1 <vars> using <filename>`
     - :code:`df_joint = df1.join(df2)` NOTE: Merging in Python is like R, SQL,
       etc. Needs more robust explanation.
   * - :code:`append using <filename>`
     - :code:`df_joint = df1.append(df2)`



Reshape
-------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`reshape <wide/long> <stubs>, i(<vars>) j(<var>)`
     - | wide: :code:`df.unstack(<level>)`
       | long: :code:`df.stack(<column_level>)`
       | see also :code:`df.pivot`



Econometrics
------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`ttest <var>, by(<var>)`
     - | :code:`from scipy.stats import ttest_ind`
       | :code:`ttest_ind(<array1>, <array2>)`
   * - :code:`xi: i.<var>`
     - :code:`pd.get_dummies(df[<var>])`
   * - :code:`i.<var>#c.<var>`
     - :code:`df[<var1>] * pd.get_dummies(df[<var2>])`
   * - :code:`reg <yvar> <xvar> if <condition>, r`
     - | :code:`import econtools.metrics as mt`
       | :code:`results = mt.reg(df[<condition>], <yvar>, <xvar>, robust=True)`
   * - :code:`reg <yvar> <xvar> if <condition>,  vce(cluster <clustervar>)`
     - :code:`results = mt.reg(df[<condition>], <yvar>, <xvar>, cluster=<clustervar>)`
   * - :code:`predict <newvar>, resid`
     - :code:`<newvar> = results.resid`
   * - :code:`predict <newvar>, xb`
     - :code:`<newvar> = results.yhat`
   * - :code:`_b[<var>]`, :code:`_se[<var>]`
     - :code:`results.beta[<var>]`, :code:`results.se[<var>]`
   * - :code:`test <varlist>`
     - :code:`results.Ftest(<varlist>)`
   * - :code:`test <varlist>, equal`
     - :code:`results.Ftest(<varlist>, equal=True)`
   * - :code:`lincom <var1> + <var2>`
     - :code:`econtools.metrics.f_test` with appropriate parameters.
   * - :code:`ivreg2`
     - :code:`econtools.metrics.ivreg`
   * - :code:`outreg2`
     - :code:`econtools.outreg`
   * - :code:`reghdfe`
     - None.


Plotting
--------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`binscatter`
     - :code:`econtools.binscatter`
   * - :code:`maptile`
     - No quick tool, but easy to do.
   * - :code:`coefplot`
     - :code:`ax.scatter(results.beta.index, results.beta)` often works. Depends on context.
   * - :code:`twoway scatter <var1> <var2>`
     - :code:`df.scatter(<var2>, <var1>)`
   * - :code:`twoway scatter <var1> <var2> if <condition>`
     - :code:`df[<condition>].scatter(<var2>, <var1>)`
   * - :code:`twoway <connected/line/area/bar/rarea>`
     - As above, though :code:`ax.plot(<var1>, <var2>)` is better. Like merge,
       it's a different paradigm, needs more explanation.
