=====================
 GNU Mailman website
=====================

This project contains the source for the `GNU Mailman website`_.  Building it
requires the `Pelican`_ static site generator.


Local preview
=============

After cloning this repository,
and assuming you have Pelican installed, you can build the site by running::

    $ make html

The files will be generated into the ``output`` directory.  To view the site,
run::

    $ make serve

and visit http://localhost:8000

Just hit ctrl-C to kill the server.


Installation
============

Installing the site means copying the generated HTML to the main site and its
mirrors.  You of course have to have permission to do any of this; mostly that
just means the Mailman project administrators.  While most of the install
steps ``rsync`` to remote locations, the GNU mirror requires a local CVS (!)
checkout of the HTML files checked out to ``~/projects/mailman-gnu``.  Have
fun with that.

To install do::

    $ make install
    $ cd ~/projects/mailman-gnu
    $ cvs commit -m'Update'


.. _`GNU Mailman website`: http://www.list.org
.. _Pelican: http://blog.getpelican.com/
