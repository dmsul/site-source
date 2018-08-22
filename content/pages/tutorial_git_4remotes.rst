:Title: Remotes: Sharing Code Online
:slug: tutorial_git_4remotes
:series: GIT_TUTORIAL
:series_index: 5

.. sectnum::

* `Overview <tutorial_git_0overview.html>`__
* Previous: `Branches and Merging <tutorial_git_3branches.html>`__

.. contents::

-----

So far, everything we've done has been on your local computer--no one else can
see your code or contribute to it. While cloud services like Dropbox and Google
Drive are popular for sharing most files within a research team, they are not
very well suited for Git repos. [#]_ Using a service designed specifcally for Git, like GitHub
or Bitbucket, is a better solution.

Any of the projects we work on will be hosted on one of the PI's GitHub or
Bitbucket accounts, so in the context of our work you won't need to worry about
creating a repo online. However, you can follow `these
<https://help.github.com/articles/creating-a-new-repository/>`__ instructions
if you want to practice that on your own.


Downloading (Cloning) a Repository
----------------------------------

To copy a repository hosted online to your computer, use the :code:`clone`
command and the URL of the online repo.

.. code-block:: shell-session

    $ git clone https://github.com/dmsul/econtools.git

This will create a folder :code:`econtools/` in the current folder that
contains all the info about the Git repository hosted at the given URL.

You can also tell Git to name your cloned repo something else:

.. code-block:: shell-session

    $ git clone https://github.com/dmsul/econtools.git different-folder-name

This will clone the :code:`econtools` Git repo into a folder called
:code:`different-folder-name/` instead of :code:`econtools/`.

Pull
----

Push
----

------

.. [#] The problem is that all information about the Git repository is stored
   in a hidden folder called :code:`.git/`. During certain operations, Git the
   software makes lots of changes to files in :code:`.git/` the folder very
   quickly. Dropbox et al. can sometimes have trouble keeping up and will try to
   change these files at the same time Git is, resulting in corrupted files. Once
   that happens, you have to scrap your repo and re-clone it.
