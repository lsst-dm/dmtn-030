.. _task-type:

Task topic type
===============

The *task* topic type defines how tasks in the LSST Science Pipelines are documented.
Tasks are basic algorithmic units that are assembled into processing pipelines.
Astronomers will use task topics to understand these algorithms and identify implications for their science.
Users will refer to task topics to learn how to configure and run pipelines.
Developers will use task topics to learn how to connect tasks into pipelines.
Thus these topics are important for both astronomy end users and developers.

Currently the Science Pipelines have two flavors of tasks: tasks, and *command line* tasks.
Though command line tasks have additional capabilities over plain tasks, those capabilities are strict supersets over the regular task framework.
In other words, a command line task is also a task.
The topic type design reflects this by making no significant distinction between tasks and command line tasks with two design principles.
First, command line task topics will have additional sections.
Second, tasks and counterpart command line tasks are documented as the same identity.

Soon, a new SuperTask framework will replace command line tasks (though like command line tasks, they are still subclasses of a base ``Task`` class).
SuperTasks will allow a task to be activated from a variety of contexts, from command line to cluster workflows.
By documenting the core task and extending that documentation with additional 'activation' details, the task topic type should gracefully evolve with the SuperTask framework's introduction.

A task topic consists of the following components:

- :ref:`Title <task-topic-summary>`.
- :ref:`Summary sentence <task-topic-processing-sketch>`.
- :ref:`Processing sketch <task-topic-seealso>`.
- :ref:`Module membership <task-topic-module-membership>`.
- :ref:`See also <task-topic-seealso>`.
- :ref:`Configuration <task-topic-configuration>`.
- :ref:`Entrypoint <task-topic-entrypoint>`.
- :ref:`Butler inputs <task-topic-butler-inputs>`.
- :ref:`Butler outputs <task-topic-butler-outputs>`.
- :ref:`Examples <task-topic-examples>`.
- :ref:`Debugging variables <task-topic-debugging>`.
- :ref:`Algorithm details <task-topic-notes>`.

.. note::

   This topic design replaces earlier patterns for documenting tasks.
   Archives of documentation for the previous system are included in this technote.

   - :download:`How to Document a Task </_static/how-to-document-a-task.pdf>` (Confluence; September 23, 2014).
   - :download:`AstrometryTask </_static/astrometrytask-doxygen.pdf>`: example of task documentation implemented in Doxygen.

.. _fig-task-mockup:

.. figure:: /_static/task-mockup.svg
   :width: 100%

   Mockup of the task topic type.

.. _task-topic-title:

Title
-----

A task topic's title is the name of the task's class.
For example,

| ProcessCcdTask

.. note::

   Following the design principle that command line tasks be documented with the underlying task itself, the title should *not* be the command line script's name, such as "processCcd.py."

   We should monitor how the SuperTask command line activator refers to tasks; it may make sense for SuperTasks to always use the task's class name rather than use an alternate form.

.. note::

   An alternative to forming the title from *only* the task's class name is to add a description, for example:

   | ProcessCcdTask — Calibrate and measure a single exposure

   A summary is already provided with the :ref:`task-topic-summary` component, but including a summary in the title may improve the usability of the task listing from :ref:`module topics <module-type>` and processing topic pages.

.. _task-topic-summary:

Summary sentence
----------------

This sentence, appearing directly below the title, has two goals: indicate that the page is for a task, and succinctly describe what the task does.
This sentence is important for establishing *context*; readers should be able to use this sentence to quickly determine if the page is relevant to their task.

.. _task-topic-processing-sketch:

Processing sketch
-----------------

Appearing after the summary sentence as one or more distinct paragraphs and lists, this component provides additional details about what the task does.
A processing sketch might list the methods and sub-tasks called, in order or execution.
Mentions of methods and sub-tasks should be linked to the API reference and task topic pages, respectively, for those objects.

Like the summary sentence, this component is intended to quickly establish the task's context.
This sketch should not be extensive; detailed academic discussion of an algorithm and technical implementation should be deferred to the :ref:`task-topic-notes` component.

.. _task-topic-module-membership:

Module membership
-----------------

In a separate paragraph after the processing sketch, this component states what module implemented the task:

