.. _homepage-design:

Designing the homepage
======================

Identifying an inventory of topic types requires foresight of what the Science Pipelines documentation will become.
We approached this by first designing the homepage for the Science Pipelines documentation.
The homepage provides a unique, overarching view into the inventory of content needed to document the full domain of the Science Pipelines for all expected audiences.

We envision four distinct areas on the homepage: :ref:`preliminaries <homepage-preliminaries>`, :ref:`processing <homepage-processing>`, :ref:`frameworks <homepage-frameworks>`, and :ref:`modules <homepage-modules>`.
Each area organizes and links to topics of distinct types.
The following sub-sections motivate each area of the homepage, while later sections describe the design of each topic type in greater detail.

.. _fig-homepage-mockup:

.. figure:: /_static/homepage-mockup.svg
   :width: 100%

   Mockup of the Science Pipelines documentation homepage layout.

.. _homepage-preliminaries:

Preliminaries section
---------------------

Above the fold, the first task of the documentation site is to address readers who have little or no knowledge with the LSST Science Pipelines.
This area contains:

- A blurb that introduces readers to the Science Pipelines.
- Links to installation topics, and EUPS usage topics.
- Links to release note topics.
- An invitation to try a quick tutorial that helps a reader understand what the Science Pipelines feel like to use.
- Links to topics describing how to contribute to the LSST Science Pipelines.
- An explanation of how to get help with the LSST Science Pipelines (that is, link to https://community.lsst.org).

In summary, this section establishes the LSST Science Pipelines as an open source software project.

.. _homepage-processing:

Processing section
------------------

A common task for readers (both community end users, and indeed, the DM team itself) is to *use* the Science Pipelines.
This is a distinct viewpoint from documenting the Science Pipelines's implementation (modules, and frameworks).
Rather, the processing section focuses on how to organize data, use command line tasks to process data, and consume those outputs for scientific investigations.
And while topics in the processing section defer to :ref:`task topics <task-type>` as definitive self-contained scientific descriptions of algorithms, the processing section is used to frame these command line tasks and help astronomers make judgments about how they are used for science.

Based on the Twinkles_ pipeline, which uses the LSST Science Pipelines, we recognized that processing can be organized into *contexts*.
Each context has a well-defined type of input, well-defined types of outputs, and well-defined types of measurements.
A core set of contexts is:

1. Data ingest. *Organizing Butler repositories for different observatories.*
2. Single frame processing. *This is primarily an introduction to ProcessCcdTask.*
3. Coaddition processing.
4. Difference image processing.
5. Multi-epoch measurement.
6. Postprocessing. *This is a discussion of output catalogs, and may need more fine-grained topical organization.*

On the homepage, each listed context is a link to a :ref:`processing topic <processing-topic-type>`.

.. note::

   LDM-151_ §5 follows a similar pattern:

   - §5.1: Image Characterization and Calibration
   - §5.2: Image Coaddition and Differencing
   - §5.3: Coadd Processing
   - §5.4: Overlap Resolution
   - §5.5: Multi-Epoch Object Characterization
   - §5.6: Postprocessing

   While LDM-151's sectioning makes sense for motivating algorithm development (LDM-151's purpose), we believe that real-world usage warrants our sugggested organization of the processing section.

.. _homepage-frameworks:

Frameworks section
------------------

To bridge high level usage documentation to low-level API references, we realized that frameworks are an ideal platform for introducing and framing implementation documentation.
Frameworks are collections of modules (possibly crossing EUPS packages) that implement functionality.
Examples of frameworks are:

- Observatory interface (obs) framework.
- Measurement framework.
- Modelling framework.
- Task framework.
- Butler (data access) framework.
- Data structures framework.
- Geometry framework.
- Display framework.
- Logging framework.
- Debug framework.
- QA (validate) framework.
- Build system.

By organizing topics around frameworks, we have a platform to discuss their functionality for both end users (how to use the framework's features) and developers (patterns for developing in and with the framework) in a way that's not constrained by implementation details (module organization).

The frameworks section of the homepage lists each framework's name, along with a descriptive subtitle.
Each item is a link to a corresponding :ref:`framework topic <framework-type>`.

.. _homepage-modules:

Modules section
---------------

The final section of the homepage is a comprehensive listing of modules in the LSST Science Pipelines.
Each item is a link to a corresponding :ref:`module topic <module-type>`.
This listing will be heavily used by developers seeking API references for the modules they are using on a day-to-day basis.

These module topics are :ref:`imported from the doc/ directories <docs-in-packages>` of each Science Pipelines EUPS package.
The homepage's module listing can be automatically compiled in a custom `reStructuredText directive <directive>`_.
