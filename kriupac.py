"""
IUPAC
Nucleotide Code:  Base:
----------------  -----
A.................Adenine
C.................Cytosine
G.................Guanine
T (or U)..........Thymine (or Uracil)
R.................A or G
Y.................C or T
S.................G or C
W.................A or T
K.................G or T
M.................A or C
B.................C or G or T
D.................A or G or T
H.................A or C or T
V.................A or C or G
N.................any base
. or -............gap
"""

IUPAC_DOUBLE_DNA_DICT = {
    'AG': 'R',
    'CT': 'Y',
    'AC': 'M',
    'GT': 'K',
    'AT': 'W',
    'CG': 'S'
}
