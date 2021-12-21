> The **terrain** [brush](Brush-Shaders) generates a terrain topography by combining different types of noise and [fBm](https://en.wikipedia.org/wiki/Fractional_Brownian_motion). 

<!-- TOC -->
- [Parameters](#parameters)
- [Mode](#mode)

## Parameters

Parameter | Description
--------- | -----------
**Mode**       | Colour mode (see below)
**Direction**  | Direction
**Scale**      | Scale of the terrain
**Iterations** | Number of iterations, lower values produce less terrain features and high values more features. This can be roughly thought of as increasing the height-map resolution.
**Octaves**    | Number of octives when for generating displacements of the terrain (small features). Higher values produce more features (but more noise) and lower values produce less features (and smoother terrain). This can be roughly thought of as 
**Contrast**   | Adjusts the contrast of the height-map. The default value of `50` represents the mid-point, valueas towards `100` increase the depth of high and low values. Where as values towards `0` produces smoother terrain. For low number of *Iterations* or *Octaves*, it might be necessary to increase the contrast.
**Shift**      | Shift the mid-point of the height-map. The default value of `50` represents the normal mid-point.
**Gain**       | Influence of each iteration. Effectively this multiplies each iteration.Smaller values produce smoother terrain, and higher values produce more turbulance and noise.
**Lacunarity** | Lacunarity
**Noise**      | Additional colour node (depending on the *Mode*)
**Tile X** | Tile offet on the X-axis
**Tile Y** | Tile offet on the Y-axis

**Tile X** and **Tile Y** parameters are used to generate noise over multiple adjacent volumes. For instance, to create a terrain that exceeds the 256<sup>2</sup> size limit.
