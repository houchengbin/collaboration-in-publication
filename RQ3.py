import scholar # https://github.com/ckreibich/scholar.py
import time
import random


def list_to_txt(filename, my_dict):
    with open(filename+str('.csv'),'w') as fout:
        for key, value in my_dict.items():
            fout.write(str(key)+str(', ')+str(value))
            fout.write('\n')

def main():
    filename = 'all_papers'

    title_author_list = []
    with open(filename+str('.csv'),'r') as fin:
        for line in fin.readlines():
            title_author_list.append( [ line.split(',')[0], int(line.split(',')[1]) ] )
    print('The number of papers ------ : ', len(title_author_list))
    print('One of paper titles  ------ : ', title_author_list[99][0])

    my_querier = scholar.ScholarQuerier()
    my_querier.apply_settings(scholar.ScholarSettings())

    title_author_citation_list = []
    counter = 0
    for title_author in title_author_list:
        print('paper @ {}/{}'.format(counter,len(title_author_list)))
        
        my_query = scholar.SearchScholarQuery()
        my_query.set_words(title_author[0])
        my_querier.send_query(my_query)
        print(my_querier.articles)

        if len(my_querier.articles) == 0:
            print('NOT found... ', title_author[0])
        else:
            citation = my_querier.articles[0].attrs["num_citations"][0]
            title_author_citation_list.append(title_author.append(citation))
        time.sleep(20 + random.randint(0, 20))

if __name__ == '__main__':
    main()