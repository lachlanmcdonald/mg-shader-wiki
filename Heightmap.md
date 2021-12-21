> The **heightmap** shader treats the first layer of voxels as a 2D height-map texture and extrudes upwards to create a 3D volume. Height is determined by the _perceived luminance_ of each voxel.

<!-- TOC -->
- [Parameters](#parameters)
- [Mode](#mode)

## Parameters

Parameter | Description
--------- | -----------
**Blur**       | Blurs the height-map by the number of voxels to smooth any noise in the original texture. The default value of `0` does not blurring, and values up to `10` increase the blurring and the smoothness of the result.
**Auto Balance**  | When `1`, the range is remapped according to the selected colours in the palette. When `0`, the range is not changed by the palette. See below for more information.
**Reverse**      | When `0`, the luminance of a voxel determines how far it is extruded. When `1`, this is reversed and darker voxels are extruded.

## Blur

## Auto Balance

The **heightmap** shader uses the _perceived luminance_ of a voxel to determine its height. By default, the maximum luminance is white (`1.0`) and minimum is black (`0.0`).

 The maximum height is determined by the volume size. 

> If your volume is 20x20x40 voxels, A luminance of `1` would equal `40` voxels; `0.5` would equal `20` voxels; etc.

For instance, if you import a height-map texture that ranges from black (`0.0`) to 50% grey (`0.5`), the heightmap shaders can do two things:

- If **Auto Balance** is `1` and you select the colors in the palette used by the height-map texture, the shader will treat the colours relatively and calculate a new maximum and minimum ranges for you.
- If **Auto Balance** is `0`, the shader will treat values absolutely with no changes, meaning the highest point will be 50% of the volume.

If **Auto Balance** is `1` and you haven't selected ever colour used by the height-map texture, those unselected colours are ignored when generating the map. This can lead to odd results.

## Reverse
