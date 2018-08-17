:Title: Project File Organization
:slug: tutorial_workflow_2project_org

.. sectnum::


* `Writing Code in Econ Overview <tutorial_workflow_0overview.html>`__
* Previous: `Software Setup <tutorial_workflow_1setup.html>`__
* Next: TBD

.. contents::

..

    Never memorize anything you can look up.
    ~ Albert Einstein, maybe

It's a good idea to keep your code organized. As projects get bigger, and as
you step away from them and return, it's easier to get lost.  A corollary to
the supposed Einstein quote is "never memorize anything you can re-derive when
you need it." It's easier to come back to code after a long time and go through
logic like "a script like X would probably be in folder Y" than it is to read
through every file and every folder searching for X.

The file and folder structure outlined here is one way to do that.


Data-only project
-----------------

An important principle in coding is to only define something once, whether it's
a variable or a function, and refer back to that singular definition everywhere
else. No copying and pasting snippets of code! If you find an error in a
sequence of code you've copied-and-pasted to 5 other files, you'd better hope
you remember what those files are. This "do it once and never do it again"
principle includes code that accesses data files, which is a lot of what we do.

To this end, we will write a separate (usually small) Python package for each
major data source we use. This will make it easy to use the data again and
again across different projects without copying and pasting.

The folders in such a project will generally look like this:

:: 

    data-project-name/
    |── setup.py
    |── data_project_name/
        |── __init__.py
        |── util/
        |   |── __init__.py
        |   |── env.py
        |── clean/
            |── __init__.py
            |── raw.py

The top-level :code:`data-project-name` is a Git repository that contains
everything else. The folder with the same name (substituting dashes for
underscores) just underneath it is the Python package within the Git
repository. They don't have to be the same, but it makes things easier. The
:code:`setup.py` script is a boilerplate script used to install a Python
package so that it can be referenced in any other Python script on the
computer. 

The :code:`__init__.py` files will usually be empty and are there to let Python
know that the folder is part of a Python package (see `here
<https://stackoverflow.com/questions/448271/what-is-init-py-for>`__).

Where's the data?
~~~~~~~~~~~~~~~~~

Notice that there's no :code:`data` folder here. That's because the data files
are (usually ) not kept in the Python package or the Git repository.
First, they often can't be, since raw data files can be several gigabytes which
would make hosting the repository online at Github or Bitbucket difficult.
Second, they don't need to be, as we'll see with the :code:`data_path` function
below.
Since the data files often can't be stored in the repo, and never *have* to be
stored there, it's easiest to be uniform across all projects and just put the
data *somewhere* on your hard drive and point the rest of your code to where
that is (using the :code:`data_path` function, explained below).

The folder where the data files are stored still has a set structure:

::
    
    mass-data-folder-on-big-hard-drive/
    |── data-project-name-data/
    |   |── src/
    |   |── clean_file_1.dta
    |   |── clean_file_2.dta
    |── other-data-project-name/
        |── src/

The key principle here is to preserve the source data for each project which is
kept in :code:`src`. The rule is that raw data goes from the BLS website or
where ever it came from straight into :code:`src` and the raw files are never
touched again. *Never manually edit the raw CSV files.* All cleaning is
programmatic, which means that you should be able to download the data fresh
from the source and immediately run the code.  files from :code:`src` and save
them to :code:`data-project-name-data`. That way you know that anything not in
:code:`src` was created by you and can be deleted as long as you still have the
code that created the file in the first place.


Define data locations once (and only once)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :code:`util` folder is for scripts that will be used a lot within the data
cleaning itself but not by any other Python code or projects. In fact,
:code:`util` will often just contain a single file, :code:`env.py`. The
:code:`util/env.py` file contains environmental variables for the project,
hence the name. These are variables like where on the hard drive the raw data
are stored.  A basic :code:`util/env.py` file looks like this:

.. code-block:: python3

    import os

    data_root = r'd:/'
    DATA_PATH = os.path.join(data_root, 'Data', 'data-project-name')

    def data_path(*args):
        return os.path.join(DATA_PATH, *args)

    def src_path(*args):
        return data_path('src', *args)


The :code:`src_path` and :code:`data_path` functions take a file name as a
string and appends all the folder information to it, so all you need to worry
about is the name of the actual file, not all the folders. The basic use of the
functions looks like this.

.. code-block:: ipython3

    In [1]: from util.env import data_path

    In [2]: print(data_path('main_file.dta'))
    Out[2]: 'd:\\Data\\data-project-name\\main_file.dta'

These functions are *the* canonical definitions of where the data files are
found on the computer.  All other scripts will refer to these definitions by
importing them. For example, a function that cleans and saves a dataset might
look like this:

.. code-block:: python3

    import pandas as pd

    from util.env import src_path, data_path

    def clean_gdp_data():
        # Read data from raw CSV file
        df = pd.read_csv(src_path('annual_gdp.csv'))

        # Fudge the numbers
        df['gdp'] = df['gdp'] * 2

        # Save to Stata DTA
        df.to_stata(data_path('annual_gdp.dta'))

    if __name__ == '__main__':
        clean_gdp_data()

