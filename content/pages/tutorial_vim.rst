:Title: The (very) basics of Vim
:slug: tutorial_vim

.. contents::

**NOTE**: Specific examples given for options, flags, commands variations,
etc., are not comprehensive.

Normal Mode
-----------

Vim has 2 main "modes." In each mode, every key on your keyboard does something
different. The default mode of Vim is Normal Mode and is mostly used for moving
the cursor and navigating the current file.

Saving and quitting
~~~~~~~~~~~~~~~~~~~


Some important (or longer) commands begin with :code:`:`. After typing
:code:`:`, you will a colon appear in the bottom left of the screen, followed
by any subsequent charactser you type.  screen.

* :code:`:q[uit]` - quit (the current window of) Vim. ("Window" here is
  internal to Vim, not if you have multiple OS-level windows of Vim open at
  once.)
* :code:`:q!` - force quit (if the current buffer has been changed since the
  last save)
* :code:`:e[dit] {filename}` - read file {filename} into a new buffer. If
  :code:`{filename}` doesn't exist, create a buffer (*not* a file) associated
  with that filename.  Vim doesn't "open" files like MS Word does. Instead, it
  reads the contents of a file into RAM and then you edit the "buffer" in RAM.
  Other programs may access and change the underlying file you originally
  opened (Vim will notice this and issue a warning).
* :code:`:w[rite] {filename}` - write the current buffer to {filename}. If no
  filename passed (i.e., :code:`:w`) and the buffer already has an
  associated filename (the one used with :code:`:e {filename}`), that
  associated filename will be used.  A simple :code:`:w` is like MS Word "save"
  and :code:`:w {new_filename}` is "save a copy as :code:`{new_filename}` but
  keep the current buffer.
* :code:`:w!` - force write (e.g., even if the underlying file has been been
  changed by another program and this write will overwrite those changes)
* :code:`:save {filename}` - Save as (and change current buffer to {filename})
* :code:`:save! {filename}` - Save as and overwrite {filename} if it exists.

These commands can be combined, e.g.  :code:`:wq` - write the buffer and quit
:code:`:wq!` - force write and quit  

Moving around the buffer
~~~~~~~~~~~~~~~~~~~~~~~~

Basic motion commands move cursor...
++++++++++++++++++++++++++++++++++++

* :code:`j` - down  
* :code:`k` - up
* :code:`h` - left  
* :code:`l` - right  


Moving quickly between words
++++++++++++++++++++++++++++

* :code:`w` - forward one word (alphanumeric, :code:`\_;`, or consective chars that
  are none of those)
