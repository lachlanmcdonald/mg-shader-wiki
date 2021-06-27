> This page explains a few commonly used terms through-out this documentation.

<!-- TOC -->
- [Axis Modes](#axis-modes)
- [Seeds](#seeds)

## Axis Modes

**Axis Modes** are part of the MagicaVoxel UI and restricts editing to only certain axes (X, Y, and Z). Some shaders respond differently when an **Axis Mode** is selected.

**Axis Modes** are toggled with these buttons in the **Brush** panel:

<img src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/0.11.0/axis_modes.png" width="150px">

## Seeds

Most shaders need to generate pseudo-random numbers to create noise or variation when they run. However, the language (GLSL) that is used for writing shaders does not have the ability to generate pseudo-random numbers, so each time the shader is run, it will generate the same randomness.

Shaders with a **Seed** argument allows you to give the shader a new starting number, allowing you to generate different randomness each time.

THis is often not necessary for small scenes. However, if you are generating the same pattern over multiple objects, it can be used to make sure every object does not look the same.
