#!/usr/bin/env python
#
# Sphinx configuration file
# see metadata.yaml in this repo for to update document-specific metadata

import os
from documenteer.sphinxconfig.technoteconf import configure_technote

# Ingest settings from metadata.yaml and use documenteer's
# configure_sphinx_design_doc to build a Sphinx configuration that is
# injected into this script's global namespace.
metadata_path = os.path.join(os.path.dirname(__file__), 'metadata.yaml')
with open(metadata_path, 'r') as f:
    confs = configure_technote(f)
g = globals()
g.update(confs)

# ignore technote partials
exclude_patterns.append('_*.rst')
