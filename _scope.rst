.. _scope:

Scope of the Science Pipelines documentation project
====================================================

One of the basic questions our design sprint needed to address was *what is the scope of pipelines.lsst.io?*
Typically this question is defined by a product marketing team, or by a source code repository (for instance, https://docs.astropy.org is documentation for the https://github.com/astropy/astropy software project).
In our case, the situation is complicated by the fact that Data Management software is being built by multiple teams across many coupled repositories.
Taken together, the software repositories of the Data Management System are typically called *the Stack*, but not all parts of the Stack are used together.
There are server-side database and display components, as well as pipelines algorithms bound together with middleware.

In this documentation design, our stance is to label all Data Management client-side code that is imported as the ``lsst`` Python package as *The LSST Science Pipelines*.
Specifically:

- Core frameworks, like ``afw``, are included.
- The client-side Butler is included.
- Middleware that is integral to the ``lsst`` python package, like ``logging``, is included. The backend counterparts, like an ELK stack to receive log messages is not included.
- Tasks and other algorithmic components are included.
- Display packages are included, like ``display_firefly``, though Firefly itself is not.
- Observatory interfaces maintained by DM are included.
- Despite being in the ``lsst`` namespace, LSST Simulations software **is not included** since it is managed and versioned separately. This could be redressed in the future, given how tightly coupled the DM and Simulations software is.

This package collection crosses DM team lines, but reflects how the software is used, and how it can be maintained as an open source project into the future.

.. note::

   A related issue is the name of the product itself.
   This segment of the Data Management System does not have name; while the name "Stack" is often used, that refers to all software in the DMS.

   This technote uses the branding "LSST Science Pipelines" and "pipelines.lsst.io," though technically this is an appropriation of the collective name of work by the University of Washington and Princeton teams.
   The Science Pipelines product and documentation site also includes elements from the Data Access, Science User Interface Toolkit, Middleware and SQuaRE teams.
   
   Overall, the product naming is an unresolved issue and we acknowledge that the pipelines.lsst.io branding may change.

Developer documentation
-----------------------

A related issue is how developer documentation for the Science Pipelines should be managed.
Currently, the separate `DM Developer Guide`_ contains a mixture of organizational policy documents and technical documentation needed to build DM software---including the LSST Science Pipelines.
We propose to move developer documentation tightly coupled to the LSST Science Pipelines from the `DM Developer Guide`_ project to pipelines.lsst.io, such as:

- Build system information (``lsst-build``, ``lsstsw``).
- How to create packages in ``lsst``.
- How to write tests in the ``lsst``.
- Patterns for using EUPS.

Some information in the `DM Developer Guide`_ is applicable beyond the Science Pipelines project.
In this case, information can be merely linked from pipelines.lsst.io to developer.lsst.io, such as:

- Code style guides.
- General documentation writing patterns.

Keeping policies like these in developer.lsst.io allows them to be centrally referenced by other DM projects.

Relationship to other DM documentation projects
-----------------------------------------------

The tight focus of pipelines.lsst.io necessitates other DM user guide projects.
This is anticipated by LDM-493_.

We expect pipelines.lsst.io to be joined by other software documentation projects:

- Firefly/SUIT.
- Qserv.
- Webserv/DAX.
- Various projects by SQuaRE.

There will also be "data" documentation in the operations era:

- Science Platform user guide.
- Alert Production user guide (for services and scientists that consume the alert stream).
- Data Release documentation projects, archived for each data release (DR1, DR2, and so on).

Note that the alert and data release documentation will consume the Science Pipelines documentation: those projects will describe pipelines built *from* the LSST Science Pipelines and use the algorithmic descriptions published with the pipelines code on pipelines.lsst.io.

Finally, there will be operations guides that, like developer.lsst.io, document internal processes for operating LSST.
