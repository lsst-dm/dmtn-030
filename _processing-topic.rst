.. _processing-topic-type:

Processing topic type
=====================

Processing topics are a practical platform that discuss how to calibrate and measure astronomy datasets with the LSST Science Pipelines.
As discussed in :ref:`homepage-design`, processing is organized around *contexts*, such as single frames, coaddition, or difference imaging.
Each processing context has a main page that conforms to the processing topic type.

As processing topic consists of the following components:

- :ref:`Title <processing-title>`.
- :ref:`Context <processing-context>`.
- :ref:`In depth <processing-in-depth>`.
- :ref:`Tutorials <processing-tutorials>`.
- :ref:`Command line tasks <processing-tasks>`.

.. _fig-processing-mockup:

.. figure:: /_static/processing-mockup.svg
   :width: 100%

   Mockup of processing topic type pages.

.. _processing-title:

Title
-----

The name of a processing topic is the name of the processing context.
For example, "Single frame processing" or "Multi-epoch processing."

.. _processing-context:

Context
-------

Within a couple short paragraphs below the title, this component establishes the topic's context:

- Explain what the processing context *means* in non-jargon language.
  What data goes in? What data comes out?
- Link to adjacent processing contexts.
  For example, a single frame processing topic should link to the data ingest topic.
- Mention and link to the main command line tasks used in this context.
- Suggest and link to an introductory tutorial for this processing context.

.. _processing-in-depth:

In depth
--------

This section lists and links (as a ``toctree``) to separate topic pages.
Each of these self-contained topics provide in-depth background into aspects of processing in this context.
They should primarily be written as narrative glue to other types of documentation, including :ref:`frameworks <framework-type>`, :ref:`tasks <task-type>`, and :ref:`modules <module-type>`.
That is, these topics are guides into understanding the Science Pipelines from a practical data processing perspective.
The first in depth topic should be an 'Overview' that describes the processing context itself, and introduces other in-depth topics and tutorials.

Based on experience from Twinkles, a project using the LSST Science Pipelines, many of these topics can be divided into two halves: processing data in this context, and measuring objects from the products of that processing.
Processing topic pages have the flexibility to organize in depth topics (and :ref:`tutorials <processing-tutorials>`, below) around themes like this.

.. _processing-tutorials:

Tutorials
---------

The Tutorials section links (as a ``toctree``) to tutorial topic pages that demonstrate processing real datasets in this context.
These tutorials should be easily reproduced and run by readers; necessary example datasets should be provided.

These tutorials might be designed to be run as a series across several processing context.
For example, a tutorial on ingesting a dataset in the "ingest' context may be a pre-requisite tutorial for a processCcd tutorial in a "single frame processing" context.

.. _processing-tasks:

Command line tasks
------------------

Command line tasks are the primary interface for processing data with the Science Pipelines.
This final section in a processing topic lists all command line tasks associated with that processing context.
Links in this ``toctree`` are to :ref:`task topics <task-type>`.

Note that only *command line* tasks associated with a context are listed here.
This is done because the 
Processing topics are designed to be approachable for end users of the Science Pipelines.
Command line tasks are immediately usable, while sub-tasks are only details for configuration (that is, re-targettable sub tasks) or for developers of new pipelines.
Thus mentioning only command line tasks gives users a curated list of runnable tasks.
As a user gains experience with command line tasks like ``processCcd.py``, they will gradually learn about sub-tasks through links built into the `task topic` design, and thus graduate from new user to experience user and potential developer.