* :code:`e` - end of current word (or next word if currently at end of word)
* :code:`b` - to beginning of word (or previous word if currently at beginning)  
* :code:`}` - Move forward a paragraph (or a function or a section, depending
  on the type of file you're editing).
* :code:`{` - Move back a paragraph.

* :code:`%` - If the cursor is inside parentheses (or or quotes, brackets,
  etc.), move to opening paren. If the cursor is on a paren, move to its
  partner paren. If not between parens, do nothing. (Can do weird stuff with
  unmatched parens.)


Moving within a line
++++++++++++++++++++

* :code:`0` - Move to beginning of line  
* :code:`^` - Move to first non-space character in line (same as "0" if the
  line starts with a non-space character) 
* :code:`$` - Move to end of line

*Note*: :code:`^` and :code:`$` are Regular Expression shortcuts for beginning
and end of a string, respectively

Moving to a specific point in the buffer
++++++++++++++++++++++++++++++++++++++++

* :code:`[#]gg` - go to line :code:`[#]` (Example :code:`20gg` goes to line 20)  
* :code:`gg` - go to beginning of buffer
* :code:`G` - go to end of buffer
* :code:`[#]|` - go to column :code:`[#]` on current line, e.g. :code:`10|`
  goes to col 10.  

* :code:`''` - jump to wherever you were before the last jump. This is useful
  after using commands like :code:`gg` to get back to wherever you were when
  you used :code:`gg` to jump to the beginning of the buffer. Using :code:`''`
  repeatedly will jump you back and forth.


Searching the buffer
++++++++++++++++++++

* :code:`f<char>` - put cursor on next instance of :code:`<char>` in the
  current line. Example: :code:`fa` will jump to the next "a".
* :code:`F` - :code:`f` but backwards search  :code:`t` - "to"/ like
* :code:`t` - Just like :code:`f`, but put cursor right before the character
  you're searching instead of on it.  
* :code:`T` - :code:`t` but backwards search
* :code:`;` - move to next instance of your most recent :code:`f` or :code:`t`
  This will not take you past the end of the current line.

**Note**: You can think of :code:`f` and :code:`t` as "find" and "to".

* :code:`/<RegEx><Enter>` - Go to next instance of :code:`<RegEx>` in the current buffer. This uses full Regular Expression matching (with a bit of Vim-specific syntax).
    - :code:`/Hello` takes you to the next "Hello"
    - :code:`/^Hello` takes you to the next "Hello" that is at the beginning of a line.
    - :code:`/\sHello` takes you to the next "Hello" that has a space (or tab) right in front of it.
* :code:`?` - Same as :code:`/` but search backward in the buffer instead of
  forward
* :code:`n(N)` - next (previous) instance of the most recent :code:`/` or
  :code:`?` search  
* :code:`*` - Do a :code:`/` search for word under cursor 

**Note**: While these commands are a quick way to move your cursor, they are
also the basic search functionality in Vim.  For example, :code:`/gen<Enter>`
will take you to the next instance of the string "gen".  Then you can hit
:code:`n` repeatedly to move to each subsequent instance of "gen". When you get
to the end of the file, it will cycle back to the beginning.

Editing the text in Normal Mode (and composing commands)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most composing of actual text will be done in Insert Mode, explained below.
However, there are a number of commands that are meant to quickly edit the text
without leaving Normal Mode.

Many of these commands require a motion command (signified here as :code:`[m]`)
to specify the extent over which to execute the edit. Several common
conventions for many (but not all) commands:

* double-tap: execute command for entire line cursor is currently on
* shift + command: execute command from cursor to end of current line

More generally, the composability of editing commands and motion is what makes
Vim particularly powerful. If you know 5 editing commands and 5 motion
commands, you actually know (at least) 25 commands.

* :code:`d[m]` - delete from cursor location to wherever :code:`[m]` takes the cursor. Examples:
    - :code:`dw` delete from here (location of cursor) to beginning of next
      word (includes character under the cursor)  
    - :code:`dtT` deletes "to" (up to but not including) the next instance of
      "T" on this line
    - :code:`df)` deletes to ("finds") the next instance of ")" on this line  
    - :code:`d/the` deletes everything between the cursor and the next instance
      of "the" in the buffer.
* :code:`dd` delete this entire line
* :code:`D` delete from here to end of line  
* :code:`4dd` delete this line and next 3 (4 total) 

..

* :code:`y[m]` yank (copy). Same basic behavior as d (delete).
    - :code:`yw` yank from here to beginning of next word
    - :code:`y$` yank from here to end of line
* :code:`yy` - yank the current line

*Note*: To make it consistent with :code:`D`, it's common to add an analagous
mapping for :code:`Y` in your vimrc like so: :code:`nnoremap Y y$`

* :code:`p` - paste after cursor location. Example: To copy the current line,
  use :code:`yyp`, which yanks the current line and then pastes it.
* :code:`P` - paste before cursor location

..

* :code:`>[m]` - Indent through modtion :code:`m`.
    - :code:`>>` - Indent current line.
* :code:`<[m]` - Un-indent/opposite of :code:`>`.


Composing Commands
++++++++++++++++++

Most motion and editing commands can take a number before them to execute that
number of times.

* :code:`4j` - Move cursor down 4 times  
* :code:`10w` - Move cursor forward 10 "words"  
* :code:`d4w` - Delete from here to beginning of 4th word forward
* :code:`<G` - Indent everything from cursor to end of buffer

Special Motion Commands
+++++++++++++++++++++++

* :code:`daw` - "Delete a word"; delete the word under the cursor plus any trailing space.
* :code:`diw` - "Delete inner word"; delete the word under the cursor, leave spaces.

Explain.

* :code:`[e]ip`
* :code:`[e]ap`
* :code:`[e]i(`
* :code:`[e]a(`

Undo/Redo
+++++++++

* :code:`u` - undo  
* :code:`c-r` - redo  


Misc. Other Commands
++++++++++++++++++++

Change letter case

* :code:`~` - toggle the case of this character 
    * :code:`[#]~` - toggle case of :code:`[#]` next character(s)  
* :code:`g~[m]` - toggle case with motion [m]  
* :code:`gU[m]` - uppercase  
* :code:`gu[m]` - lowercase  

Combine lines

* :code:`J` - Take the next line and move it to the end of this line.

Format line/wrap text

* :code:`gq[m]` - Format the text between here and :code:`[m]` (usually just
  breaks overly long lines to smaller lines, by default 80 characters).
* :code:`gqq` - Format the current line  
* :code:`gqap` - Format this ("a") paragraph


Scrolling
~~~~~~~~~

* :code:`c-e` - scroll forward, keeping cursor in place 
* :code:`e-y` - scroll backward, keeping cursor in place  
* :code:`c-u` - move cursor Up full page  
* :code:`c-d` - move cursor Down full page
* :code:`c-f` - Forward half-page  
* :code:`c-b` - Back half-page  

**Note**: :code:`c-u` or :code:`C-u` in Vim mappings is short for
:code:`Ctrl+u`. :code:`m-u` is for "meta", which will be the Alt key on Windows
machines. Be aware that meta bindings will not always work on Unix systems,
especially old ones.

* :code:`H` - Move cursor to highest line on screen (home)  
* :code:`M` - Move cursor to middle line on screen
* :code:`L` - Move cursor to lowest line on screen  


Insert Mode
-----------

Most commands are executed in Normal Mode. If you actually want to add to the
text (type a "j" instead of moving down one line) you need to enter Insert
Mode. There are several ways to do this.

* :code:`i` - Enter Insert mode before the current character  
* :code:`a` - Enter insert mode After the current character  
* :code:`<Esc>` - Exit Insert Mode (go back to Normal Mode).

*Note*: Because :code:`<Esc>` is a little out of the way, it's common to remap
a more convenient keybinding to also exit Insert Mode. For example,
:code:`inoremap jk <Esc>` in your vimrc will allow you to use a quick
:code:`jk` instead of :code:`<Esc>`.

* :code:`I` - Enter insert mode at the beginning of the current line's text
  (same as doing :code:`^` then :code:`i:code:`)
* :code:`A` - Enter insert mode After the end of th current line (like
  :code:`$` then :code:`a:code:`). "Append" is another good pnemonic.
* :code:`o` - Add a new line after the current line and enter insert mode (like
  doing :code:`A<Enter>:code:`)  
* :code:`O` - Add a new line before the current line and enter insert mode  

..

The "change" commands delete the desired text and immediately enters insert mode. 

* :code:`c[m]` - Change text from here to [m]. This includes "advanced" movements.
    - :code:`ci(` - Change everything between the current parentheses.
* :code:`cc` - Change this whole line.  
* :code:`C` - Change from here to end of line.  

"Replace" commands:

* :code:`r` - replace the current character with the next character typed (only
  one character allowed)
* :code:`R` - Replace characters until you hit :code:`<Esc>` (like
  replace/overwrite mode in Word)  


## Registers (for yank and paste).  :code:`"\<char>y` - yank to register
:code:`<char>:code:`.  This allows you to have multiple things in your
clipboard. Note the Vim clipboard is separate from the OS clipboard. To move
between the two (copy/paste between Vim and another program) use the *
register, so:

:code:`y$` - yanks to end of line, puts in default register  :code:`"a$` - yank
to register "a"  :code:`"*yG` - yanks to end of file, puts in OS register
:code:`p` - pastes what's in the default register (after the cursor, like
:code:`a:code:`)  :code:`P` - paste before cursor (like command
:code:`i:code:`)  :code:`"*p` - pastes what's in the OS register (i.e., if you
already yanked to * or you did a Ctrl+C copy in another program)

