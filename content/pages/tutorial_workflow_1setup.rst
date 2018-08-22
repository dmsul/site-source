:Title: Software Setup
:slug: tutorial_workflow_1setup

.. sectnum::
    :start: 1


Writing Code in Econ:

* `Overview <tutorial_workflow_0overview.html>`__
* Next: `Project Organization <tutorial_workflow_2project_org.html>`__

.. contents::

-----


You'll need accounts with the following websites if you don't already have one.
These are accounts that you'll likely have for a long time, so don't worry
about tieing them to your work email.

#. `Trello <https://trello.com/danielsullivan49/recommend>`__
#. `Bitbucket <https://www.bitbucket.org>`__
#. `Github <https://www.github.com>`__

You'll also need a bunch of new software.

Atom (or other editor)
++++++++++++++++++++++

Many built-in text editors that come with social science software are okay.
Many are hot garbage.
If you're going to spend any significant amount of time writing code, whether
it's Stata, Matlab, Python, Latex, or whatever, your productivity will benefit
greatly from having a single, professional-grade text editor. This is true for
two reasons.

First, real text editors have a number of features
designed to make your life easier, like auto-completion, Git integration,
syntax checking/linting, code folding, project-level search and replace, etc.
Some built-in editors have some of these features. Some have few or none.

Second, using a single editor across all languages means that as you get better
in one language, you get better in all of them. You have one set of keyboard
shortcuts to learn, one set of options to set, one set of tricks to master.

If you're not already attached to a serious editor (Vim, Emacs, Sublime Text),
I recommend you start with `Atom <https://atom.io/>`_.

Git
+++

Download Git `here <https://git-scm.com/downloads>`__. If you're not on Windows
you might have other ways of getting Git on your computer.

You will be asked if you want Git to be in your PATH and if you want
Git-related tools in your PATH. Choose to have Git in your PATH but not the
tools.

More info on setting up and using Git can be found `here
<tutorial_git_0overview.html>`__.


CMDer
+++++

This is only for people on Windows because Windows has awful command line
interfaces (shells). CMDer is an attempt to fix that. Download it `here
<http://www.cmder.net>`__.

Also, once you have Git installed, you can use Git bash through CMDer to have
access to all the amazing tools there like :code:`grep`, :code:`head`, even
:code:`ssh`.


Python (via Anaconda)
+++++++++++++++++++++

Python is a very powerful programming language that we will use for statistical
analysis and cleaning data. There are a number of extensions to Python, called
packages, that help with this. Keeping track of all these packages can get
difficult (especially on Windows). Anaconda solves this problem by keeping
track of packages automatically.

Download it `here <https://conda.io/docs/user-guide/install/download.html>`__.

You can install regular Anaconda, which will automatically install a lot of
packages, or you can install "Miniconda" which will not install any packages
until you ask it to. In either case, I recommend you install it to
:code:`C:\Anaconda` if you are on Windows.

There are lots of articles online about getting started with Anaconda.
`This
<https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c>`__
is a random one I found that looks okay.


Other
+++++

These are optional or as the need arises.

#. `Sourcetree <https://www.sourcetreeapp.com/>`_. This is an easy way to
   visualize Git repositories.
#. Trello desktop app. As long as you're not on Windows 7, you should be able
   to get the Trello desktop app, which I think is alittle nicer to use
   regularly than the in-browser version.
#. `TeXLive <https://www.tug.org/texlive/>`_. This is basically Anaconda for
   LaTeX. Set install size to the biggest available; set default paper to
   letter; add latex to your path; do *not* install the offered editor. Be
   aware that this takes 30+ minutes to install, depending on your internet
   connection.
