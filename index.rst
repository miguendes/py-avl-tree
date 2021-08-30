py-avl-tree - A Pythonic AVL Tree for Aliens™
=============================================

|Build Status| |codecov| |image2| |License: MIT|

``py-avl-tree`` implements a balanced binary tree.

Reference: http://en.wikipedia.org/wiki/AVL\_tree

In computer science, an AVL tree is a self-balancing binary search tree,
and it is the first such data structure to be invented. In an AVL tree,
the heights of the two child subtrees of any node differ by at most one;
therefore, it is also said to be height-balanced. Lookup, insertion, and
deletion all take O(log n) time in both the average and worst cases,
where n is the number of nodes in the tree prior to the operation.
Insertions and deletions may require the tree to be rebalanced by one or
more tree rotations. The AVL tree is named after its two inventors, G.M.
Adelson-Velskii and E.M. Landis, who published it in their 1962 paper
"An algorithm for the organization of information."

Dependencies
------------

To run this project you need the following dependencies:

-  Python 3.6+
-  Pipenv 2018+

Installation
------------

1. Clone the repo
^^^^^^^^^^^^^^^^^

.. code:: bash

    $ git clone git@github.com:mendesmiguel/py-avl-tree.git

2. Install Dependencies
^^^^^^^^^^^^^^^^^^^^^^^

To install all dependencies, you can use
`pipenv <http://pipenv.org/>`__.

Pipenv will spin up a virtualenv and install the dependencies based on a
``Pipenv.lock`` file inside the root of the project.

.. code:: bash

    $ cd py-avl-tree/
    $ pipenv install 

3. (Optional) Run the tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

    $ python3 -m unittest

How to Contribute
-----------------

1. Check for open issues or open a fresh issue to start a discussion
   around a feature idea or a bug.
2. Fork `the repository <https://github.com/mendesmiguel/py-avl-tree>`__
   on GitHub to start making your changes to the **master** branch (or
   branch off of it).
3. Write a test which shows that the bug was fixed or that the feature
   works as expected.
4. Send a pull request and bug the maintainer until it gets merged and
   published. :)

https://miguendes.me

.. |Build Status| image:: https://travis-ci.org/mendesmiguel/py-avl-tree.svg?branch=master
   :target: https://travis-ci.org/mendesmiguel/py-avl-tree
.. |codecov| image:: https://codecov.io/gh/mendesmiguel/py-avl-tree/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/mendesmiguel/py-avl-tree
.. |image2| image:: https://img.shields.io/badge/python-3.6+-blue.svg
   :target: https://www.python.org/download/releases/3.6.0/
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-green.svg
   :target: https://opensource.org/licenses/MIT
