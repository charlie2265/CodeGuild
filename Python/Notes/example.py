import os
dir_name = 'csvs'

cwd = '.'
dir_path_ = os.path.join(cwd, dir_name)
csv_to_dict = {}

# print(dir_name, cwd, dir_path, sep= '\n')
for file_name in os.listdir(dir_path_):
    if file_name.endswith('.csv'):
        file_path = os.path.join(dir_path_, file_name)
        with open(file_path) as f:
            Contents = f.read().split('\n')
        csv =[]
        keys = Contents[0].split(',')
        rows = Contents[1:]
        print(keys)
        print(rows)
        print()
        for row in rows:
            row = row.split(',')
            print(row)
            row_as_dict = dict(zip(keys, row))
            csv.append(row)
            print(csv)
        csv_to_dict[file_name] = csv
print (csv)