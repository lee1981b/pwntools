.. testsetup:: *

   import tempfile
   import subprocess
   from pwn import *

   # TODO: Remove global POSIX flag
   import doctest
   doctest_additional_flags = doctest.OPTIONFLAGS_BY_NAME['POSIX']

:mod:`pwnlib.asm` --- Assembler functions
=========================================

.. automodule:: pwnlib.asm
   :members:

Internal Functions
-----------------------------------------

These are only included so that their tests are run.

You should never need these.

.. autofunction:: pwnlib.asm.dpkg_search_for_binutils
.. autofunction:: pwnlib.asm.print_binutils_instructions
