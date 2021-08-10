<!-- TOC -->
- [Writing shaders](#writing-shaders)
- [Observations](#observations)
  - [Overloading existing functions](#overloading-existing-functions)
  - [Type casting](#type-casting)
  - [Voxel coordinates](#voxel-coordinates)
  - [`voxel` always refers to original model](#voxel-always-refers-to-original-model)
  - [Functions must be declared before they are used](#functions-must-be-declared-before-they-are-used)
  - [Limit on array size](#limit-on-array-size)
  - [Using the `voxel` function beyond the volume size](#using-the-voxel-function-beyond-the-volume-size)
- [Snippets](#snippets)
  - [Determine if a axis mode is set](#determine-if-a-axis-mode-is-set)
  - [Determine which axis mode is set](#determine-which-axis-mode-is-set)
  - [`mix()` for selected colours](#mix-for-selected-colours)
  - [Determine if the provided color is one of the selected colors](#determine-if-the-provided-color-is-one-of-the-selected-colors)
- [Editing](#editing)
  - [Testing shaders in MagicaVoxel](#testing-shaders-in-magicavoxel)
  - [Visual Studio Code](#visual-studio-code)

## Writing shaders

Shader files are written in _OpenGL Shader Language_ (GLSL), version _1.10_. [The Book of Shaders](https://thebookofshaders.com/) is a good beginners guide to the shader language.

Each shader has a `map` function which is executed once per voxel:

- It recieves the location of the voxel as its only argument
- Should return a float between `0.0` and `255.0` representing the voxel color in the palette.

For example, the following shader will fill the entire volume with voxels colored from palette index `1`.

```glsl
// xs_begin
// author : '@lachlanmcdonald'
// xs_end

float map(vec3 v) {
	return 1.0;
}
```
- Shaders must contain the header (`xs_begin` and `xs_end`), even if there are no arguments.
- `author` is optional. Whilst there is no standard for it value, a URL or Twitter handle is customary.
- As shaders return a `float`, the value is rounded-up. For instance, `0.4999` will result in a voxel palette of `1.0`.
- Return values are clamped between `0.0` and `255.0`, so it is safe to return a value outside of this range.

## Observations

### Overloading existing functions

Some hardware will not allow the extension of exiting functions with a different signature. For maximum portability, a function's name should never match an existing function.

For instance, the following code (which attempts to create a new version of `mod` to work with only `int`s) will not work on all systems:

```glsl
int mod(int a, int b) {
	return int(mod(float(a), float(b)));
}
```

Instead, it should be given a different name:

```glsl
int imod(int a, int b) {
	return int(mod(float(a), float(b)));
}
```

### Type casting

Some hardware cannot coercion betwen `int` and `float`, and instead require an explicit command. You should always explicity cast from `int` to `float` and vice versa.

i.e.

```glsl
float a = 1.0;
int b = int(a * 2.0); // will work on all hardware
int b = a * 2.0;      // will not work on all hardware

float c = 2 * 6;        // will not work on all hardware
float c = float(2 * 6); // will work on all hardware
```

Similarly, a function must always return the expected _return type_ (the value is not coerced):

```glsl
float a() {
	return float(1); // will work
	return 1;        // will not work
}
```

### Voxel coordinates

The `map` function is passed the center-point of the voxel. So, a voxel as position `0`, `0`, `0` will be passed to the `map` function as `vec3(0.5, 0.5, 0.5)`.

If this is undesirable, you can floor the entire `vec3` in one operation:

```glsl
vec3 v = floor(v);
```

Which is the same as below but more concise:

```glsl
v.x = floor(v.x);
v.y = floor(v.y);
v.z = floor(v.z);
```

### `voxel` always refers to original model

`voxel()` always refers to the original model. For example:

```glsl
float map(vec3 v) {
	if (all(equal(v, vec3(0.0, 0.0, 0.0)))) {
		return 1.0;
	} else {
		return voxel(vec3(0.0, 0.0, 0.0));
	}
}
```

Will not result in the entire model being replaced with index `0`. Instead, all voxels will be replaced with the original index at position `0,0,0`.

### Functions must be declared before they are used

For example, `b()` must be defined before `a()`, or it will not be defined when `a()` tries to call it.

```glsl
float b() {
	return 1.0;
}

float a() {
	return b();
}

float map(vec3 v) {
	return a();
}
```

### Limit on array size

There are platform-dependant limits on the size of arrays. When an array size exceeds this limit, MagicaVoxel will not display an error but no voxels will be added by the shader. However, in some circumstances random voxels will appear.

It is best not to initaialise arrays with more than 255 elements. 

### Using the `voxel` function beyond the volume size

`voxel()` for retrieving a color index will return `0.0` when addressing beyond the volume size. Therefore, it is not necessary to check wether the `x`, `y` or `z` co-ordinates will be out-of-bounds before calling `voxel`.

```glsl
voxel(500.0, 500.0, 500.0); // 0.0
voxel(-1.0, -1.0, -1.0); // 0.0
```

## Snippets

### Determine if a axis mode is set

`no_axis_mode` will be `true` when no axis modes are set, `false` otherwise.

```glsl
bool no_axis_mode = all(equal(ivec3(i_axis), ivec3(0)));
```

### Determine which axis mode is set

```glsl
bvec3 axis_mode = equal(ivec3(i_axis), ivec3(1));
```

`axis_mode` is a `bvec3` indicating which axis mode is set.

**For example:** `axis_mode.x` will be `true` if the X-axis mode is set.

### `mix()` for selected colours

```glsl
float pal_mix(float p) {
	float f = floor(mix(0.0, float(i_num_color_sels), p));
	return color_sel(f);
}
```

### Determine if the provided color is one of the selected colors

```glsl
bool is_sel_color(float p) {
	for (int i = 0; i < i_num_color_sels; i += 1) {
		if (p == color_sel(float(i))) {
			return true;
		}
	}
	return false;
}
```

## Editing

### Testing shaders in MagicaVoxel

By default, shaders are loaded from MagicaVoxel's `shader` director. However, you can set a new path by changing the `dir_xs_shader` parameter within `config/config.txt` and specifying the new path:

i.e.

```
dir_xs_shader		: "/Users/lachlan/magicavoxel-shaders/shader"
```

### Visual Studio Code

In **Visual Studio Code**, GLSL shader syntax-highlighting can be enabled with the [Shader languages support for VS Code](https://marketplace.visualstudio.com/items?itemName=slevesque.shader) extension.

`.txt` files are not automatically detected as shaders. The following snippet can be added to the workspace settings to override the associations for `.txt` files:

```json
{
	"files.associations": {
		"**/shader/**/*.txt": "glsl"
	}
}
```
