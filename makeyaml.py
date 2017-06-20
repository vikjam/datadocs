import yaml
import csv
import collections
from xlrd import open_workbook

wb = open_workbook('docs/databases.xlsx')

for sheet_name in wb.sheet_names():
    sheet                   = wb.sheet_by_name(sheet_name)
    database                = dict()
    database['title']       = sheet_name
    database['description'] = "Description for the database"
    database['categories']  = list()
    number_of_rows          = sheet.nrows
    number_of_columns       = sheet.ncols

    for row in range(0, number_of_rows):
        if sheet.cell(row, 3).value == '':
            database['categories'].append(dict())
            database['categories'][-1]['title']       = sheet.cell(row, 0).value
            database['categories'][-1]['description'] = sheet.cell(row, 1).value
            database['categories'][-1]['fields']      = list()
        else:
            database['categories'][-1]['fields'].append(dict())
            database['categories'][-1]['fields'][-1]['name']        = sheet.cell(row, 0).value
            database['categories'][-1]['fields'][-1]['description'] = sheet.cell(row, 4).value

            field_type = sheet.cell(row, 3).value
            if field_type == 'Cont' or field_type == 'float':
                database['categories'][-1]['fields'][-1]['type'] = 'Numeric'
            elif field_type == 'string':
                database['categories'][-1]['fields'][-1]['type'] = 'Text'
            elif field_type == 'disc' or field_type == 'integer':
                database['categories'][-1]['fields'][-1]['type'] = 'Boolean'
            else:
                database['categories'][-1]['fields'][-1]['type'] = 'Categorical'

    yaml_filename = 'docs/{database_name}.yaml'.format(database_name = sheet_name)
    with open(yaml_filename, 'w') as yaml_file:
        yaml.dump(database, yaml_file, default_flow_style = False)

    fields = []
    for category in database['categories']:
        for field in category['fields']:
            fields.append(field['name'])

    csv_filename = 'docs/{database_name}.csv'.format(database_name = sheet_name)
    with open(csv_filename, 'w') as csvfile:
        writer = csv.writer(csvfile,
                            delimiter =',')
        writer.writerow(fields)
