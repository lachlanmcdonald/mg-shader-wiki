from os import path, listdir
from pybars import Compiler
from time import time
import json
import re

# LIST template marker pattern
LIST_PATTERN = re.compile(r"""
	\s*<!--\s+LIST\s+   # Start of marker
	([a-z0-9_]+)        # JSON file
	\s+                 # Mandatory whitespace
	(\d+)               # Width of image preview
	\s+-->              # End of marker
	.*?                 # HTML
	<!--\s+END\s+-->\s* # END marker
""", re.DOTALL + re.VERBOSE + re.IGNORECASE)

# SAMPLE table template
SAMPLE_PATTERN = re.compile(r"""
	[\s\n]*<!--\s+SAMPLE\s+  # Start of marker
	([a-z0-9_]+)         # JSON file
	\s+                  # Mandatory whitespace
	(\d+)                # Items per row
	\s+-->               # End of marker
	.*?                  # HTML
	<!--\s+END\s+-->[\s\n]*  # END marker
""", re.DOTALL + re.VERBOSE + re.IGNORECASE)

# Template compiler
compiler = Compiler()

with open(path.join(path.dirname(__file__), 'list.hbs')) as f:
	LIST_TEMPLATE = compiler.compile(f.read().strip())

with open(path.join(path.dirname(__file__), 'sample.hbs')) as f:
	SAMPLES_TEMPLATE = compiler.compile(f.read().strip())


# Load JSON data
DATA_DIR = path.join(path.dirname(__file__), 'data')
JSON_DATA = {}

for fp in listdir(DATA_DIR):
	if path.splitext(fp)[1] == '.json':
		with open(path.join(DATA_DIR, fp), 'r') as fh:
			k = path.basename(path.splitext(fp)[0][1:])
			JSON_DATA[k] = json.load(fh)


def chunks(j, n):
	for i in range(0, len(j), n):
		yield j[i:i + n]


def list_repl(match):
	k = match.group(1)
	width = match.group(2)
	assert k in JSON_DATA, '{} not in data ({})'.format(k, f)

	contents = LIST_TEMPLATE({
		'cache': int(time()),
		'args': ' '.join(['LIST', k, width]),
		'items': JSON_DATA[k],
		'width': width
	})
	return '\n\n' + contents + '\n\n'


def arg_sample_repl(match):
	k = match.group(1)
	per_row = int(match.group(2))
	assert k in JSON_DATA, '{} not in data ({})'.format(k, f)

	contents = SAMPLES_TEMPLATE({
		'args': ' '.join(['SAMPLE', k, str(per_row)]),
		"has_value_label": any([ 'value' in j or 'label' in j for j in JSON_DATA[k]]),
		"has_text": any([ 'raw' in j or 'text' in j for j in JSON_DATA[k]]),
		'rows': list(chunks(JSON_DATA[k], per_row)),
		'width': re.sub(r'\.?0+%$', '%', "{:.2f}%".format(100 / per_row))
	})
	return '\n\n' + contents + '\n\n'


# Process markdown files
for f in listdir(path.dirname(__file__)):
	if path.splitext(f)[1] == '.md' and f.startswith('_') is False:
		with open(f, 'r') as h:
			contents = h.read()
			new_contents = LIST_PATTERN.sub(list_repl, contents)
			new_contents = SAMPLE_PATTERN.sub(arg_sample_repl, contents)

		if contents != new_contents:
			with open(f, 'w') as h:
				h.write(new_contents)
