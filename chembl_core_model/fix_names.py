import re
import os
import sys

path = 'migrations'

re_pat = re.compile("(\s*)'db_table'\s*:\s*'(\w+)'\s*(.*)")

for item in os.listdir(path):
	if item == '__init__.py':
		continue

	content = ''
	item_path = path + '/' + item	
	with open(item_path, 'r') as f:
		for line in f:
			match = re_pat.search(line)
			if not match is None:
				table =  match.group(2)
				if table != 'compound_mols':
					print 'Table: -' + table + "-"
					table = table.replace('_','')
					content += match.group(1) + "'db_table':'chembl_core_model_"+table+"'"+match.group(3)+"\n"
				else:
					content += line
			else:
				content += line			
	with open(item_path, 'w') as fw:
		fw.write(content)