| AstrometryTask is part of the ``lsst.meas.astrom.astrometry`` module.

The module mention is a link to the :ref:`module's topic <module-type>`.

This component establishes the task's code context, which is useful for developers.

.. _task-topic-seealso:

See also
--------

Wrapped inside a ``seealso`` directive, this component links to related content, such as:

- Tasks that commonly use this task (this helps a reader landing on a "sub task's" page find the appropriate driver task).
- Tasks that can be used *instead of* this task (to link families of sub tasks).
- Pages in the :ref:`Processing <homepage-processing>` and :ref:`Frameworks <homepage-frameworks>` sections of the Science Pipelines documentation.

.. _task-topic-configuration:

Configuration
-------------

This section describes the task's configurations defined in the task class's associated configuration class.
Configuration parameters are displayed similarly to attributes in Numpydoc with the following fields per configuration:

- Parameter name.
- Parameter type. Ideally the parameter type links to a documentation topic for that type (such as a class's API reference).
- A description sentence or paragraph. The description should mention default values, caveats, and possibly an example.

We anticipate that a reStructuredText directive can be built to automatically generate this topic component.

.. _task-topic-entrypoint:

Entrypoint
----------

The entrypoint section documents the task's 'run' method.
Note that task run methods are not necessarily named 'run,' nor do they necessarily share a uniform interface.

Initially this section will only contain the namespace of the run method, such as

| ``lsst.meas.astrom.astrometry.AstrometryTask.run``

(with the namespace linked to the method's API reference).

Later, a custom directive may automatically replicate information from the method's API reference and insert it into the Entrypoint section (recall that topics should be self-contained).

.. todo::

   We may also need to add a section on Task class initialization.

.. _task-topic-butler-inputs:

Butler inputs
-------------

This section documents datasets that this task (as a command line task) consumes from the Butler.

For each ``Butler.get()``, this section lists standardized entries with:

- Dataset type (linked to the dataset type's class documentation).
- A free-form description.

We anticipate that the SuperTask framework will provide hooks for auto-documenting this.

.. _task-topic-butler-outputs:

Butler outputs
--------------

This section documents datasets that this task (as a command line task) consumes from the Butler.

For each ``Butler.put()``, this section lists standardized entries with:

- Dataset type (linked to the dataset type's class documentation).
- A free-form description.

Again, we anticipate that the SuperTask framework will provide hooks for auto-documenting this.

.. _task-topic-examples:

Examples
--------

The section provides one or more runnable examples that demonstrate both the task's usage within Python, and from teh command line.

More design work is needed to implement examples.
The examples should fulfill the following criteria:

- Test data sets to run the example should be documented and made accessible to the reader.
- The example should be runnable by a reader within minimal work. That is, the example includes all surrounding boilerplate.
- The example should also be runnable from a continuous integrated context, with verifiable outputs.
- Where an example includes a large amount of boilerplate, it should be possible to highlight the parts most relevant to the task itself.

Many tasks already have associated examples in the host package's ``examples/`` directory.
As an early implementation, these examples can be copied into the documentation build and linked from this section.
For example:

| **Examples**
| 
| - ``exampleModule.py`` — Description of the example.

.. _task-topic-debugging:

Debugging variables
-------------------

This section documents all variables available in the task for the debugging framework.
Like Numpydoc 'Arguments' fields, for each debug variable the following fields are documented:

- Variable name.
- Variable type (linking to the type's API reference).
- Free-form description. The description should indicate default values, and if the variable is a complex type, include an example.

This section also includes a link to the debug framework's topic page so that the debug framework itself isn't re-documented in every task page.

.. _task-topic-notes:

Algorithm notes
---------------

This section can contain extended discussion about an algorithm.
Mathematical derivations, figures, algorithm workflow diagrams, and literature citations can all be included in the Algorithm notes section.

Note that this section is the definitive scientific description of an algorithm.
Docstrings of methods and functions that (at least partially) implement an algorithm can defer to this section.
This design makes it easier for scientific users to understand algorithms without following method call paths, while allowing method and function docstrings to focus on technical implementation details (such as arguments, returns, exceptions, and so forth).
