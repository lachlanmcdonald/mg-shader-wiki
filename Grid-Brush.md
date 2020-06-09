> The **Grid** [brush](Brush-Shaders) generates a grid pattern with variable thickness and spacing.

- [Parameters](#parameters)
- [Thickness](#thickness)
- [Axis Modes](#axis-modes)
- [Examples](#examples)

## Parameters

- **Color A**: Color of the lines
- **Color B**: Color of the boxes in between the lines
- **Thickness**: Line thickness
- **X Spacing**: Spacing between lines on the X-axis
- **Y Spacing**: Spacing between lines on the Y-axis
- **Z Spacing**: Spacing between lines on the Z-axis

Setting **Color A** to `0` will result in gaps, instead of lines. Similarly, setting **Color B** to `0` will only produce lines (with no boxes in between).

## Thickness

<table>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/grid_thickness_1.png" alt="Example of a thickness of 1"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/grid_thickness_2.png" alt="Example of a thickness of 2"></td>
    </tr>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/grid_thickness_3.png" alt="Example of a thickness of 3"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/grid_thickness_4.png" alt="Example of a thickness of 4"></td>
    </tr>
</table>

## Axis Modes

Axis Modes can be used to only generate a grid on a particular axis. When no Axis Mode is set, a grid is generated on all axes.

<table>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/magica_grid_axis_XYZ.png" alt="Example of no set axis mode"></td>
        <td width="50%"></td>
    </tr>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/magica_grid_axis_X.png" alt="Example of X-axis mode"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/magica_grid_axis_Y.png" alt="Example of Y-axis mode"></td>
    </tr>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/magica_grid_axis_XY.png" alt="Example of X & Y-axis mode"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/magica_grid_axis_Z.png" alt="Example of Z-axis mode"></td>
    </tr>
</table>

## Examples

<table>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/magica_grid_1.png" alt="Example 1"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/magica_grid_2.png" alt="Example 2"></td>
    </tr>
    <tr>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/magica_grid_3.png" alt="Example 3"></td>
        <td width="50%"><img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/239ce726-a6bd-4d08-b68b-21e125a27337/magica_grid_4.png" alt="Example 4"></td>
    </tr>
</table>