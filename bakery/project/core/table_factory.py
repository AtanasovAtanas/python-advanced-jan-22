from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class TableFactory:
    table_types = {
        'InsideTable': InsideTable,
        'OutsideTable': OutsideTable,
    }

    def create_table(self, table_type: str, table_number: int, capacity: int):
        return self.__class__.table_types[table_type](table_number, capacity)
