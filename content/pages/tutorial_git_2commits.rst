:Title: First steps: Making commits
:slug: tutorial_git_2commits
:series: GIT_TUTORIAL
:series_index: 3

.. sectnum::

**A Brief Intro to Git**

* `Overview <tutorial_git_0overview.html>`__
* Previous: `Setup <tutorial_git_1setup.html>`__
* Next: `Branches and Merging <tutorial_git_3branches.html>`__

.. contents::
    Page Contents


Set up a new code project
~~~~~~~~~~~~~~~~~~~~~~~~~

Git is version control software used for keeping track of the changes in coding
projects. A folder containing files being tracked by git is called a
**repository**.  After you've created a repository (that is, after you've told
git to watch a folder of code), git will be ready to record the incremental
changes that happen to the code. However, we get to decide exactly which
changes are recorded.

This tutorial will walk you through using git with a very simple Python
project.  (You don't need Python installed. We're not going to run this file.
It's just to give git some actual code to work with.) Code examples that begin
with :code:`$` are meant to be entered into the git bash command line.

To start, we're going to create a directory to put our fake project in:

.. code-block:: shell-session

    $ cd ~                  # Go to our home directory
    $ mkdir git_practice    # Make the new directory
    $ cd git_practice       # Navigate to the new directory


We're also going to put a file in our new directory. Create a file called
:code:`hello.py` that looks like this:

.. code-block:: python3

    print("Hello, world!")



Tell git to watch a directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To tell git that you want to the current directory to be a repository (that is,
you want git to watch this directory), you use the following command:

.. code-block:: shell-session
    
    $ git init

That's it!

Ask git what our workspace looks like
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that you've run :code:`git init`, we can use git commands in our directory.
Let's start with :code:`git status`, which tells us what's going on in our working
directory.

.. code-block:: shell-session

    $ git status
    On branch master

    No commits yet

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

            hello.py

    nothing added to commit but untracked files present (use "git add" to track)

Git lists :code:`hello.py` under "Untracked files". That's because :code:`git init`
only tells git that we want to use this directory. To track individual files,
we need to tell git which files to watch or "track".


Tell git to track a file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use :code:`git add <filename>` to have git start tracking a file

.. code-block:: shell-session

    $ git add hello.py

To check what we've accomplished, use :code:`git status` like before:

.. code-block:: shell-session

    $ git status
    On branch master

    No commits yet

    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)

            new file:   hello.py

Now git is specifically watching our :code:`hello.py` file.


Commit a new file to the repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You probably noticed that the last :code:`git status` listed our file under
"Changes to be committed".  That's because adding a new file (or a change to an
existing file) to the permanent record of the repository is a two-step process.

The first step is **staging**.  This is like putting items in a moving box but
leaving the box open.  We might put more things in, we take more
things out--it's not permanent *yet*. We staged our new file with
:code:`git add hello.py`; we told git to add :code:`hello.py` to a box but to leave the top open
for now.

The second step is the **commit**. Making a commit takes all the changes we've
staged (the things we've put in the box) and adds them to the permanent record
of the repository (seals the box and puts it in storage).

To make a commit, you first have to have something staged. We already did this
with :code:`git add hello.py`, which is why :code:`hello.py` is now listed under
"Changes to be committed".

Now let's actually make the commit. The base command is :code:`git commit`.
However, it's good practice to also add a short note or message that describes
the commit; it's like writing the contents of a box on the outside of the box.
The easiest way to do this is with the :code:`-m` option, "m" for "message". So to
make the commit with the message "Add hello.py", run this command:

.. code-block:: shell-session

    $ git commit -m "Add hello.py"
    [master (root-commit) 823459f] Add hello.py
     1 file changed, 1 insertion(+)
     create mode 100644 hello.py

And that's it! This version of :code:`hello.py` has been committed to the record
that git keeps about our project. We can double check that our commit worked by
running :code:`git status`:

.. code-block:: shell-session

    $ git status
    On branch master
    nothing to commit, working tree clean


Commit a change to a file
~~~~~~~~~~~~~~~~~~~~~~~~~

Now that git is tracking :code:`hello.py`, it will alert us when the file changes.

First, change :code:`hello.py` so it looks like this:

.. code-block:: python3

    to_print = "Hello, world!"
    print(to_print)


Now ask git if anything has changed:

.. code-block:: shell-session

    $ git status
    On branch master
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

            modified:   hello.py

    no changes added to commit (use "git add" and/or "git commit -a")

Git sees that :code:`hello.py` has changed. Remember that adding these changes to
the repository record is a two step process:

#. Stage (add to the box)
#. Commit (seal the box)

So let's tell git to stage the changes made to :code:`hello.py`, then check our
:code:`git status`.

.. code-block:: shell-session

    $ git add hello.py
    $ git status
    On branch master
    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

            modified:   hello.py

Now let's make the commit and check that it worked.

.. code-block:: shell-session

    $ git commit -m "Added a variable to hello.py"
    [master 7d6a299] Added a variable to hello.py
     1 file changed, 2 insertions(+), 1 deletion(-)

    $ git status
    On branch master
    nothing to commit, working tree clean


Look at the list of commits
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The whole point of commits is to keep track of the incremental changes we make
to our code. So we need a way to look back at the list of commits we've made.
This is done with the :code:`git log` command. However, the standard :code:`git log`
command puts out a lot of information we don't necessarily need. If you're
using the :code:`.gitconfig` file listed above, you can use :code:`git lg` to see a
customized version of :code:`git log` that is a little simpler:

.. code-block:: shell-session

    $ git shortlog
    * 7d6a299 -  (HEAD -> master) Added a variable to hello.py
    * 823459f -  Add hello.py

Each :code:`*` marks a commit. Next to that is the commit's ID number or "hash".
For our most recent commit, this is :code:`7d6a299`. Your hashes will likely be
different because git generates unique ID's for every commit. That's okay. We
won't be directly using the hashes in this tutorial for a while.

After the hash is the commit message we wrote. :code:`(HEAD -> master)` marks what
the most recent commit is. Don't worry about this just yet, we'll get to it.
