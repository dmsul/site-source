:Title: Project File Organization
:slug: tutorial_workflow_2project_org

.. sectnum::
    :start: 1


* `Overview <tutorial_workflow_0overview.html>`__
* Previous: `Software Setup <tutorial_workflow_1setup.html>`__
* Next: TBD

.. contents::


Two types, data-only projects, which are meant to be fully installable Python
packages, and regular projects that form the basis of a research paper.


Data-only project
-----------------

File structure:

:: 

    data-project-name/
    |── setup.py
    |── data-project-name/
        |── __init__.py
        |── util/
        |   |── __init__.py
        |   |── env.py
        |── clean/
            |── __init__.py
            |── raw.py


Example :code:`util/env.py` file:

.. code-block:: python3

    import os
    import datetime


    data_root = r'd:/'

    DATA_PATH = os.path.join(data_root, 'Data', 'data-project-name')

    # Get the current year and month as "YYMM"
    now = datetime.datetime.now()
    out_month = str(now.year)[-2:] + str(now.month).zfill(2)
    OUT_PATH_ROOT = os.path.join(dropbox_root, 'research', 'mon-coverage', 'out')
    OUT_PATH_MONTH = os.path.join(OUT_PATH_ROOT, out_month)


    def data_path(*args):
        return os.path.join(DATA_PATH, *args)


    def src_path(*args):
        return data_path('src', *args)


    def out_path(*args):
        if not os.path.isdir(OUT_PATH_ROOT) and os.path.isdir(OUT_PATH_MONTH):
            os.makedirs(OUT_PATH_MONTH)
        return os.path.join(OUT_PATH_MONTH, *args)


.. code-block:: ipython3

    In [1]: from util.env import data_path

    In [2]: print(data_path('main_file.dta'))
    Out[2]: 'd:\\Data\\data-project-name\\main_file.dta'



Full project
------------


How it's done

:: 

    project-name/
    |── draft/
    |── present/
    |── lit/
    |── data/
    |   |── src/
    |── out/
    |   |── 1807/
    |   |── 1808/
    |       |── plot_variable.png
    |       |── reg_main.tex
    |── code/
        |── util/
        |── clean/
        |── analysis/
        |── driver.sh
        |── summ_a_variable.py
        |── plot_a_variable.py
        |── reg_main.py

:code:`util` and :code:`clean` as above, including :code:`util/env.py`.

Sample :code:`driver.sh`:

.. code-block:: bash

    #! /bin/bash

    python reg_main.py
    python plot_a_variable.py


