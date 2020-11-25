Installation
============

There are currently two supported ways to run the application. The first is with a native python interpreter,
the second is using Docker.

Native
++++++

Assuming you have cloned the code into the current directory, you can install the application by running
the following commands one at a time.

.. code-block:: shell

    python3 -m virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

You can then run the application by running ``python manage.py runserver``

Docker
++++++

The Docker container is automatically built off of the ``main`` branch and other branches of interest. A full
listing of all available containers can be found on the `Docker Hub <https://hub.docker.com/r/thetoddluci0/iselab_debugger/tags?page=1&ordering=last_updated>`_
