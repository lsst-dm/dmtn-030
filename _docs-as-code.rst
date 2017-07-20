.. _docs-as-code:

Documentation as code
=====================

The Science Pipelines documentation uses a *documentation-as-code* architecture.
Documentation is stored and versioned in pipelines package repositories and built by DM's standard continuous integration system with Sphinx_ into a static HTML site that is published to the web with `LSST the Docs`_.

This section outlines the basic technical design of the Science Pipelines documentation, including the layout of documentation in packages, and the system for linking package documentation into the root pipelines_lsst_io_ project.

.. _main-repo:

The pipelines_lsst_io repository
--------------------------------

The main Git repository for the Science Pipelines documentation is https://github.com/lsst/pipelines_lsst_io.
This repository provides the main Sphinx_ project structure that is ultimately built when we deploy a new version of the Science Pipelines documentation.
pipelines_lsst_io_ contains some content, namely:

- The :ref:`homepage <homepage-design>`.
- Getting-started tutorials and overviews.
- Installation documentation.
- Release notes and other project-wide documentation.
- Homepages for the :ref:`processing topics <processing-topic-type>`.
- Homepages for the :ref:`framework topics <framework-type>`.

Most content, however, is stored in the Git repositories of individual packages and linked into the pipelines_lsst_io_ project at build time, as described in the following section.

pipelines_lsst_io_ is an EUPS package itself and includes a ``ups/pipelines_lsst_io.table`` file.
We use the table file to manage the list of packages that the Science Pipelines documentation project covers.
By using the EUPS :command:`setup` command, the documentation build system can activate the correct set and versions of packages to build the Science Pipelines documentation.

.. _docs-in-packages:

Organization of documentation in packages
-----------------------------------------

Each EUPS-managed LSST Science Pipelines package includes a ``doc/`` directory that contains documentation specific to that package.
The arrangement of documentation *within* the ``doc/`` directory is motivated by the need to have package documentation mesh into the root ``pipelines_lsst_io`` project.

A package provides two types of content:

1. **Documentation for Python modules,** such as ``lsst.afw.table``.
   This documentation content is oriented towards the code base, APIs, and its usage.
   The bulk of Science Pipelines documentation is organized around Python modules.
   We describe this content further in :ref:`module-type`.
2. **Documentation for the package itself** such as ``afw``.
   This documentation concerns the Git repository itself and may provide developer documentation that is not oriented around Python modules.
   In fact, some packages, like ``afwdata`` or ``verify_metrics``, do not have any APIs and are entirely documented through this type of documentation.
   We describe this content in :ref:`package-type`.

Documentation of these two types are packaged into directories inside a package's ``doc/`` directory.
For example, the ``afw`` package (which provides several Python modules) has documentation arranged like this::

   doc/
     index.rst
     manifest.yaml
     conf.py
     _static/
       afw/
         .. static content downloads
     afw/
       index.rst
       .. additional content
     lsst.afw.cameraGeom/
       index.rst
       ..
     lsst.afw.coord/
       index.rst
       ..
     lsst.afw.detection/
       index.rst
       ..
     lsst.afw.display/
       index.rst
       ..
     lsst.afw.fits/
       index.rst
       ..
     lsst.afw.geom/
       index.rst
       ..
     lsst.afw.gpu/
       index.rst
       ..
     lsst.afw.image/
       index.rst
       ..
     lsst.afw.math/
       index.rst
       ..
     lsst.afw.table/
       index.rst
       ..

Package-oriented documentation is contained in a directory named after the package/Git repository itself.
For ``afw``, this is the ``doc/afw/`` directory.

Each module's documentation is contained in a directory named after the Python namespace of the module itself.
For example, ``doc/lsst.afw.cameraGeom``.

The ``_static/afw/`` directory hosts static files for the package's documentation.
In Sphinx, "static" files are directly copied to the output built without intermediate processing.
These could be PDFs or tarball downloads.
This static content is stored in a ``_static/`` directory.
So that static content from all packages can be integrated, each package must store static content in a sub-directory of the ``_static`` directory, such as ``_static/afw``.

