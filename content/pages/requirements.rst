:slug: requirements
:save_as: requirements.html

Requirements
~~~~~~~~~~~~

Mailman currently runs only on GNU/Linux and any other POSIX-compliant
operating system, such as BSD-based, Solaris, MacOS X, etc.  It probably does
not work on Windows, and while you might be able to get it running on a
`Cygwin <http://cygwin.com/>`__ system, it is not recommended or supported.

You must have the Python interpreter installed somewhere on your
system.  For Mailman 2.1, Python 2.7 is recommended.  For Mailman 3, you will
need Python 3.4 or newer to run the core, and Python 2.7 to run the web user
interface and archiver.

You must have a mail server (MTA) that you can send messages to, and for
Mailman 3, supports delivery to a local agent over LMTP.  You will need a web
server that supports the CGI/1.1 API for Mailman 2.1, and WSGI for Mailman 3.
Apache makes a fine choice for web server, and MTAs such as Postfix, Exim,
Sendmail, and qmail should work just fine.

For Mailman 2.1, you will also need an ANSI C compiler to build Mailman's
security wrappers.  All modern versions of the GNU C compiler should work
well.  This is not required for Mailman 3.
