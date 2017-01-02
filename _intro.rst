.. _intro:

Introduction
============

The LSST Science Pipelines are a key project in the LSST Data Management System.
DM developers, data release production operators, and the LSST astronomy community at large all have a stake in using and extending the Science Pipelines.
Comprehensive and usable documentation is prerequisite for the success of these stakeholders.

This technical note describes a design for the LSST Science Pipeline's user guide.
The initial design was developed by the authors at a design sprint held in Tucson, AZ, over December 7 to 9, 2016.\ [#meeting-notes]_
As the documentation design is implemented and improved, this technical note will be updated and serve as a reference for the project's design philosophy and direction.
The LSST Science Pipelines documentation is implemented consistently with `LDM-493 Data Management Documentation Architecture <LDM-493>`_\ ’s *user guide* project class.

.. [#meeting-notes] The meeting notes are archived with this technical note as a PDF, and also available online at http://ls.st/507.

   :download:`Meeting Notes (PDF) </_static/doc-sprint-2016-12.pdf>`

The design is presented as follows.
In :ref:`Section 2 <scope>` we define the scope of the LSST Science Pipelines as a software and documentation project.
:ref:`Section 3 <audience>` describes the audience of this documentation project.
:ref:`Section 4 <docs-as-code>` lays out the *docs-as-code* technical framework within which the documentation is produced and delivered.

In later sections we present the information architecture of the Science Pipelines documentation.
:ref:`Section 5 <topic-based-docs>` introduces *topic-based* documentation as a core design philosophy.
Topic-based documentation motivates us to build standardized documentation *types* that guide authors and also establish patterns that benefit readers.
In :ref:`Section 6 <homepage-design>` we frame these topic types by mocking up the homepage of the Science Pipelines documentation website.
Following this we present designs for topic types:

- :ref:`Section 7 <processing-topic-type>`: Processing topic type.
- :ref:`Section 8 <framework-type>`: Framework topic type.
- :ref:`Section 9 <module-type>`: Module topic type.
- :ref:`Section 10 <task-type>`: Task topic type.
- :ref:`Section 11 <api-ref>`: API reference topic type, including a discussion of prototypes.