Each package also has ``doc/conf.py`` and ``doc/index.rst`` files, these facilitate :ref:`single-package development builds <per-package-builds>`.

Finally, the ``doc/manifest.yaml`` file facilitates integrated documentation builds, as described in the :ref:`next section <integrated-build>`.

.. note::

   The ``doc/`` directory was already used by the previous Doxygen-based documentation build system.
   However, during the transition from Doxygen to Sphinx-based builds, we do not expect any conflicts since content for the two system reside in non-overlapping files (``.dox`` versus ``.rst`` files for Doxygen and Sphinx, respectively).
   It should be possible to continue to build a Doxygen version of the documentation while the new Sphinx site is being prepared.

.. _integrated-build:

Integrated documentation: linking package documenation into the pipelines_lsst_io repository
--------------------------------------------------------------------------------------------

When pipelines_lsst_io_ is built, the package, module, and ``_static`` documentation directories of each package are linked into the cloned pipelines_lsst_io_ repository::

   pipelines_lsst_io/
      index.rst
      ..
      modules/
        lsst.afw.cameraGeom/ -> link to /afw/doc/lsst.afw.cameraGeom/
        ..
      packages/
        afw/ -> link to /afw/doc/afw/
        ..
      _static
        afw/ -> link to /afw/doc/_static/afw
        ..

Module documentation directories are symlinked into pipelines_lsst_io_\ ’s ``modules/`` directory.
Likewise, package documentation directories are symlinked into pipelines_lsst_io_\ ’s ``packages/`` directory. With all documentation content directories linked into the pipelines_lsst_io_ directory, Sphinx is able to build the LSST Science Pipelines documentation as if it were a unified project.

Packages declare their module, package, and ``_static`` documentation directories with their own ``doc/manifest.yaml`` files.
As an example, the ``doc/manifest.yaml`` file included in ``afw`` may look like this:

.. code-block:: yaml

   # Name of the package and also name of the package doc directory
   package: "afw"

   # Names of module doc directories;
   # same as Python namespaces.
   modules:
     - "lsst.afw.cameraGeom"
     - "lsst.afw.coord"
     - "lsst.afw.detection"
     - "lsst.afw.display"
     - "lsst.afw.fits"
     - "lsst.afw.geom"
     - "lsst.afw.gpu"
     - "lsst.afw.image"
     - "lsst.afw.math"
     - "lsst.afw.table"

   # Names of static content directory
   # Usually just one directory
   statics:
     - "_static/afw"

The tool responsible for linking package documentation and running the Sphinx build is ``build-stack-docs``, included in the documenteer_ project.

.. _per-package-builds:

Per-package documentation builds
--------------------------------

Developers can build documentation for individual cloned packages by running ``scons sphinx`` from the command line.
This matches the workflow already used for code development.
Developers will build documentation for individual packages in development environments to preview changes to module documentation, including conceptual topics, examples, tasks, and API references.

.. note::

   The Doxygen-based build system uses a ``scons doc`` build command.
   This command (notwithstanding a likely rename to ``scons doxygen``) will remain to support Doxygen generation of C++ API metadata.

Internally, the ``scons sphinx`` command replaces the ``make html`` and ``sphinx-build`` drivers normally used for Sphinx documentation.
By integrating with Sphinx's internal Python APIs, rather than using ``sphinx-build``, we avoid putting ``conf.py`` Sphinx project configuration information in each package's ``doc/`` directory.
Instead, Sphinx configuration is centrally managed in SQuaRE's documenteer_ package, through sconsUtils_.

.. note::

   The single package documentation builds omit content from related packages, but will generate warnings about links to non-existent content.
   This is an acceptable trade-off for a development environment.
   In the continuous integration environment, where all documentation content is available, documentation builds can be configured to fail on broken links.
