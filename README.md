# mkShapesRDF: Simple Parallel RDF version of [LatinoAnalysis](https://github.com/latinos/LatinoAnalysis/)
[![Documentation Status](https://readthedocs.org/projects/mkshapesrdf/badge/?version=latest)](https://mkshapesrdf.readthedocs.io/en/latest/?badge=latest)
[![tests](https://github.com/giorgiopizz/mkShapesRDF/actions/workflows/ci_lint_format_test.yml/badge.svg)](https://github.com/giorgiopizz/mkShapesRDF/actions/workflows/ci_lint_format_test.yml)


Please refer to the [documentation](https://mkshapesrdf.readthedocs.io/en/shapes-dev-fix/index.html) for installation and a quick start guide.

Latest presentation at Latinos meeting [here](https://indico.cern.ch/event/1233729/contributions/5380538/attachments/2636898/4562210/mkShapesRDF%2026_04.pdf)

### Install

Clone the repository:

    git clone git@github.com:latinos/mkShapesRDF.git

    cd mkShapesRDF

    git checkout tags/Run3_production_v1

    source install.sh

### Setup the environment

After you install the framework, and every time you log-in, you have to setup the environment in order to use it:

    cd <your_base_directory>/mkShapesRDF/

	source start.sh

### Post-process nanoAOD files

The first step is always to setup the environment. After that, you need to create a proxy to access files in the grid:

    voms-proxy-init --voms cms -valid 192:0

The actual command to post-process files will look like the following:

    mkPostProc -o 0 Summer22EE_130x_nAODv12_Full2022v12 -s MCl2loose2022EEv12__MCCorr2022EEv12JetScaling__l2tight -T <sample_name>