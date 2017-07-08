.. _module-type:

Module topic type
=================

The module topic type comprehensively documents a *module* as an entrypoint to task and API references associated with a specific part of the codebase.

The module topic type consists of the following components:

- :ref:`Title <module-title>`.
- :ref:`Summary paragraph <module-summary>`.
- :ref:`See also <module-see-also>`.
- :ref:`In depth <module-in-depth>`.
- :ref:`Tasks <module-tasks>`.
- :ref:`Python API reference <module-api>`.
- :ref:`C++ API reference <module-api>`.
- :ref:`Related documentation <module-related-docs>`.

.. _fig-module-mockup:

.. figure:: /_static/module-mockup.svg
   :width: 100%

   Mockup of module topic types.

.. _module-title:

Title
-----

Since "module" is a Python-oriented term, the title should be formatted as: "python module name --- Short description."
For example:

| ``lsst.afw.table`` --- Table data structures.

.. _module-summary:

Summary paragraph
-----------------

This paragraph establishes the context of this module and lists key features.
This section is intended to help a reader determine whether this module is relevant to their task.

.. _module-see-also:

See also
--------

Right after the summary paragraph, and within a ``seealso`` directive, this component links to other parts of the documentation that do not otherwise follow from the topic type design.
For example, if the module is part of a framework, that framework's page is linked from here.
This component can also be used to disambiguate commonly-confused modules.

.. _module-in-depth:

In depth
--------

This section lists and links to conceptual documentation pages for the module.
Each conceptual documentation page focuses on a specific part of the API and dives into features while providing usage examples.
The topics can also document architectural decisions.
These pages are similar to the conceptual documentation provided in the "Using" sections of Astropy sub-packages (see `Using table <http://docs.astropy.org/en/stable/table/index.html#using-table>`__ for examples).
The ``lsst.validate.base`` prototype documentation (currently available at https://validate-base.lsst.io) includes examples of such conceptual documentation pages as well.

.. _module-tasks:

Tasks
-----

This section lists and links to task topics for any tasks implemented by this module.
The task topic type is discussed in :ref:`task-type`.

Minimally, this section should be a simple list where the task name is included first as a link, followed by a short summary sentence.

.. note::

   It may be useful to distinguish tasks usable as command line tasks from plain tasks.
   Perhaps the two types could be listed separately, with command line tasks appearing first.

.. _module-api:

Python and C++ API reference
----------------------------

These sections list and link to reference pages for all Python and C++ API objects.
Individual functions and classes are documented on separate pages.
See :ref:`api-ref` for a discussion of API reference pages.

.. _module-related-docs:

Related documentation
---------------------

Modules will be documented and discussed elsewhere.
This section consists of a listing of other documents related to this module, including:

- Design documentation.
- Technotes.
- RFCs.
- Community forum conversations.

For the last item, we envision a service that can monitor https://community.lsst.org forum conversations for mentions of pre-defined keywords and automatically populate a list of related forum posts.
Linking documentation to the Community forum will help make the documentation interactive.
With minimal overhead, a reader can begin to discuss and ask questions about documentation and the LSST Science Pipelines.
