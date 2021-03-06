from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import reflection

import pprint

pp = pprint.PrettyPrinter(indent=4)



db_uri = 'sqlite:///chinook.db'
engine = create_engine(db_uri)
metadata = MetaData()
metadata.reflect(bind=engine)

print('\n')


insp = reflection.Inspector.from_engine(engine)
print(list(insp.get_table_names()))

# album_table = (metadata.tables['albums'])
print('\n')
# print(album_table)

print('\n')
#
# for table in reversed(metadata.sorted_tables):
#     print(table)
# print('\n')
#
meta = pp.pprint(str(metadata.tables))

print('\n')



meta = pp.pprint(str(metadata.sorted_tables))

#
print('\n')

for table in metadata.tables.values():
    print(table.name)
#
# for _m in metadata.tables:
#     print("Table Names: ", _m)