NOTE: deleting text puts that text into the default register, so if you
:code:`yy:code:`, move to another line, then :code:`dd:code:`, you'll lose
whatever whatever you yanked with :code:`yy:code:`. There is a plugin to
override this behavior (I think by Tim Pope).


# Substitution :code:`:<range>s/<re>/<str>/<flags>` - substitute first instance
of :code:`<re>` in each line in :code:`<range>` with :code:`<str>:code:`.
:code:`<flags>` change default behavior.

- :code:`<range>:code:`: - default range is this line only  - :code:`%` -
  global (whole file)  - :code:`<a>,<b>` - between lines/markers/etc  -
  :code:`.` - current line  - :code:`$` - last line in file (so :code:`:.,$s`
  is "from here to end of file")  - *Note*: There are other :code:`<range>`
  things, most common is just :code:`%:code:`.  

- :code:`<flags>:code:`: - :code:`g` - global/all instances of :code:`<re>` on
  line (not just first instance on line)  - :code:`c` - confirm (will highlight
  next instance of :code:`<re>` and ask you to press "y" to execute change  -
  :code:`i` - case insensitive  

Specific sub: Use :code:`\zs` and :code:`\ze` to demark a sub-RegEx within the
matched RegEx that should be substituted. Example: 

:code:`:%s/Year \zs2007\ze is over/2008/g`

This changes all instances of "Year 2007 is over" to "Year 2008 is over", but
not all "2007" to "2008".


# Advanced motion(ish) commands There are "motion" commands that can be used
with delete, yank, etc., that can be used to target specific text objects.
:code:`dw` will delete from cursor to beginning of next word, so will not
delete the entire current word under the cursor unless the cursor happens to be
at the beginning of the word. So :code:`bdw` will delete the whole word and the
space(s) after it (unless the cursor is already at the beginning of the word).

A shortcut around this is these motion-like object commands.

:code:`daw` - Delete "a" "word". Deletes the current word and space(s) after
it.  :code:`diw` - Delete "inner" "word". Deletes current word but not trailing
space(s).  :code:`dap` - Delete a paragraph. A "paragraph" to Vim is a group of
consecutive lines of text between an empty line(s).  :code:`yaw` - Yanks a
word.  :code:`yiw` - Yanks inner word.  :code:`ya(` - Yank a parenthetical. If
cursor between (), yank everything between those parens and the parens
themselves. Else do Nothing.  :code:`yi(` - Yank inner parenthetical. Like
:code:`ya(:code:`, but excluding the parens.  :code:`ya)` - :code:`ya(`
:code:`ya[` - Same as :code:`ya(` but for brackets :code:`[]:code:`.
:code:`ya"` - Same  

:code:`da(` - Deletes a parenthetical.  :code:`di(` - Deletes within
parenthetical.  

:code:`g~i(` - Toggles the case of the inner parenthetical.  

:code:`ciw` - Change inner word  :code:`ci[` - Change inner (within) brackets
(delete text within brackets and enter Insert Mode).  


# Other very useful stuff

## Predictive completion (while in Insert Mode) :code:`c-p` - predictive
completion (word)  :code:`c-x c-l` - predictive completion (line)  

This takes what you've already typed (either word or line) and uses the text in
the rest of any open buffers to predict what will come next. If there's only
one possibility, it will be filled in. If there are several possibilities, it
will give you the choices.

Vim autocomplete is pretty nice, but there are better, automated predictive
text solutions (specifcally, the package YouCompleteMe). However, I've found
they're a bit too demanding for most laptops and only useful on desktop
computers.

## Global command by line :code:`:g/<RegEx>/<edit command>` - perform the edit
command on every line that matches RegEx  :code:`:g!/...` or :code:`:v/...` -
the same but for lines that don't match  Examples:  :code:`:g/DEL THIS/d`
deletes every line that contains "DEL THIS"  :code:`:g/ $/d` deletes every line
that ends with a space.  

## Macros

Hit :code:`q` then some letter, WLOG :code:`a` to begin recording macro "a".
Do your thing.  Hit :code:`q` to stop recording.  :code:`@a` to repeat the new
macro. :code:`[#]@a` repeats a :code:`[#]` times.  


# Other moderately useful stuff

## Marks

Lower case are local, upper case are global (across files). Jumping to a mark
is a standard motion command for deleting, yanking, etc.

:code:`ma` - sets mark on current cursor location (line and column), WLOG,
called "a" :code:`'a` - jump to line of "a" (first non-blank character of line)
:code:`` :code:`a :code:`` - jump to position of "a" (line and col)
:code:`:marks` - lists all current marks :code:`:delmarks <args>` - delete
specific marks  :code:`:delmarks!` - delete all lowercase in buffer
:code:`]':code:`, :code:`['` - jump to next (previous) line with a lowercase
mark  :code:`` ]` :code:``, :code:`` [` :code:`` - jump to next (previous)
lowercase mark  

### Special Marks (Most useful when beginning) :code:`'` - The line you were on
before making a "jump". So if you're on line 57 and jump to beginning of file
using :code:`gg:code:`, hitting :code:`''` will take you right back to line 57.
:code:`.` - last edit in current buffer  :code:``` :code:`` :code:``` - jump
back to position (line and col) where just jumped from  :code:`` :code:`[
:code:``, :code:`` :code:`] :code:`` - jump to beg/end of last changed or
yanked text  

