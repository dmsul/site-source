:Title: Branches and Merging
:slug: tutorial_git_3branches
:series: GIT_TUTORIAL
:series_index: 4

.. sectnum::

* `Overview <tutorial_git_0overview.html>`__
* Previous: `First Steps: Making commits <tutorial_git_2commits.html>`__
* Next: Remotes: Sharing Code Online

.. contents::

-----

Git has two main functions. We've already covered the first, which is to create
a record of all the changes we make to our code. Git's second function is
allowing several people to work on the code at once without getting in each
other's way. Branches let us do that.


Branches
--------

A **branch** is a special label that points to a commit.

Let's use our special :code:`git shortlog` command to remind ourselves what our
repository history looks like.

.. code-block:: shell-session

    $ git shortlog
    * 7d6a299 -  (HEAD -> master) Added a variable to hello.py
    * 823459f -  Add hello.py

The tag :code:`master` is the name of the branch, which is the default name Git
uses for the first branch when a repository is created. So for now, the
:code:`master` branch points to commit :code:`7d6a299`. The :code:`HEAD` tag
points to the branch we are actively working on; in Git parlance, we say this
is the branch we have "checked out".

Traditionally, the :code:`master` branch is the "final draft" branch. When we
try something new with the code that may not work right away, we want to keep a
working copy of the code we can fall back to if necessary (or if someone else
wants to try a different innovation at the same time you are trying yours). To
keep the :code:`master` branch safe, we create a new branch where we can work
on our new feature.

Let's add a subroutine to :code:`hello.py` on a new branch.


Create and checkout a new branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, list all the branches in the repo:

.. code-block:: shell-session

    $ git branch
    * master

Just one, :code:`master`. The asterisk marks the currently active branch (the
one that's checked out).

Now, create a new branch called :code:`add-subroutine`.

.. code-block:: shell-session

    $ git branch add-subroutine

and list all the branches again.

.. code-block:: shell-session

    $ git branch
      add-subroutine
    * master

So now we have our new branch. Next, check it out so it's the active branch.

.. code-block:: shell-session

    $ git checkout add-subroutine


And now we see that Git says we're on the :code:`add-subroutine` branch.

.. code-block:: shell-session

    $ git branch
    * add-subroutine
      master

    $ git status
    On branch add-subroutine
    nothing to commit, working tree clean

If we check :code:`shortlog`, we see that :code:`HEAD` is pointing to
:code:`add-subroutine`.

.. code-block:: shell-session

    $ git shortlog
    * 7d6a299 -  (HEAD -> add-subroutine, master) Added a variable to hello.py
    * 823459f -  Add hello.py

**Note:** There's a shortcut that lets you create and checkout a branch all in
one command: :code:`git checkout -b <name-of-branch>`.


Work on the new branch
~~~~~~~~~~~~~~~~~~~~~~

Adding to the branch is nothing we haven't already done. After you've checked
out a branch, any commits you make are added to that branch and that branch
alone. Let's use this branch to add a subroutine to our code.

Create a file called :code:`superprinter.py` that looks like this:

.. code-block:: python3

    def print_thrice(input_string):
        """ Prints `input_string` three times """
        print(input_string)
        print(input_string)
        print(input_string)

Add :code:`superprinter.py` to the repo and commit it:

.. code-block:: shell-session

    $ git status
    On branch add-subroutine
    Untracked files:
      (use "git add <file>..." to include in what will be committed)

            superprinter.py

    nothing added to commit but untracked files present (use "git add" to track)

    $ git add superprinter.py

    $ git status
    On branch add-subroutine
    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

            new file:   superprinter.py

    $ git commit -m "Add superprinter"
    [add-subroutine eb198f3] Add superprinter
     1 file changed, 5 insertions(+)
     create mode 100644 superprinter.py
        

If you look at the log, you can see that branch :code:`add-subroutine` points
to our new commit and that :code:`master` does not.

.. code-block:: shell-session

    $ git shortlog
    * eb198f3 -  (HEAD -> add-subroutine) Add superprinter
    * 7d6a299 -  (master) Added a variable to hello.py
    * 823459f -  Add hello.py

Let's make one more change so that :code:`hello.py` uses our subroutine:

.. code-block:: python3
    from superprinter import print_thrice

    to_print = "Hello, world!"
    print_thrice(to_print)

Commit the change:

.. code-block:: shell-session

    $ git add hello.py
    $ git commit -m "Use print_thrice"
    [add-subroutine fed0858] Use print_thrice
     1 file changed, 3 insertions(+), 1 deletion(-)

    $ git shortlog
    * fed0858 -  (HEAD -> add-subroutine) Use print_thrice
    * eb198f3 -  Add superprinter
    * 7d6a299 -  (master) Added a variable to hello.py
    * 823459f -  Add hello.py

Our two branches have diverged further. But, we can go back to :code:`master`
any time we want.

Checking out a different branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before we do anything, let's run our code to make sure we're using :code:`print_thrice`:

.. code-block:: shell-session

    $ python hello.py$ python hello.py
    Hello, world!
    Hello, world!
    Hello, world!

Looks good. Now let's go back to the :code:`master` branch for a bit, just to
check that we can.

.. code-block:: shell-session

    $ git checkout master
    Switched to branch 'master'

    $ git shortlog
    * fed0858 -  (add-subroutine) Use print_thrice
    * eb198f3 -  Add superprinter
    * 7d6a299 -  (HEAD -> master) Added a variable to hello.py
    * 823459f -  Add hello.py

Recall that :code:`HEAD` points to whatever we've checked out.

By checking out :code:`master`, Git has reverted our code project to be exactly
like it was before we did our :code:`add-subroutine` commits.  The new file
:code:`superprinter.py` is gone:

.. code-block:: shell-session

    $ ls
    hello.py
        
and :code:`hello.py` looks like it did before:

.. code-block:: shell-session

    $ cat hello.py
    to_print = "Hello, world!"
    print(to_print)

    $ python hello.py
    Hello, world!


Making a second branch
~~~~~~~~~~~~~~~~~~~~~~

Let's pretend that someone else on our team is the one working on
:code:`add-subroutine` and that our job is actually to come up with a quote
more inspiring than "Hello, world!".

.. code-block:: shell-session

    $ git checkout -b new-quote
    Switched to a new branch 'new-quote'

    $ git branch
      add-subroutine
      master
    * new-quote

    $ git shortlog
    * fed0858 -  (add-subroutine) Use print_thrice
    * eb198f3 -  Add superprinter
    * 7d6a299 -  (HEAD -> new-quote, master) Added a variable to hello.py
    * 823459f -  Add hello.py

Now let's change the :code:`to_print` variable in :code:`hello.py`:

.. code-block:: python3

    to_print = "That rug really tied the room together, did it not?"
    print(to_print)

and commit the changes:

.. code-block:: shell-session

    $ git add hello.py

    $ git commit -m "Change to_print string"
    [new-quote 44425b9] Change to_print string
     1 file changed, 1 insertion(+), 1 deletion(-)

Now, if we look at our log, we can see why branches are called "branches":

.. code-block:: shell-session

    $ git lg
    * 44425b9 -  (HEAD -> new-quote) Change to_print string
    | * fed0858 -  (add-subroutine) Use print_thrice
    | * eb198f3 -  Add superprinter
    |/
    * 7d6a299 -  (master) Added a variable to hello.py
    * 823459f -  Add hello.py

The branching is even more evident if we use a graphical Git interface:

.. image:: 

We now have three named versions of our code, :code:`master`,
:code:`add-subroutine`, and :code:`new-quote`.

Merging
-------

Wut.
