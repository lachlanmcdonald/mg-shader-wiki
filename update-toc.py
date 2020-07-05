from os import path, listdir
import re

HEADING_PATTERN = re.compile(r"""
	^      # Start of line
	(\#+)  # Depth of header
	\s*    # Ignore any whitespace
	(.+)$  # Match to end of line
""", re.VERBOSE + re.MULTILINE)

TOC_PATTERN = re.compile(r"""
	<!--\s+TOC\s+-->      # TOC marker
	(?:\s*-\s+[^\n]+\n)*  # List items
	\n+					  # New lines
""", re.VERBOSE)

for f in listdir(path.dirname(__file__)):
	if path.splitext(f)[1] == '.md' and f.startswith('_') is False:
		with open(f, 'r') as h:
			contents = h.read()
			new_contents = contents

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
				new_contents = contents.replace(existing_toc[0], toc, 1)

		if contents != new_contents:
			with open(f, 'w') as h:
				h.write(new_contents)
