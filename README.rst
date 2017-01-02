.. image:: https://img.shields.io/badge/dmtn--030-lsst.io-brightgreen.svg
   :target: https://dmtn-030.lsst.io
   :alt: Technote website
.. image:: https://img.shields.io/travis/lsst-dm/dmtn-030/master.svg?maxAge=2592000
   :target: https://travis-ci.org/lsst-dm/dmtn-030
   :alt: Travis build status
.. image:: https://zenodo.org/badge/doi/10.5281/zenodo.228174.svg
   :target: http://dx.doi.org/10.5281/zenodo.228174
   :alt: doi:10.5281/zenodo.228174

###############################################
DMTN-030 Science Pipelines Documentation Design
###############################################

A design discussion and implementation plan for the pipelines.lsst.io documentation project, including information design and topic templates.

View this technote at https://dmtn-030.lsst.io or see a preview of the current version in `this repo`_.

Build this technical note
=========================

You can clone this repository and build the technote locally with `Sphinx`_

.. code-block:: bash

   git clone https://github.com/lsst-dm/dmtn-030
   cd dmtn-030
   pip install -r requirements.txt
   make html

.. note::

   In a Conda_ environment, ``pip install -r requirements.txt`` doesn't work as expected.
   Instead, ``pip`` install the packages listed in ``requirements.txt`` individually.

The built technote is located at ``_build/html/index.html``.

Editing this technical note
===========================

You can edit the ``index.rst`` file, which is a reStructuredText document.
The `DM reStructuredText Style Guide`_ is a good resource for how we write reStructuredText.

Remember that images and other types of assets should be stored in the ``_static/`` directory of this repository.
See ``_static/README.rst`` for more information.

The published technote at https://dmtn-030.lsst.io will be automatically rebuilt whenever you push your changes to the ``master`` branch on `GitHub <https://github.com/lsst-dm/dmtn-030>`_.

Updating metadata
=================

This technote's metadata is maintained in ``metadata.yaml``.
In this metadata you can edit the technote's title, authors, publication date, etc..
``metadata.yaml`` is self-documenting with inline comments.

****

Copyright 2016, 2017 Association of Universities for Research in Astronomy

This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

.. _Sphinx: http://sphinx-doc.org
.. _DM reStructuredText Style Guide: https://developer.lsst.io/docs/rst_styleguide.html
.. _this repo: ./index.rst
.. _Conda: http://conda.pydata.org/docs/
