from os import path, listdir
from typing import Mapping
import yaml

MAPPING = [
  ["brick", "brick_grout.yml"],
  ["brick", "brick_mode.yml"],
  ["brick", "brick_noise.yml"],
  ["brick", "brick_threshold.yml"],
  ["case", "case_axis.yml"],
  ["case", "case_examples.yml"],
  ["cellular2D", "cellular2D_jitter.yml"],
  ["cellular2D", "cellular2D_mode.yml"],
  ["cellular2D", "cellular2D_noise.yml"],
  ["cellular2D", "cellular2D_power.yml"],
  ["cellular2D", "cellular2D_scale.yml"],
  ["cellular2D", "cellular2D_steps.yml"],
  ["cellular3D", "cellular3D_cavity.yml"],
  ["cellular3D", "cellular3D_jitter.yml"],
  ["cellular3D", "cellular3D_mode.yml"],
  ["cellular3D", "cellular3D_noise.yml"],
  ["cellular3D", "cellular3D_power.yml"],
  ["cellular3D", "cellular3D_scale.yml"],
  ["cover", "cover_examples.yml"],
  ["cover", "cover_variations.yml"],
  ["cylinder", "cylinder_examples.yml"],
  ["cylinder", "cylinder_rotation.yml"],
  ["cylinder", "cylinder_thickness.yml"],
  ["cylinder", "cylinder_volumes.yml"],
  ["diagonal", "diagonal_directions.yml"],
  ["diagonal", "diagonal_examples.yml"],
  ["flood", "flood_examples.yml"],
  ["flood", "flood_shaders.yml"],
  ["gradient", "gradient_direction.yml"],
  ["gradient", "gradient_mode.yml"],
  ["gradient", "gradient_noise.yml"],
  ["grass", "grass_density.yml"],
  ["grass", "grass_examples.yml"],
  ["grass", "grass_growth.yml"],
  ["grass", "grass_modes.yml"],
  ["greebles1", "greebles1_axis.yml"],
  ["greebles1", "greebles1_count.yml"],
  ["greebles1", "greebles1_examples.yml"],
  ["greebles1", "greebles1_modes.yml"],
  ["greebles1", "greebles1_variations.yml"],
  ["greebles2", "greebles2_axis.yml"],
  ["greebles2", "greebles2_modes.yml"],
  ["greebles2", "greebles2_variations.yml"],
  ["grid", "grid_axis.yml"],
  ["grid", "grid_examples.yml"],
  ["grid", "grid_thickness.yml"],
  ["heightmap", "heightmap_autobalance.yml"],
  ["heightmap", "heightmap_blur.yml"],
  ["heightmap", "heightmap_reverse.yml"],
  ["heightmap", "heightmap_usage.yml"],
  ["noise", "noise_axis.yml"],
  ["noise", "noise_sizes.yml"],
  ["outline", "outline_examples.yml"],
  ["prism", "prism_examples.yml"],
  ["prism", "prism_mode0_sizes.yml"],
  ["prism", "prism_mode1_sizes.yml"],
  ["prism", "prism_modes.yml"],
  ["pyramid", "pyramid_axis.yml"],
  ["pyramid", "pyramid_noise.yml"],
  ["sand", "sand_examples.yml"],
  ["sand", "sand_modes.yml"],
  ["soil", "soil_headroom.yml"],
  ["stairs", "stairs_directions.yml"],
  ["stairs", "stairs_height.yml"],
  ["stairs_runs", "stairs_runs_count.yml"],
  ["stairs_runs", "stairs_runs_height.yml"],
  ["stairs_runs", "stairs_runs_xy_gap.yml"],
  ["stairs_runs", "stairs_runs_z_gap.yml"],
  ["stairs_stringer", "stairs_stringer_directions.yml"],
  ["stairs_stringer", "stairs_stringer_stringers.yml"],
  ["tiles", "tiles_examples.yml"],
  ["tiles_puzzle", "tiles_puzzle_examples.yml"],
  ["tiles_puzzle", "tiles_puzzle_line_width.yml"],
  ["tiles_puzzle", "tiles_puzzle_mode.yml"],
  ["tiles_puzzle", "tiles_puzzle_noise.yml"],
  ["tiles_puzzle", "tiles_puzzle_variations.yml"],
  ["tiles_uneven", "tiles_uneven_line_width.yml"],
  ["tiles_uneven", "tiles_uneven_modes.yml"],
  ["tiles_uneven", "tiles_uneven_noise.yml"],
  ["tiles_uneven", "tiles_uneven_variations.yml"],
  ["treemap", "treemap_mode.yml"],
  ["truchet", "truchet_mode.yml"],
  ["truchet", "truchet_noise.yml"],
  ["truchet", "truchet_size.yml"],
  ["weave", "weave_line_widths.yml"],
  ["weave", "weave_modes.yml"],
  ["zigzag", "zigzag_range_directions.yml"],
  ["zigzag", "zigzag_range_examples.yml"],
  ["zigzag2", "zigzag2_directions.yml"],
  ["zigzag2", "zigzag2_examples.yml"],
  ["zigzag3", "zigzag3_directions.yml"],
  ["zigzag3", "zigzag3_examples.yml"]
]

# Load YAML data
BASE_DIR = path.dirname(__file__)
DATA_DIR = path.join(BASE_DIR, 'data')
YAML_DATA = {}

print("=> Reading YAML")
for fp in listdir(DATA_DIR):
	if path.splitext(fp)[1] == '.yml':

		with open(path.join(DATA_DIR, fp), 'r') as fh:
			k = path.basename(fp)
			YAML_DATA[k] = yaml.safe_load(fh)

MERGED_DATA = {}

for output_file, yaml_file in MAPPING:
	if yaml_file in MERGED_DATA:
		key = path.splitext(yaml_file)[0].replace(output_file + "_", "")

		if output_file not in MERGED_DATA:
			MERGED_DATA[output_file] = {}

		MERGED_DATA[output_file][key] = YAML_DATA[yaml_file]

for output_file, data in MERGED_DATA.items():
	output_path = path.join(DATA_DIR, "{}.yml".format(output_file))

	with open(output_path, "w+") as fh:
		yaml.safe_dump(data, fh, default_flow_style=False, allow_unicode=True)

MARKDOWN = {}
print("=> Reading Markdown")
for fp in listdir(BASE_DIR):
	if path.splitext(fp)[1] == '.md':
		with open(fp, 'r') as fh:
			MARKDOWN[fp] = fh.read()

REPLACEMENTS = {}
for output_file, yaml_file in MAPPING:
	k = path.splitext(path.basename(yaml_file))[0]
	key = path.splitext(yaml_file)[0].replace(output_file + "_", "")

	a = "SAMPLE {}".format(k)
	b = "SAMPLE {} {}".format(output_file, key)
	REPLACEMENTS[a] = b

for md_file, original_contents in MARKDOWN.items():
	new_contents = original_contents[:-1]

	for a, b in REPLACEMENTS.items():
		new_contents = new_contents.replace(a, b)

	if original_contents != new_contents:
		with open(md_file, 'w+') as fh:
			fh.write("{}\n".format(new_contents.strip()))
