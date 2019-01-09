import bibtexparser
# import re

def remove_line_feed(bib_dict):
    for key, value in bib_dict.items():
        bib_dict[key] = value.replace('\n',' ')
    return bib_dict

def remove_comma(bib_dict):
    for key, value in bib_dict.items():
        bib_dict[key] = value.replace(',',' ')
    return bib_dict

def dict_to_txt(filename, my_dict):
    with open(filename+str('.csv'),'w') as fout:
        for key, value in my_dict.items():
            fout.write(str(key)+str(', ')+str(value))
            fout.write('\n')

def main():
    filename = 'TKDE15'

    with open(filename+str('.bib'),'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    papers = bib_database.entries
    print('The number of papers ------ : ', len(papers))

    title_author_dict = {}

    for paper in papers:
        paper = remove_line_feed(paper)
        paper = remove_comma(paper)
        # print(paper['title'])
        # print(paper['author'])
        # title_author_dict[paper['title']] = paper['author']
        authors = paper['author'].split('and')
        num_authors = len(authors)
        title_author_dict[paper['title']] = num_authors

    print(title_author_dict)

    dict_to_txt(filename, title_author_dict)

if __name__ == '__main__':
    main()
