from all_tables import AllMultikinoEntities
from supporting_methods import random_date_generator

if __name__ == '__main__':
    tabs = AllMultikinoEntities()

    with open('document.txt', 'w') as f:
        for x in tabs.tab_with_all_tabs:
            print(len(x))

    # write_to_docs: bool = True
    #
    # if write_to_docs:
    #     with open('document.txt', 'w') as f:
    #         for x in tabs.all_entities:
    #             add_element, data_element = x.sql_addable, x.__dict__
    #             f.write(f'{x}\n')
                # f.write(f'{data_element} -> {add_element}\n')

    # year_start: int = 1930
    # year_end: int = 2021
    # for x in range(1000):
    #     random_date_generator(year_start, year_end)