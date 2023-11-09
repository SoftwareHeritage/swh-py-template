Software Heritage - Python module template
==========================================

This is a copier_ template aiming at helping the creation and the lifecycle
management of the many Software Heritage Python modules.

Make sure you have `copier installed`_ in your working environment.


Create a new ``swh`` package
----------------------------

1. create the new package (here a ``swh.foo``) from this template and answer the
   questions asked:

   .. code-block:: console

      $ copier copy https://gitlab.softwareheritage.org/swh/devel/swh-py-template.git swh-foo

2. initialize your new git repository from there:

   .. code-block:: console

      $ cd swh-foo
      swh-foo$ git init .
      swh-foo$ git add -A
      swh-foo$ git commit -m "Initial import from copier"

3. you also probably want to install the pre commit hook (according you have
   pre-commit_ installed in your working environment):

   .. code-block:: console

      swh-foo$ pre-commit install


That's it! You should have a working swh package ready to hack. It includes:

- a ``tox.ini`` file so you can run directly ``tox`` in there (it should fail,
  since the example test is an ``assert False`` one),

- a sphinx documentation template; you can run ``tox -e sphinx`` to build it,

- a template tests/ directory; you can run ``tox -e py3`` to run them,

- a set of configuration for mypy, pytest, flake8 etc.

In a real life scenario, you typically will want to start from the
`swh-environment`_ developer environment, so go read the `developer setup`_
installation documentation.

Please read the copier_ documentation for more details on the usage of the
``copier`` tool.


.. _copier: https://copier.readthedocs.io
.. _`copier installed`: https://copier.readthedocs.io/en/stable/#installation
.. _pre-commit: https://pre-commit.com/
.. _`swh-environment`: https://gitlab.softwareheritage.org/swh/devel/swh-environment
.. _`developer setup`: https://docs.softwareheritage.org/devel/developer-setup.html
