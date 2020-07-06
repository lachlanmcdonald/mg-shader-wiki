from os import path, listdir
from pybars import Compiler
from time import time
import json
import re

# LIST template marker pattern
LIST_PATTERN = re.compile(r"""
	\s*<!--\s+LIST\s+   # LIST marker
	([a-z_]+)           # JSON file
	\s+                 # Mandatory whitespace
	(\d+)               # Width of image preview
	\s+-->              # End of LIST marker
	.*?                 # HTML
	<!--\s+END\s+-->\s* # END marker
""", re.DOTALL + re.VERBOSE + re.IGNORECASE)

# LIST template
compiler = Compiler()

LIST_TEMPLATE = compiler.compile(u"""
<!-- {{args}} -->
<table>
	<tbody>
		{{#each items}}
		<tr>
			<td valign="top" align="left"><a href="{{{href}}}"><img width="{{{@root.width}}}" src="{{{preview}}}?cache={{@root.cache}}" alt=""></a></td>
			<th valign="top" align="left"><a href="{{{href}}}">{{heading}}</a></th>
			<td valign="top">{{content}}</td>
		</tr>
		{{/each}}
	</tbody>
</table>
<!-- END -->
""")

# Load JSON data
JSON_DATA = {}
for fp in listdir(path.dirname(__file__)):
	if path.splitext(fp)[1] == '.json' and fp.startswith('_'):
		with open(fp, 'r') as fh:
			k = path.splitext(fp)[0][1:]
			JSON_DATA[k] = json.load(fh)

def repl(match):
	k = match.group(1)
	width = match.group(2)
	assert k in JSON_DATA, '{} not in data ({})'.format(k, f)

	contents = LIST_TEMPLATE({
		'cache': int(time()),
		'args': ' '.join(['LIST', k, width]),
		'items': JSON_DATA[k],
		'width': width
	})

	return '\n' + contents + '\n'

# Process markdown files
for f in listdir(path.dirname(__file__)):
	if path.splitext(f)[1] == '.md' and f.startswith('_') is False:
		with open(f, 'r') as h:
			contents = h.read()
			new_contents = LIST_PATTERN.sub(repl, contents)

		if contents != new_contents:
			with open(f, 'w') as h:
				h.write(new_contents)
