.. _module-type:

Module topic type
=================

The module topic type comprehensively documents a *module* as an entrypoint to task and API references associated with a specific part of the codebase.

The module topic type consists of the following components:

- :ref:`Title <module-title>`.
- :ref:`Summary paragraph <module-summary>`.
- :ref:`See also <module-see-also>`.
- :ref:`Overview <module-overview>`.
- :ref:`Tasks <module-tasks>`.
- :ref:`Using \<module name\> <module-using>`.
- :ref:`Python API reference <module-api>`.
- :ref:`C++ API reference <module-api>`.
- :ref:`Packaging <module-packaging>`.
- :ref:`Related documentation <module-related-docs>`.

.. _module-title:

Title component
---------------

Since *module* is a Python-oriented, the title should be formatted as: "python module name --- Short description."
For example:

| ``lsst.afw.table`` --- Table data structures.

.. _module-summary:

Summary paragraph component
---------------------------

This paragraph establishes the context of this module, and lists key features and functionality.
This section is intended to help a reader determine whether this module is relevant to their task.

.. _module-see-also:

See also component
------------------

Right after the summary paragraph, and within a ``seealso`` directive, this component links to other parts of the documentation that do not otherwise follow from the topic type design.
For example, if the module is part of a framework, that framework's page is link from here.
This component can also be used to disambiguate commonly-confused modules.

.. _module-overview:

Overview component
------------------

If necessary, this section component links to additional pages that provide overviews and architectural background for the module.

.. todo::

   Combine with the "Using" section to form a new "In depth" section component?

.. _module-tasks:

Tasks component
---------------

This section lists and links to to task topics for any tasks implemented by this module.
The task topic type is discussed in TODO.

Minimally, this section with should be a simple list where the task name is included first as a link, followed by a short summary sentence.

It may be useful to distinguish tasks useable as command line tasks from plain tasks.
Perhaps the two types could be listed separately, with command line tasks appearing first.

.. _module-using:

Using <module name> component
-----------------------------

This section lists and links to conceptual documentation pages for the module.
Each conceptual documentation page focuses on a specific part of the API and dives into features while providing usage examples.
These pages are similar to the conceptual documentation provided in the "Using" sections of Astropy sub-packages (see `Using table <http://docs.astropy.org/en/stable/table/index.html#using-table>`__ for examples).
The ``lsst.validate.base`` prototype documentation (currently available at https://validate-base.lsst.io) includes examples of such conceptual documentation pages as well.

.. todo::

   This section could easily be combined with the Overview component.
   The new, combined section could be called "In depth."

.. _module-api:

Python and C++ API reference components
---------------------------------------

These section list and links to reference pages for all Python and C++ API objects.
Each API object (functions and classes) are documented on separate pages.
See :ref:`api-ref` for a discussion of API reference pages.

.. _module-packaging:

Packaging component
-------------------

Module exist inside EUPS packages.
This section is designed to help a user understand how to access a module, and understand how this module's package relates to other packages in the Science Pipelines documentation by:

- Stating what package a module is part of.
- Linking to that package's GitHub repository.
- Stating what top-level packages include this module's package. This help readers understand what package to install.
- Stating what packages this depend on this module's package, distinguishing between direct and in-direct dependencies. This will help developers.
- Stating what packages in the LSST Stack dependent on this package. Again, this will primarily help developers.

The package dependencies can be expressed as both lists and graph diagrams.

.. _module-related-docs:

Related documentation component
-------------------------------

A module will be documented elsewhere.
This section consists of a listing of other documents related to this module, including:

- Design documentation.
- Technotes.
- RFCs.
- Community forum conversations.

For the last item, we envision a service that can monitor https://community.lsst.org forum conversations for mentions of pre-defined keywords and automatically populate a list of related forum posts.
Linking documentation to the Community forum will help make the documentation interactive.
With minimal overhead, a reader can begin to discuss and ask questions about documentation and the LSST Science Pipelines.
