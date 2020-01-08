def csvify(data, column_names=None, strip=True):
    """Convert a list of lists (data) into a csv."""
    import csv
    import io
    strio_csv = io.StringIO()
    csv_writer = csv.writer(strio_csv)
    if column_names:
        column_row = []
        for column in column_names:
            if isinstance(column, str):
                column_row.append(column)
            else:
                column_row.append(column[0])
        csv_writer.writerow(column_row)
    for row in data:
        if strip:
            row = [str(element).strip() for element in row]
        csv_writer.writerow(row)
    str_csv = strio_csv.getvalue().rstrip()
    return(str_csv)


column_names = ['Fruit', 'Count']
data = [
    ['Apple', 8],
    ['  Apricot', 2],
    ['Orange', 7],
]
csv_str = csvify(data, column_names)

print(csv_str)
