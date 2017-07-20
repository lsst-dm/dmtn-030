.. _package-type:

Package topic type
==================

The package topic type documents individual stack packages (Git repositories).

The topic type consists of the following components:

- EUPS package name.
- Description.
- Git repository URL
- JIRA component for issue reporting.
- List of Python modules (linking to :ref:`module topics <module-type>`).
- User and developer documentation appropriate for the package (for example, the procedure for updating datasets in a test data repository).
- EUPS dependencies (computed both downstream and upstream).

Most documentation provided by a package is included in :ref:`module topics <module-type>`.
The package topic type, though, provides a documentation platform for the package itself.
Some packages may be documented only through the package topic type if they do not include Python APIs (such as data packages, or vendored third-party packages).
