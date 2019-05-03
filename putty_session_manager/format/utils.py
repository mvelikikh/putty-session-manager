from prettytable import PrettyTable

MAX_WIDTH = 80

def list_to_table(column_names, values):
    """
    Formats list to table
    """
    table = PrettyTable(column_names)
    table._set_max_width(MAX_WIDTH)
    for i in range(len(column_names)):
        table.align[column_names[i]] = 'l'

    for i in range(len(values)):
        row = values[i]
        if isinstance(row, list):
            table.add_row(row)
        else:
            table.add_row([row])

    return table
