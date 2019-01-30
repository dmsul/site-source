:Title: Remotes: Sharing Code Online
:slug: tutorial_git_4remotes
:series: GIT_TUTORIAL
:series_index: 5

.. sectnum::

**A Brief Intro to Git**

* `Overview <tutorial_git_0overview.html>`__
* Previous: `Branches and Merging <tutorial_git_3branches.html>`__

.. contents::
    Page Contents

-----

So far, everything we've done has been on your local computer--no one else can
see your code or contribute to it. While cloud services like Dropbox and Google
Drive are popular for sharing most files within a research team, they are not
very well suited for Git repos. [#]_ Using a service designed specifcally for
Git, like GitHub or Bitbucket, is a better solution.

Any of the projects we work on will be hosted on one of the PI's GitHub or
Bitbucket accounts, so in the context of our work you won't need to worry about
creating a repo online. However, you can follow `these
<https://help.github.com/articles/creating-a-new-repository/>`__ instructions
if you want to practice that on your own.


Downloading (Cloning) a Repository
----------------------------------

To copy a repository from the Internet to your computer, use the :code:`clone`
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

Remote branches
---------------

After you've cloned a repo, you'll have a copy of it on your hard drive.
Suppose that your :code:`shortlog` looks like this:

.. code-block:: shell-session

    $ git shortlog
    * 2f40bfd -  (HEAD -> master, origin/master) Merge branch 'new-quote'
    * 7d6a299 -  Added a variable to hello.py
    * 823459f -  Add hello.py

By default, you have the :code:`master` branch checked out after a clone.
You'll notice that there's another branch label, :code:`origin/master`.
When you clone a repo, Git remembers the website where the repo originated and
calls it :code:`origin` for short. Git also creates special branches in your
local copy of the repo that mirror the branches in the original online repo.
These are **remote branches** and follow the naming convention
:code:`<remote_name>/<branch_name>`.

Update a remote branch (Fetch and Pull)
---------------------------------------

What if the online repo gets updated, how do you get the updates to your computer?
You use the :code:`fetch` command:

.. code-block:: shell-session

    $ git fetch origin
    remote: Enumerating objects: 4, done.
    remote: Counting objects: 100% (4/4), done.
    remote: Total 5 (delta 4), reused 4 (delta 4), pack-reused 1
    Unpacking objects: 100% (5/5), done.
    From github.com:dmsul/econtools
       073517e..906b941  master     -> origin/master

    $ git shortlog
    * 4b93ceq -  (origin/master) A new commit on the website
    * 2f40bfd -  (HEAD -> master) Merge branch 'new-quote'
    * 7d6a299 -  Added a variable to hello.py
    * 823459f -  Add hello.py

Now :code:`origin/master` is one commit ahead of our local :code:`master`
branch. We can merge the two using :code:`git merge origin/master` just like we
did before. Because this process of fetching and merging is so common, there's
a shortcut command, :code:`pull`, which does a fetch, then a merge.

.. code-block:: shell-session

    $ git pull origin master
    From github.com:dmsul/econtools
     * branch            master     -> FETCH_HEAD
    Updating 073517e..906b941
    Fast-forward
     econtools/util/reference.py | 5 +++++
     1 file changed, 5 insertions(+)

    $ git shortlog
    * 4b93ceq -  (HEAD -> master, origin/master) A new commit on the website
    * 2f40bfd -  Merge branch 'new-quote'
    * 7d6a299 -  Added a variable to hello.py
    * 823459f -  Add hello.py

Now our local code is updated to match the code on the website.

Upload your changes to the remote server (Push)
-----------------------------------------------

If you add a commit to your local :code:`master` branch, the remote branch
:code:`origin/master` is unaffected. After adding a commit, your shortlog looks
like this:

.. code-block:: shell-session

    $ git shortlog
    * 4b93ceq -  (HEAD -> master) A new local commit
    * 4b93ceq -  (origin/master) A new commit on the website
    * 2f40bfd -  Merge branch 'new-quote'
    * 7d6a299 -  Added a variable to hello.py
    * 823459f -  Add hello.py

Now :code:`master` is one commit ahead of :code:`origin/master`. To get our new
commit uploaded to :code:`origin` (e.g., Github) and to update
:code:`origin/master`, we use the :code:`push` command:

.. code-block:: shell-session

    $ git push origin master
    Counting objects: 12, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (12/12), done.
    Writing objects: 100% (12/12), 2.09 KiB | 1.05 MiB/s, done.
    Total 12 (delta 10), reused 0 (delta 0)
    remote: Resolving deltas: 100% (10/10), completed with 6 local objects.
    To github.com:dmsul/econtools
       de8fb4e..2e49c46  master -> master

    $ git shortlog
    * 4b93ceq -  (HEAD -> master, origin/master) A new local commit
    * 4b93ceq -  A new commit on the website
    * 2f40bfd -  Merge branch 'new-quote'
    * 7d6a299 -  Added a variable to hello.py
    * 823459f -  Add hello.py


Checkout a local copy of a remote branch
----------------------------------------

[In Progress]

.. code-block:: shell-session

    $ git checkout -b branch-name origin/branch-name



------

.. [#] The problem is that all information about the Git repository is stored
   in a hidden folder called :code:`.git/`. During certain operations, Git the
   software makes lots of changes to files in :code:`.git/` the folder very
   quickly. Dropbox et al. can sometimes have trouble keeping up and will try to
   change these files at the same time Git is, resulting in corrupted files. Once
   that happens, you have to scrap your repo and re-clone it.
