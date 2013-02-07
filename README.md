# krpy

krpy is a collection of Python scripts, classes and functions written by Karolis Ramanauskas.

## Files

The list of files in the collection with brief descriptions.

### kralign.py

Dealing with biological sequence alignments.

### krbioio.py

Dealing with biological sequence data input/output operations.

### krbionames.py

Dealing with organism nomenclature.

### krcl.py

Dealing with command line interactions.

### krio.py

Dealing with file system operations.

### krncbi.py

Dealing with National Center for Biotechnology Information (NCBI) databases.

### krpipe.py

This file contains functions used to construct pipelines. These functions combine various other modules and do something short and useful. Output is predictable and can be used by other functions within the module. Good example of how these pipeline elements can be combined is the "search-and-align" module under pipelines directory.

### krseq.py

Dealing with various biological sequence annotations.

### krusearch.py

Working with [USEARCH](http://drive5.com/usearch)

## Dependencies

These modules depend on these Python packages:

* [Biopython](http://biopython.org)
* [Unidecode](http://pypi.python.org/pypi/Unidecode)

Some modules in this package allow for interaction with:

* [USEARCH](http://drive5.com/usearch)
* [MAFFT](http://mafft.cbrc.jp/alignment/software)
* [MUSCLE](http://www.drive5.com/muscle)