## Spellcheck

Turn on with :code:`:set spell:code:`, turn off with :code:`:set
nospell:code:`.

:code:`z=` - Suggest correctly spelled words  :code:`]s:code:`, :code:`[s` -
Move to next/previous mispelled word (use :code:`S` for "bad words only")
:code:`zq` - Add word under cursor as good word to first name in 'spellfile'
:code:`zw` - Mark as bad word  :code:`zu[q,w]` - Undo marking  

Visual "Mode"
-------------

* :code:`v[m]` - Go into visual (highlight) mode to select characters, then use
  usual motion commands like :code:`j` or :code:`k` to add to selection as
  the cursor moves.
* :code:`V` - Visual mode, but grab whole lines at a time instead of characters.
* :code:`c-v` - Visual mode, but select vertically (by columns) instead of
  horizontally

* :code:`ggvG` - Highlight whole file, i.e., go to beginning of file
  (:code:`gg:code:`), enter visual mode (:code:`v:code:`), go to end of file
  (:code:`G:code:`).  

Once a selection has been made, you can use an edit command on that selection
and it will (usually) behave as you'd expect.  

Tricks And Extra Special Commands
---------------------------------

Repeating Commands (The Mighty :code:`.`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The command :code:`.` repeats last edit command you executed, including insert,
replace, indent, etc.  **This is one of the most useful features in Vim.**
Some examples:

* :code:`A;<Esc>j.`
    - Enter insert mode at end of line (:code:`A`),
    - type a semi-colon (:code:`;`),
    - exit Insert Mode; (:code:`<Esc>`),
    - move down one line (:code:`j`),
    - add a semi-colon to the end of this new line without leaving Normal Mode
      (:code:`.` which equals :code:`A;<Esc>`).
* :code:`>>...`
    - Indent this line :code:`>>`,
    - then indent it another three times (:code:`...`).






