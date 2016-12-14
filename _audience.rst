The audience of pipelines.lsst.io
=================================

Audience is a fundamental driver of design.
In our documentation design exercise, we attempted to identify who the core users of the LSST Science Pipelines are, and what their documentation needs are.

We identified the following groups:

- **DM Developers.** From a construction standpoint, this is the key audience. It is also the most active audience. DM developers need:

  - Complete and accurate API references. Currently developers learn by introspecting APIs and reading other code and tests that consume an API. The current Doxygen site is not useful.
  - Descriptions of how tasks fit together; both API-wise and from a high-level algorithmic perspective.
  - Examples.
  - Tutorials and other documentation for running pipelines on validation clusters.

- **Construction-era science collaborations.** We find that most astronomers using the LSST Science Pipelines are not processing data, but rather are using it as a core library for the Simulations stack (such as the Metrics Analysis Framework to motivate the `Observing Strategy Whitepaper`_).

- **DESC.** This collaboration is exceptional in that it wants to process data using the Science Pipelines, contribute packages (Twinkles) and provide algorithmic feedback. DESC needs:

  - Developer documentation (to support their own package development).
  - Algorithm background (to comment on).
  - Documentation on how to run pipelines on their own infrastructure.

- **LSST operators and scientists in operations.**

  - The Science Directorate will have very similar needs to DM developers now.
  - DRP will need documentation on how the Science Pipelines work, but will augment this with internal operations guides (which are out of scope).

- **Astronomers using the LSST Science Platform in operations.**

  - Typical SDSS usage is: small queries to subset data; complex queries to get objects of interest.
  - Astronomers will want to run pipeline tasks on a subset of data with customized algorithms.
  - Astronomers will use the Butler to get and put datasets within their storage quota.
  - Develop and test algorithms that may be proposed for incorporation in DRP (though an atypical scenario).

- **Other observatories and surveys.**

We conclude that DM is the most active user group, and also has the greatest documentation needs.
The needs of other groups are consistent with DM's.
From a user research perspective this is useful, because if we build pipelines.lsst.io with DM's own needs in mind, the documentation will also be immediately useful for other groups.
As the project matures, we can add tutorial documentation to help other user groups.
