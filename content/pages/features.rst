:slug: features
:save_as: features.html

Mailman Features
~~~~~~~~~~~~~~~~

Here's a brief description of the features in Mailman.  For a detailed
descriptions of recent changes see the
`NEWS file for Mailman 2.1
<http://bazaar.launchpad.net/~mailman-coders/mailman/2.1/view/head:/NEWS>`__
and the `NEWS file for Mailman 3
<https://gitlab.com/mailman/mailman/blob/master/src/mailman/docs/NEWS.rst>`__.

-  Through-the-web list creation and removal (with automatic support
   depending on the MTA)
-  Multi-lingual support: list web pages and email notices can be in any
   of nearly two dozen supported language, configurable per-site,
   per-list, and per-user
-  "Real name" support for members
-  Support for personalized deliveries and
   `VERP <http://cr.yp.to/proto/verp.txt>`__-like message delivery for
   foolproof bounce detection
-  Emergency moderation
-  MIME-based content filtering, with demime/stripmime like options
-  Regular expression based topic filtering
-  Through the web membership management
-  Through the web administrative requests pages
-  Moderated newsgroup support
-  Flexible moderation and privacy controls
-  Subscription invitations
-  Auto-response controls.
-  User controllable delivery options
-  Urgent: header support (bypasses digests to reach all users
   immediately).

Mailman 3 adds lots of other features, including:

- Virtual hosting support, with no list name restrictions
- Single user account to manage all subscription addresses
- Users can specify a *preferred address* to use by default
- Flexible architecture for integration with your own site
- REST-based API for the core system
- Completely revamped and improved web user interface (`Postorius
  <https://gitlab.com/mailman/postorius>`__) and default archiver
  (`HyperKitty <https://gitlab.com/mailman/hyperkitty>`__).
