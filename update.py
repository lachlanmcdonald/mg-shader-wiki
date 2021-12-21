from os import path, listdir
from pybars import Compiler
import sys
import yaml
import re

# LIST template marker pattern
LIST_PATTERN = re.compile(r"""
	[\s\n]*<!--\s+LIST\s+    # Start of marker
	([a-z0-9_]+)             # YAML file
	\s+                      # Mandatory whitespace
	(\d+)                    # Width of image preview
	\s+-->                   # End of marker
	.*?                      # HTML
	<!--\s+END\s+-->[\s\n]*  # END marker
""", re.DOTALL + re.VERBOSE + re.IGNORECASE)

# SAMPLE table template
SAMPLE_PATTERN = re.compile(r"""
	[\s\n]*<!--\s+SAMPLE\s+  # Start of marker
	([a-z0-9_]+)             # YAML file
	\s+                      # Mandatory whitespace
	(\d+)                    # Items per row
	\s+-->                   # End of marker
	.*?                      # HTML
	<!--\s+END\s+-->[\s\n]*  # END marker
""", re.DOTALL + re.VERBOSE + re.IGNORECASE)

# Extract headings
HEADING_PATTERN = re.compile(r"""
	^      # Start of line
	(\#+)  # Depth of header
	\s*    # Ignore any whitespace
	(.+)$  # Match to end of line
""", re.VERBOSE + re.MULTILINE)

# Pattern to identify existing TOC
TOC_PATTERN = re.compile(r"""
	<!--\s+TOC\s+-->      # TOC marker
	(?:\s*-\s+[^\n]+\n)*  # List items
	\n+					  # New lines
""", re.VERBOSE)

# Pattern to identify sidebar links
SIDEBAR_PATTERN = re.compile(r"""
	[\s\n]*<!--\s+SIDEBAR\s+-->  # Marker
	.*?                          # HTML
	<!--\s+END\s+-->[\s\n]*      # END marker
""", re.DOTALL + re.VERBOSE + re.IGNORECASE)

IMAGE_BASE_URL = 'https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders'

# Template compiler
compiler = Compiler()

with open(path.join(path.dirname(__file__), 'templates', 'list.hbs')) as f:
	LIST_TEMPLATE = compiler.compile(f.read().strip())

with open(path.join(path.dirname(__file__), 'templates', 'sample.hbs')) as f:
	SAMPLES_TEMPLATE = compiler.compile(f.read().strip())

with open(path.join(path.dirname(__file__), 'templates', 'sidebar.hbs')) as f:
	SIDEBAR_TEMPLATE = compiler.compile(f.read().strip())

# Load YAML data
DATA_DIR = path.join(path.dirname(__file__), 'data')
YAML_DATA = {}

print("=> Reading YAML")
for fp in listdir(DATA_DIR):
	if path.splitext(fp)[1] == '.yml':
		print("   {}".format(fp))

		with open(path.join(DATA_DIR, fp), 'r') as fh:
			k = path.splitext(path.basename(fp))[0]
			YAML_DATA[k] = yaml.safe_load(fh)


def chunks(j, n):
	for i in range(0, len(j), n):
		yield j[i:i + n]


def list_repl(match):
	k = match.group(1)
	width = match.group(2)
	assert k in YAML_DATA, '{} not in data ({})'.format(k, f)

	contents = LIST_TEMPLATE({
		'image_base': IMAGE_BASE_URL,
		'args': ' '.join(['LIST', k, width]),
		'items': YAML_DATA[k],
		'width': width
	}).strip()
	return '\n\n' + contents + '\n\n'


def arg_sample_repl(match):
	k = match.group(1)
	per_row = int(match.group(2))
	assert k in YAML_DATA, '{} not in data ({})'.format(k, f)

	contents = SAMPLES_TEMPLATE({
		'image_base': IMAGE_BASE_URL,
		'args': ' '.join(['SAMPLE', k, str(per_row)]),
		"has_value_label": any([ 'value' in j or 'label' in j for j in YAML_DATA[k]]),
		"has_text": any([ 'raw' in j or 'text' in j for j in YAML_DATA[k]]),
		'rows': list(chunks(YAML_DATA[k], per_row)),
		'width': re.sub(r'\.?0+%$', '%', "{:.2f}%".format(100 / per_row))
	}).strip()
	return '\n\n' + contents + '\n\n'

def sidebar_repl(match):
	contents = SIDEBAR_TEMPLATE({
		'items': [
			{"label": 'Home', 'href': 'home'},
			{"label": 'Brush Shaders', 'href': 'Brush-Shaders'},
			*[{'label': x['heading'], 'href': x['href'], 'indent': '  '} for x in YAML_DATA['list_brushes']],
			{"label": 'Primitive Brush Shaders', 'href': 'Brush-Shaders'},
			*[{'label': x['heading'], 'href': x['href'], 'indent': '  '} for x in YAML_DATA['list_primitives']],
			{"label": 'Volume Shaders', 'href': 'Volume-Shaders'},
			*[{'label': x['heading'], 'href': x['href'], 'indent': '  '} for x in YAML_DATA['list_volumes']],
			{"label": 'Commands', 'href': 'Commands'},
			{"label": 'Terms', 'href': 'terms'},
			{"label": 'Shaders in MagicaVoxel', 'href': 'Shaders-in-MagicaVoxel'},
		]
	}).strip()
	return '\n\n' + contents + '\n\n'


# Process markdown files
for f in listdir(path.dirname(path.realpath(sys.argv[0]))):
	if path.splitext(f)[1] == '.md':
		with open(f, 'r') as h:
			contents = h.read()

			# Templates
			new_contents = LIST_PATTERN.sub(list_repl, contents)
			new_contents = SAMPLE_PATTERN.sub(arg_sample_repl, new_contents)

			# Sidebar
			new_contents = SIDEBAR_PATTERN.sub(sidebar_repl, new_contents)

			# TOC
			headings = HEADING_PATTERN.findall(contents)
			existing_toc = TOC_PATTERN.findall(contents)
			toc = ['<!-- TOC -->']

			if existing_toc and headings:
				base_depth = min([len(depth) for depth, _ in headings])

				for depth, heading in headings:
					indentation = '  ' * (len(depth) - base_depth)
					anchor = re.sub('\s', '-', re.sub('[^\w\d\s]', '', heading.strip())).lower()

					temp = '{}- [{}](#{})'.format(indentation, heading.strip(), anchor)
					toc.append(temp)

				toc = '\n'.join(toc) + '\n\n'
				new_contents = new_contents.replace(existing_toc[0], toc, 1)

		with open(f, 'w', newline='\n') as h:
			h.write(new_contents.strip() + '\n')
