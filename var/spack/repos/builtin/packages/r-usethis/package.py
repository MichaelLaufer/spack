# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RUsethis(RPackage):
    """Automate package and project setup tasks that are otherwise performed
    manually. This includes setting up unit testing, test coverage, continuous
    integration, Git, 'GitHub', licenses, 'Rcpp', 'RStudio' projects, and
    more."""

    homepage = "https://usethis.r-lib.org/"
    url      = "https://cloud.r-project.org/src/contrib/usethis_1.5.1.tar.gz"
    list_url = "https://cloud.r-project.org/src/contrib/Archive/usethis"

    version('1.6.1', sha256='60339059a97ed07dea7f8908b828b5bb42e0fd0b471165c061bc9660b0d59d6f')
    version('1.5.1', sha256='9e3920a04b0df82adf59eef2c1b2b4d835c4a757a51b3c163b8fc619172f561d')

    depends_on('r@3.2:', type=('build', 'run'))
    depends_on('r-clipr@0.3.0:', type=('build', 'run'))
    depends_on('r-clisymbols', when='@:1.5', type=('build', 'run'))
    depends_on('r-cli', when='@1.6.1:', type=('build', 'run'))
    depends_on('r-crayon', type=('build', 'run'))
    depends_on('r-curl@2.7:', type=('build', 'run'))
    depends_on('r-desc', type=('build', 'run'))
    depends_on('r-fs@1.3.0:', type=('build', 'run'))
    depends_on('r-gh', type=('build', 'run'))
    depends_on('r-gh@1.1.0', when='@1.6.1:', type=('build', 'run'))
    depends_on('r-git2r@0.23:', type=('build', 'run'))
    depends_on('r-glue@1.3.0:', type=('build', 'run'))
    depends_on('r-purrr', type=('build', 'run'))
    depends_on('r-rematch2', when='@1.6.1:', type=('build', 'run'))
    depends_on('r-rlang', type=('build', 'run'))
    depends_on('r-rlang@0.4.3', when='@1.6.1:', type=('build', 'run'))
    depends_on('r-rprojroot@1.2:', type=('build', 'run'))
    depends_on('r-rstudioapi', type=('build', 'run'))
    depends_on('r-whisker', type=('build', 'run'))
    depends_on('r-withr', type=('build', 'run'))
    depends_on('r-yaml', type=('build', 'run'))