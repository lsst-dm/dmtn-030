.. _framework-type:

Framework topic type
====================

Frameworks in the LSST Science Pipelines are collections of modules that provide coherent functionality.
Rather than only documenting modules in isolation, the framework topic type is a platform for documenting overall concepts, design, and usage patterns for these frameworks that cross module bounds.

A non-exhaustive list of frameworks in the Science Pipelines is:

- Measurement framework.
- Butler framework.
- Task framework.
- Observatory interface (obs) framework.
- Modeling framework.
- Geometry framework.
- QA framework.
- Build, packaging, and utility framework.

Topic type components
---------------------

Each framework has a homepage that conforms to the *framework topic type*, which has the following components:

- :ref:`Title <framework-title>`.
- :ref:`Context <framework-context>`.
- :ref:`In depth <framework-concepts>`.
- :ref:`Tutorials <framework-tutorials>`.
- :ref:`Modules <framework-modules>`.

.. _fig-framework-mockup:

.. figure:: /_static/framework-mockup.svg
   :width: 100%

   Mockup of the framework topic type.

.. _framework-title:

Title
^^^^^

The title of the framework's topic is simply the name of the framework itself.

.. _framework-context:

Context
^^^^^^^

Following the title, the initial few paragraphs of the topic should establish context.
A context paragraph establishes what the framework is for, and what the framework's primary features or capabilities are.

.. _framework-concepts:

In depth
^^^^^^^^

This section provides a table of contents (``toctree``) for additional topics that cover individual framework concepts.
Concept topics can include guides for developing against the framework, and descriptions of the basic ideas implemented by the framework.
'*Concept*' is purposefully ambiguous but we require that concept topic pages follow the design principles of :ref:`topic-based documentation <topic-based-docs>`.

Generally, the first topic should be an overview.
The overview topic's narrative introduces and links to other framework topics.

..
  .. todo::
  
     Include examples.

.. _framework-tutorials:

Tutorials
^^^^^^^^^

The Tutorials section provides a table of contents (``toctree``) linking to separate tutorial topic pages.
These tutorials demonstrate and teach how to use and develop in the framework.

.. note::

   Additional design work is required for tutorial topic types.

.. _framework-modules:

Modules
^^^^^^^

This section lists and links to the :ref:`module topic <module-type>` of all modules included in a framework.
These links establish a connection between the high-level ideas in a framework's documentation with lower-level developer-oriented details in a module's documentation.

Framework topic type extensibility
----------------------------------

The components described above are a *minimum* set used by each framework topic.
Some frameworks may add additional components.
For example, the measurement framework might include an index of all measurement plugins.
The task framework might include an index of all tasks.
