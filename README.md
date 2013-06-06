warden-installer
================

Installs the various dependencies for warden.  This is required because graphite+carbon+whisper don't play so well with Django i.t.o. install-data directives.

It also then runs the initialisation scripts for warden, to create the django app and so on.
