> Generates a grid pattern with variable thickness and spacing.

## Parameters

- **Color A**: Color of the lines
- **Color B**: Color of the boxes in between the lines
- **Thickness**: Thickness of the lines
- **X Spacing**: Spacing of lines on the X-axis
- **Y Spacing**: Spacing of lines on the Y-axis
- **Z Spacing**: Spacing of lines on the Z-axis

Setting **Color A** to `0` will result in gaps, instead of lines, and similarly, setting **Color B** to `0` will only produce lines (with no boxes in between).

## Axes Modes

- *Axis Mode* can be used to only generate a grid on a particular axis.
- When no *Axis Mode* is set, a grid is generated on all axes.

<table>
    <tr>
        <td width="50%">
            <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/magica_grid_axis_XYZ.png" alt="Example of no set axis mode">
        </td>
        <td width="50%"></td>
    </tr>
    <tr>
        <td width="50%">
            <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/magica_grid_axis_X.png" alt="Example of X-axis mode">
        </td>
        <td width="50%">
            <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/magica_grid_axis_Y.png" alt="Example of Y-axis mode">
        </td>
    </tr>
    <tr>
        <td width="50%">
            <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/magica_grid_axis_XY.png" alt="Example of X & Y-axis mode">
        </td>
        <td width="50%">
            <img width="100%" src="https://s3.amazonaws.com/misc.lachlanmcdonald.com/magicavoxel-shaders/5efad020-561b-4086-866d-40868862311e/magica_grid_axis_Z.png" alt="Example of Z-axis mode">
        </td>
    </tr>
</table>