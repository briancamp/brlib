def tablify(data, column_names):
    """Convert a list of lists (data) into a ascii table."""
    import prettytable
    if not data:
        return('')

    default_alignment = 'l'
    alignments = {'left': 'l', 'right': 'r', 'center': 'c'}
    columns = []
    max_row_len = max([len(row) for row in data])
    for column in column_names:
        if isinstance(column, str):
            columns.append({'name': column})
        else:
            col = {'name': column[0]}
            for attr in column[1:]:
                if attr in alignments:
                    col['align'] = alignments[attr]
            columns.append(col)
    table = prettytable.PrettyTable([column['name'] for column in columns])
    for column in columns:
        if 'align' in column:
            table.align[column['name']] = column['align']
        else:
            table.align[column['name']] = default_alignment
    for row in data:
        row_len = len(row)
        if row_len < max_row_len:
            row = list(row)
        while len(row) < max_row_len:
            row.append('')
        table.add_row(row)
    table_str = str(table)
    return(table_str)


column_names = ['Fruit', 'Count']
data = [
    ['Apple', 8],
    ['Apricot', 2],
    ['Orange', 7],
]
table_str = tablify(data, column_names)
print(table_str)