If you're working with big data files and have lots of people on your team, you
can use Python's builtin :code:`socket` library to code if-then statements that
change the :code:`data_root` variable depending on the name of the computer
running the code.

**NOTE:** These :code:`data_path` and :code:`src_path` functions should *never*
be used in code outside :code:`data_project_name`. Other projects will have
their own data access functions.


Pull it all together
~~~~~~~~~~~~~~~~~~~~

The :code:`clean` folder contains scripts that clean the raw data. 
Usually we'll call the barebones basic script that reads the source data
:code:`raw.py`, but sometimes that's all there is. If it's a very simple
project, there may be a `clean.py` file instead of a folder.

Finally, after all the cleaning functions are written, we'll import them into
the project-level :code:`__init__.py` file like this:

.. code-block:: python3

    from clean.raw import load_data_1, load_data_2  # etc.

That way we don't have to worry about the interal file structure of
:code:`data-project-name` when we're using the data package in other projects.
Did :code:`data-project-name` use a :code:`clean.py` file or a :code:`clean`
folder? Did it use any other folders? If we import any externally facing
functions into the project-level :code:`__init__.py`, it doesn't matter. All we
have to do in other projects is

.. code-block:: python3

    from code_package_name import load_data_1

This is the advantage of installing the package using :code:`setup.py` and
making the data package accessible to any other scripts. You don't have to
remember the details of the cleaning code beyond the specific function you
want, and for that you just have to look in a single :code:`__init__.py` file.


Full empirical project
----------------------

Full projects that form the basis of an academic paper are structured in a
similar way.

:: 

    project-name/
    |── draft/              <- Is a Git repo
    |── present/            <- Maybe a Git repo
    |── lit/
    |── data/
    |   |── src/
    |── out/
    |   |── 1807/
    |   |── 1808/
    |       |── plot_variable.png
    |       |── reg_main.tex
    |── code/               <- Is a Git repo
        |── util/
        |   |── env.py
        |── clean/
        |── analysis/
        |── driver.sh
        |── summ_a_variable.py
        |── plot_a_variable.py
        |── reg_main.py


The :code:`data/` folder is for incidental data that is specific to this
project. If it's data like CPI data or Census data that's likely to be used
again and again, it should be in its own data-only project. 

The :code:`draft/` folder is for drafts of the paper if/when we get that far,
including :code:`bib` files and anything else that goes with the draft.  Same
goes for :code:`present/` (presentations) and :code:`lit/` (other papers from
the literature we'll need to refer to).

Output path
~~~~~~~~~~~

The :code:`util` folder is the same as above. The :code:`util/env.py` file will
also have an :code:`out_path` function that defines where we want the output of
analyses saved.  This will usually just point to the :code:`out/` folder,
however we will often keep the :code:`out/` folder on Dropbox so we can always
access our results. Actual figures and tables are saved in individual folders
within :code:`out/` depending on the month the file was generated, e.g., 1808
for August 2018. Adding the month-year folder is handled automatically by
:code:`out_path`.

Code organization
~~~~~~~~~~~~~~~~~

Python makes it very easy to import functions from one file into another.
One danger of this that you can get circular imports, where Script A imports
from Script B and Script B imports from Script A. Python will raise an error if
this happens. This is surprisingly easy to do once you get nested imports,
where A imports B imports C and so on.

To avoid this, the :code:`code/` folder has a hierarchical structure:

#. :code:`util/`: useful utility functions that will be used a lot all over the
   package. Things like coordinate converters or ID generators. Scripts in
   :code:`util/` *never* import from other scripts in the project. That way you
   know that any other script can use the tools in :code:`util/`. It's a
   universal donor to other scripts and never receives from them.
#. :code:`clean/`: for incidental data cleaning. Can import from :code:`util/`
   but that's it.
#. :code:`analysis/`: This is for prepping regression files and the like.
   Remember to define things once and only once. This goes for regression
   samples, too, and :code:`analysis` is the place to put them. Can import from
   :code:`util/` and :code:`clean/`.
#. The root folder, :code:`code/`: this is where we put scripts that create
   final output. Regressions, figures, summary stats, all here. These scripts
   can import from anywhere else in the project and they should never be
   imported from. If you write a function in `reg_main.py` that you want to use
   somehwere else, move it to :code:`analysis` first.

    The final output scripts in :code:`code/` are prefixed by what they do,
    :code:`summ_` for summary stats, :code:`plot_` for plots, etc.

Finally, there's :code:`driver.sh`. In theory, this is a simple script that if
run would ideally create all the final tables and figures for our paper. In
practice, the script is never run but serves as a shopping list of sorts to
remind us of the command line options, etc., that we've settled on. A simple
example is:

.. code-block:: bash

    #! /bin/bash

    python reg_main.py --lag 3
    python plot_a_variable.py --grayscale
