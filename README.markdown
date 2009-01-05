Introduction
============

``scm-up-all.py`` is script to update all SCMs (Bazaar, Git, Git SVN,
Mercurial, Subversion) directories located in your shared packages directory.

For example, I was cloned several Bazaar, Git, Mercurial and Subversion
repositories to ``/srv/shared``:

    /srv/shared
      + django
      + django_xmlrpc
      + git-sh
      + jinja2

And for updating all of these directories I need to typo:

    $ svn up /srv/shared/django
    $ cd /srv/shared/django_xmlrpc && bzr pull
    $ cd /srv/shared/git-sh && git pull
    $ cd /srv/shared/jinja2 && hg fetch

But, with ``scm-up-all.py`` I need only to set ``/srv/shared`` as first
argument and all supported SCMs directories will be updated automatic:

    $ scm-up-all.py /srv/shared

or

    $ cd /srv/shared && scm-up-all.py

Requirements
============

 * Python 2.3 or higher

Installation
============

To install ``scm-up-all.py`` script, execute:

    sudo make install

from this directory. This will install ``scm-up-all.py`` to ``/usr/local``. If
you want to change destination directory or haven't permissions to write into
system directories, setup ``PREFIX`` environment var, by:

    make PREFIX=~ install

To uninstall ``scm-up-all.py`` script, execute:

    sudo make uninstall

or

    make PREFIX=~ uninstall

if you use custom prefix on installation.