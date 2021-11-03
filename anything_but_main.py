from all_tables import AllTables

if __name__ == '__main__':
    tabs = AllTables()
    with open('document.txt', 'w') as f:
        for x in tabs.all_entities:
            add_element, data_element = x.sql_addable, x.__dict__
            f.write(f'{x}\n')
            # f.write(f'{data_element} -> {add_element}\n')
