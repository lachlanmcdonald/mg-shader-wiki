<!-- TOC -->
- [Writing shaders](#writing-shaders)
- [Observations](#observations)
  - [Voxel coordinates](#voxel-coordinates)
  - [`voxel` always refers to original model](#voxel-always-refers-to-original-model)
  - [Functions must be declared before they are used](#functions-must-be-declared-before-they-are-used)
  - [Using the `voxel` function beyond the volume size](#using-the-voxel-function-beyond-the-volume-size)
- [Snippets](#snippets)
  - [Determine if a axis mode is set](#determine-if-a-axis-mode-is-set)
  - [Determine which axis mode is set](#determine-which-axis-mode-is-set)
- [Editing](#editing)

## Writing shaders

Shader files are written in _OpenGL Shader Language_ (GLSL). [The Book of Shaders](https://thebookofshaders.com/) is a good beginners guide to the shader language.

The `map` function in the shader is executed once per voxel:

- It recieves the location of the voxel as its only argument
- Should return a float between `0` and `255` representing the voxel color in the palette.

For example, the following shader will fill the entire volume with voxels colored from palette index `1`.

```glsl
// xs_begin
// author : '@lachlanmcdonald'
// xs_end

float map(vec3 v) {
	return 1.0;
}
```
- Shaders must start with the header (`xs_begin` and `xs_end`), even if there are no arguments.
- `author` is optional. Whilst there is no standard for it value, a URL or Twitter handle is implied.
- As shaders return a `float`, the value is rounded. For instance, `0.4999` will result in a voxel palette of `1.0`.
- Values are clamped between `0` and `255`, so it is safe to return a value of this range

## Observations

### Voxel coordinates

The `map` function is passed the center-point of the voxel. So, a voxel as position `0`, `0`, `0` will be passed to the `map` function as `vec3(0.5, 0.5, 0.5)`.

If this is undesirable, you can floor the entire `vec3` in one operation:

```glsl
v = floor(v);
```

Which is a more concise way to write:

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

### Using the `voxel` function beyond the volume size

`voxel()` for retrieving a color index will return `0.0` when addressing beyond the volume size. Therefore, it is not necessary to check wether the `x`, `y` or `z` co-ordinates will be out-of-bounds before calling `voxel`.

**For example:**

```glsl
vector(500.0, 500.0, 500.0); // 0.0
vector(-1.0, -1.0, -1.0); // 0.0
```

## Snippets

### Determine if a axis mode is set

`no_axis_mode` will be `true` when no axis modes are set, `false` otherwise.

```glsl
bool no_axis_mode = all(equal(i_axis, vec3(0.0, 0.0, 0.0)));
```

### Determine which axis mode is set

```glsl
bvec3 axis_mode = equal(i_axis, vec3(1.0, 1.0, 1.0));
```

`axis_mode` is a `bvec3` indicating which axis mode is set.

**For example:** `axis_mode.x` will be `true` if the X-axis mode is set.

## Editing

In **Visual Studio Code**, GLSL shader syntax-highlighting can be enabled with the [Shader languages support for VS Code](https://marketplace.visualstudio.com/items?itemName=slevesque.shader) extension.

`.txt` files are not automatically detected as shaders. The following snippet can be added to the workspace settings to override the associations for `.txt` files:

```json
{
	"files.associations": {
		"**/shader/**/*.txt": "glsl"
	}
}
```
