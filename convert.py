from os import path, listdir
import yaml
import json

DATA_DIR = path.join(path.dirname(__file__), 'data')

for fp in listdir(DATA_DIR):
	if path.splitext(fp)[1] == '.json':
		with open(path.join(DATA_DIR, fp), 'r') as fh:
			data = json.load(fh)

		new_path = path.splitext(fp)[0] + '.yml'
		with open(path.join(DATA_DIR, new_path), 'w') as fh:
			yaml.safe_dump(data, fh, default_flow_style=False, allow_unicode=True)
