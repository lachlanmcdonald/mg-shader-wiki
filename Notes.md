## Observations

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
