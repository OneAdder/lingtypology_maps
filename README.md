# lingtypology
<table>
  <tr>
    <td>Latest Release</td>
    <td>
      <a href="https://pypi.org/project/lingtypology/"/>
      <img src="https://img.shields.io/pypi/v/lingtypology.svg"/>
    </td>
  </tr>
  <tr>
    <td>License</td>
    <td>
      <a href="https://github.com/OneAdder/lingtypology/blob/master/LICENSE.md"/>
      <img src="https://img.shields.io/github/license/OneAdder/lingtypology.svg"/>
    </td>
  </tr>
  <tr>
    <td>DOI</td>
    <td>
      <a href="https://doi.org/10.5281/zenodo.2669068"/>
      <img src="https://zenodo.org/badge/DOI/10.5281/zenodo.2669068.svg"/>
    </td>
  </tr>
</table>

Lingtypology is a Python3 tool for linguistic interactive mapping and online linguistic databases API.
It is inspired by [R-package](https://github.com/ropensci/lingtypology) created by [Agrizolamz](https://github.com/agricolamz).
It uses the same phylosophy and provides similar functionality.  

## Installation
The package is available in PyPI.
Therefore, you can install it by running: pip install lingtypology`

## Usage
Lingtypology package contains `LingMap` class that allows to draw interactive maps, `glottolog` library that allows to interact with Glottolog data and `datasets` that allows to interact with different other linguistic databases.  
For more informations consult [Lingtypology: Documentation](https://oneadder.github.io/lingtypology/).

## Glottolog
Lingtypology relies on data from the [Glottolog](https://glottolog.org/glottolog/language) database.
With each new version of `lingtypology` Glottolog data is updated. Now it is using Glottolog `5.0`.
You can update data from Glottolog. To get the instruction on how to do it, consult the [tutorial](https://oneadder.github.io/lingtypology/glottolog#g_version).

## Citation
If you are using this package in a scientific publication, it will be most appreciated if you add the citation:
```
@misc{MichaelVoronov2669068,
    author = {Michael Voronov},
    title = {{lingtypology: a Python tool for linguistic typology}},
    month = june,
    year = 2019,
    doi = {10.5281/zenodo.2669068},
    url = {https://doi.org/10.5281/zenodo.2669068}
}
```
