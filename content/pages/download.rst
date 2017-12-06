:slug: download
:save_as: download.html

Requirements
~~~~~~~~~~~~

See the `requirements page <requirements.html>`__ for the list of
pre-requisites.

Downloading
~~~~~~~~~~~

Mailman 2.1 is available from the following sources:

-  `Launchpad <http://launchpad.net/mailman>`__
-  `GNU <http://ftp.gnu.org/gnu/mailman/>`__

*Note: the GNU ftp site may lag behind Launchpad, especially just after
a release announcement. It often takes a little while for the GNU ftp
site to catch up.*

Mailman 3 is available from the `Python Package Index (PyPI) <https://pypi.python.org/pypi?%3Aaction=search&term=mailman&submit=search>`__.

Mailman 3 has been split into a suite of related components.  See
`Mailman Suite Installation <http://docs.list.org/en/latest/prodsetup.html>`__
for some installation documentation.

Here's a list of the names of the Mailman 3 components:

-  *Mailman Suite* refers to the collection of related Mailman projects that provide all the pieces of a typical mailing list management setup.
-  *Mailman Core* is the part that delivers the emails and handles the mailing list and user data
-  *Postorius* is the web interface that allows users (list members, list admins, moderators) to change their user settings and the settings for their lists.
-  *HyperKitty* is the archiver which provides a web interface to access GNU Mailman v3 archives as well as ways interact with the lists. It can behave a little like a web forum, for those who prefer not to use email.
-  *MailmanClient* is the library that provides official Python bindings for the GNU Mailman 3 REST API. This allows you to write your own front end or scripts for interacting with Mailman. (It's also what Postorius uses to interact with Mailman Core.)
-  *Mailman Bundler* is a tool to help you install all of Mailman Suite via PyPI


Signing keys
~~~~~~~~~~~~

We always sign releases with the `GPG keys <http://www.gnupg.org>`__ of one of
the core developers: Barry Warsaw or Mark Sapiro.  Our public keys are
available from all the public keyservers. For cross referencing, here are the
keys we use to sign releases:

+--------------------+--------------------+---------------------------------------------------------+
| Developer          | GPG key id         | GPG fingerprint                                         |
+====================+====================+=========================================================+
| Barry Warsaw       | ``A74B06BF``       | ``8417 157E DBE7 3D9E AC1E  539B 126E B563 A74B 06BF``  |
+--------------------+--------------------+---------------------------------------------------------+
| Mark Sapiro        | ``953B8693``       | ``C638 CAEF 0AC2 1563 736B  5A22 555B 975E 953B 8693``  |
+--------------------+--------------------+---------------------------------------------------------+
|Abhilash Raj        | ``61D0A67C``       | ``541E A044 8453 394F F77A  0ECC 9D9B 2BA0 61D0 A67C``  |
+--------------------+--------------------+---------------------------------------------------------+
