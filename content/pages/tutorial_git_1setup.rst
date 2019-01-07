:Title: Setting up Git
:slug: tutorial_git_1setup
:series: GIT_TUTORIAL
:series_index: 2

.. sectnum::

A Brief Intro to Git:

* `Overview <tutorial_git_0overview.html>`__
* Next: `First Steps: Making Commits <tutorial_git_2commits.html>`__

------

First, make sure you can access git from the command line by executing the
following command:

.. code-block:: shell-session
    
    $ git --version

You should see something like this:

.. code-block:: shell-session

    $ git --version
    git version 2.17.1.windows.2

If instead you see :code:`bash: git: command not found`, double check you have git
installed. [Coming soon: Tutoral on installation and making sure this works.]

Second, configure git to fit you.
Instead of a options menu, git is configured through a :code:`.gitconfig` file
in your home directory.
You can quickly set it up by copying the following settings into your
:code:`.gitconfig` file:

.. code-block:: linux-config

    [user]
            name = Firstname Lastname               # Fill this in
            email = me@mailhost.com                 # Fill this in
    [push]
            default = matching
    [core]
            excludesfile = ~/.gitignore_global
            autocrlf = false
            fileMode = false
            editor = atom                           # Fill this in
    [color]
            ui = true
    [difftool]
            prompt = false
    [alias]
            st = status
            ci = commit
            ch = checkout
            br = branch -vva
            shortlog = log --graph --abbrev-commit --decorate --date=relative --format=format:'%C(bold blue)%h%C(reset) - %C(bold yellow)%d%C(reset) %C(white)%s%C(reset)' --all


Double check that your :code:`.gitconfig` is ready by running this command:

.. code-block:: shell-session

    $ cat ~/.gitconfig

The :code:`cat` command will print the file on your screen. You can also use :code:`git config --list`.


.. list-table:: Frozen Delights!
   :widths: 40 60
   :header-rows: 1

   * - Stata
     - Python
   * - :code:`log using <file>`
     - Python doesn't display results automatically like Stata. You have to
       explicitly call the :code:`print` function. Using a Jupyter notebook is
       the closest equivalent.
   * - :code:`cd <directory>`
     - :code:`import os; os.chdir('<directory>')`, but this is bad practice.
       Better practice is to use full pathnames whenever possible.
   * - :code:`use <dtafile>`
     - :code:`import pandas as pd; df = pd.read_stata('<dtafile>')`
   * - :code:`import excel using <excelfile>`
     - :code:`df = pd.read_excel('<excelfile>')`
   * - :code:`import delimited using <csvfile>`
     - :code:`df = pd.read_csv('<csvfile>')`
   * - :code:`desc`
     - :code:`df.dtypes` Note that Python does not have value labels like Stata does.
   * - :code:`desc <var>`
     - :code:`df[<var>].dtype`
   * - :code:`count`
     - :code:`df.shape[0]` OR :code:`len(df)`. Here :code:`df.shape` returns a
       tuple with the length and width of the DataFrame.
   * - :code:`count if <condition>`
     - :code:`df[<condition>].shape` OR :code:`(<condition>).sum()` if the condition involves a DataFrame, e.g., :code:`(df['age'] > 2).sum()`
   * - :code:`summ <var>`
     - :code:`df['<var>'].describe()`
   * - :code:`summ <var> if <condition>`
     - :code:`df[<condition>][<var>].describe()` OR :code:`df.loc[<condition>, <var>]. describe()`
   * - :code:`summ <var> [aw = <weight>]`
     - Right now you have to calculate weighted summary stats manually. There
       are also some tools available in the Statsmodels package.
   * - | :code:`collapse (sd) <var> (median) <var> ///`
       |    :code:`(max) <var> (min) <var>, ///`
       |    :code:`by(<groupvars>)`
     - :code:`df.groupby('<groupvars>')['<var>'].agg(['std', 'median', 'min', 'max', 'sum'])`

