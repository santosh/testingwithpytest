# pytest-nice

pytest-nice is a pytest plugin to show motivational message to developers which motivates them and make the whole development process more productive.

Features
--------

-  Includes user name of person running tests in pytest output.
-  Adds ``--nice`` option that:
    -  turns ``F`` to ``O``
    -  with ``-v``, turns ``FAILURE`` to ``OPPORTUNITY for improvement``

Installation
------------

::
    $ pip install pytest-nice-0.1.0.tar.gz
::

Usage
-----

::
    $ pytest --nice
::
