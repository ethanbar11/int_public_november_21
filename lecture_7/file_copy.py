original_path = 'to_read.txt'
new_path = 'new_file.txt'

with open(original_path, 'r') as old_file: # old_file=open(original_path,'r')
    with open(new_path, 'w') as new_file:
        for line in old_file:
            new_file.write(line)

print('Here the file is close.')
