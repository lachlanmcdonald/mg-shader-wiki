> **random** replaces voxels which match your selected color, at random, with a chosen color

- [Parameters](#parameters)
- [Threshold](#threshold)
- [Axis modes](#axis-modes)

## Parameters

- **Threshold**: Threshold of noise, lower values produce replace less voxels and higher values replace more voxels
- **Color**: Color index to replace voxels (setting the index to `0` will remove voxels)

## Threshold

<table>
    <tr>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/rand_025.png" alt="">Threshold: <code>0.25</code></td>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/rand_050.png" alt="">Threshold: <code>0.5</code></td>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/rand_075.png" alt="">Threshold: <code>0.75</code></td>
    </tr>
</table>

## Axis modes

Voxels are replaced across all axes. You can randomize the X, Y, or Z-axis (or a combination) with the axis mode.

<table>
    <tr>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/rand_050_y.png" alt="">Y-axis</td>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/rand_050_xy.png" alt="">X &amp; Y axes</td>
        <td width="33%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/caf97416-2a0d-4bde-a839-8f3f2d50e5a5/rand_050_xz.png" alt="">X &amp; Z axes</td>
    </tr>
</table>