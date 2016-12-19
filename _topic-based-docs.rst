Topic-based documentation
=========================

The Science Pipelines documentation, following the proposed `LDM-493 Data Management Documentation Architecture <LDM-493>`_, will use *topic-based* content organization.
In this approach, content is organized into into self-contained, well-structured pieces that support a reader's current task, and that link the reader to other topics for related details.
Topic-based content differs from books, research articles, and indeed, paper manuals, where a reader is expected to gradually accumulate knowledge and context through a preset narrative.
In task-based documentation, readers drop into specific pages to support a specific objective, but can follow links to establish context, and in effect, build a personalized curriculum for learning and using the software.

.. In the same way that documentation-as-code is a governing principle that governs the technical structure, *topics* govern the content structure of the Science Pipelines documentation.

.. Fundamentally, topic-based documentation followed from the acknowledgment that the web is the *primary* medium for distributing information, and that manuals formatted like books are not effective on the web.
.. Whereas the stacking of pages leads books to assume that readers consume and gain knowledge linearly from front to back, the web is intrinsically non-linear.
.. Links and search engines can drop a reader anywhere into a website.
.. Unlike a book, it's entirely unlikely that readers will encounter the table of contents before the content itself.
.. Topic-based documentation is designed to work under these common circumstances.

The topic-based documentation approach is widely employed by the technical writing community.
Help sites from companies like `GitHub <https://help.github.com>`__ and `Slack <https://help.slack.com>`__ use topic-based documentation.
Open source projects like `Astropy <https://docs.astropy.org>`__ also use elements of topic-based documentation philosophy.
`Wikipedia <https://en.wikipedia.org/wiki/Topic-based_authoring>`__ is an excellent example of organically-evolving topic-based documentation.
The (currently proposed) LDM-493 Data Management Documentation Architecture also identifies topic-based documentation as the information architecture of DM's user guides.
Every Page is Page One by Mark Baker, hereafter referred to as *EPPO*, describes the motivation and principles of topic-based documentation. 
This section is intended to brief the Data Management team on topic-based documentation concepts, following EPPO.

.. TODO make a bibtex citation to EPPO.

In topic-based documentation, a topic *often* maps to an individual HTML page or reStructuredText source file.
Baker, in EPPO 6.8, identified the following design principles of topics:

| 1. Self-contained.
| 2. Specific and limited purpose.
| 3. Conform to type.
| 4. Establish context.
| 5. Assume the reader is qualified.
| 5. Stay on one level.
| 6. Link richly.

Topic types
-----------

In this planning exercise, principle #3 is immediately relevant.
Topic types are predefined structures for documentation, and every implemented topic page inherits from one of these types.
For writers, topic types are valuable since provide a strong template into which the domain expert's knowledge can be filled.
Topic types are also valuable to readers since they provide systematic patterns that can be learned and used as wayfinding.
For example, Numpydoc Python API references are built on a topic type (perhaps a few, for classes and for function and for indices).
Authors immediately know how to write a Python API references, and readers immediately know how to use a Python API reference page when they see one.

Defining topic types requires us to identify every topic of documentation we will write (alternatively, each kind of thing that must be documented).
Then the topic type can be implemented as a template given to authors.
The template itself imbues topic instances with many of the characteristics of an EPPO topic, but should be backed up with authoring instructions.
Section TODO of this technote identifies the primary topic types in the Science Pipelines documentation, and those types are designed in later sections.

.. TODO add links

Topic scope
-----------

Another aspect critical for this planning exercise is that topics are self-contained (principle #1), and have a specific and limited purpose (#2).
This mean that each documentation page can be outlined a priori with:

- A title.
- A purpose and scope.
- Known related documents that the page can link to, rather than duplicate.

Thus many authors can work on separate topics in parallel, knowing that each topic conforms to a uniform type pattern, and is supported by topics.
In software architecture parlance, *topics have well-defined interfaces*.
Topic-based documentation can be much more effectively planned and managed than traditional narrative writing.
