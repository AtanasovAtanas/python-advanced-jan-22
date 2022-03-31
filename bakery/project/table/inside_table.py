from project.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def min_table_number(self):
        return 1

    @property
    def max_table_number(self):
        return 50

    @property
    def table_number_error_message(self):
        return "Inside table's number must be between 1 and 50 inclusive!"
