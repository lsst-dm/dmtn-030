.. _docs-as-code:

Documentation as code
=====================

The Science Pipelines documentation uses a *documentation-as-code* architecture.
Documentation is stored and versioned in pipelines package repositories, and built by DM's standard continuous integration system with Sphinx_ into a static HTML site that is published to the web with `LSST the Docs <SQR-006>`_.
This section outlines the basic technical design of the Science Pipelines documentation.

.. _docs-in-packages:

Documentation in packages
-------------------------

Each EUPS-managed LSST Science Pipelines package contains a ``doc/`` directory.
All documentation specific to that package is contained within the ``doc/`` directory.
A minimal ``doc/`` directory looks like::

   doc/
     index.rst
     tasks/
     _static/

Here, ``index.rst`` is a reStructuredText document we refer to as a :ref:`module topic <module-type>`, described later.
The ``tasks/`` directory hosts :ref:`task topic pages <task-type>` for any pipeline tasks implemented in that module.
The ``_static/`` directory is a space for non-reStructuredText content that is copied verbatim to the built site.

Most Science Pipelines packages host a single :ref:`module <module-type>`, but there are exceptions like ``afw``.
In this case, there is an additional level of directories::

   doc/
     index.rst
     cameraGeom/
       index.rst
       tasks/
       _static/
     coord/
     detection/
     display/
     fits/
     geom/
     gpu/
     image/
     math/
     table/

Each ``afw`` module subdirectory contains the ``index.rst``, ``tasks/`` and ``_static/`` structure.
The root ``doc/index.rst`` file is a minimal file containing a `toctree`_ that is only used for local, single package documentation builds.

.. note::

   The ``doc/`` directory was already used by the previous Doxygen-based documentation build system.
   However, during the transition from Doxygen to Sphinx-based builds, we do not expect any conflicts since content for the two system reside in non-overlapping files (``.dox`` versus ``.rst`` files for Doxygen and Sphinx, respectively).
   It should be possible to continue to build a Doxygen version of the documentation while the new Sphinx site is being prepared.

Per-package documentation builds
--------------------------------

Developers can build documentation for individual cloned packages by running ``scons sphinx`` from the command line.
This matches the workflow already used for code development.
Developers will build documentation for individual packages in development environments to preview changes to module documentation, including conceptual topics, examples, tasks, and API references.

.. note::

   The Doxygen-based build system uses a ``scons doc`` build command.
   This command (notwithstanding a rename) will remain to support Doxygen generation of C++ API metadata.

Internally, the ``scons sphinx`` command replaces the ``make html`` and ``sphinx-build`` drivers normally used for Sphinx documentation.
By integrating with Sphinx's internal Python APIs, rather than using ``sphinx-build``, we avoid putting ``conf.py`` Sphinx project configuration information in each package's ``doc/`` directory.
Instead, Sphinx configuration is centrally managed in SQuaRE's documenteer_ package, through sconsUtils_.

.. note::

   The single package documentation builds omit content from related packages, but will generate warnings about links to non-existent content.
   This is an acceptable trade-off for a development environment.
   In the continuous integration environment, where all documentation content is available, documentation builds can be configured to fail on broken links.

Integrated documentation: the pipelines_lsst_io repository
----------------------------------------------------------

Besides documentation embedded in Science Pipelines packages, there is a core documentation repository: https://github.com/lsst/pipelines_lsst_io.
This repository hosts higher-level documentation that crosses modules, including: installation guides, release notes, getting-started tutorials, processing and framework documentation.

When pipelines_lsst_io_ is built, the ``doc/`` directories of each package is linked into the cloned pipelines_lsst_io_ repository::

   pipelines_lsst_io/
      index.rst
      _static
      ...
      afw/ -> linked or copied from afw/doc/
      pipe_base -> linked or copied from pipe_base/doc/

With these linked package ``doc`` directories, the Sphinx build for ``pipelines_lsst_io`` is able to build all documentation simultaneously, and resolve all links within the project.

The `LTD Mason tool <ltd-mason>`_ (see SQR-006_) was designed to make the package documentation links, assuming that lsstsw was being used (as it it is in the Jenkins environment).
However, it may be more appropriate to make `pipelines_lsst_io`_ agnostic of lsstsw, which implies that `pipelines_lsst_io`_ should itself be an EUPS-managed package, and that its build logic should also be hosted in ``sconsUtils``.
