import pylab as pl
import sciris as sc

citations_dict = {'kenji doya':6363, 'erik de schutter':6366, 'eve marder': 27480}
citations_odict = sc.odict({'kenji doya':6363, 'erik de schutter':6366, 'eve marder': 27480})

total_citations = pl.array(citations_dict.values()).sum()
total_citations = citations_odict[:].sum()

alphabetized_dict = {key:citations_dict[key] for key in sorted(list(citations_dict.keys()))}
alphabetized_odict = citations_odict.sorted()

first_entry = alphabetized_dict[list(alphabetized_dict.keys())[0]]
first_entry = alphabetized_odict[0]

alphabetized_odict.sorted(sortby=pl.argsort(alphabetized_odict[:]))
alphabetized_odict.sorted('values')