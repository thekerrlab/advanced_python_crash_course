import pylab as pl

def makecumulativenumbers():
    randomnumbers = pl.randn(50,10);
    cumulativenumbers = pl.cumsum(abs(randomnumbers), axis=0)
    return cumulativenumbers