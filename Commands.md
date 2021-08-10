> The following page outlines the shader commands for use in MagicaVoxel's console.
> 
> Since the addition of the shader UI, default parameters and error-checking has been removed from the scripts. All arguments are required.

- [gradient](#gradient)
- [cellular2D](#cellular2D)
- [cellular3D](#cellular3D)
- [truchet](#truchet)
- [bricks](#bricks)
- [bricks_vert](#bricks_vert)
- [diagonal](#diagonal)
- [grass](#grass)
- [grid](#grid)
- [stairs](#stairs)
- [stairs_runs](#stairs_runs)
- [stairs_stringer](#stairs_stringer)
- [tiles](#tiles)
- [tiles_puzzle](#tiles_puzzle)
- [tiles_uneven](#tiles_uneven)
- [weave](#weave)
- [zigzag](#zigzag)
- [zigzag2](#zigzag2)
- [zigzag3](#zigzag3)
- [case](#case)
- [cover](#cover)
- [flood](#flood)
- [flood2](#flood2)
- [noise](#noise)
- [outline](#outline)
- [outline2](#outline2)
- [cylinder](#cylinder)
- [greebles1](#greebles1)
- [greebles2](#greebles2)
- [prism](#prism)
- [pyramid](#pyramid)
- [random](#random)
- [sand](#sand)
- [sand2](#sand2)
- [slice_x](#slice_x)
- [slice_y](#slice_y)
- [slice_z](#slice_z)
- [soil](#soil)
- [soil_replace](#soil_replace)
# gradient

```
xs brush/gradient [Mode] [Direction] [Noise] [Seed]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-5
`1` | **Direction** | Integer | 0-5
`2` | **Noise** | Integer | 0-50
`3` | **Seed** | Integer | 1-100

Example:

```
xs brush/gradient 0 0 0 1
```
[Top](#)
# cellular2D

```
xs brush/cellular2D [Mode] [Scale] [Jitter] [Noise] [Power] [Steps] [Seed] [Tile X] [Tile Y]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-5
`1` | **Scale** | Integer | 1-100
`2` | **Jitter** | Integer | -100-100
`3` | **Noise** | Integer | 0-100
`4` | **Power** | Float | 0-10
`5` | **Steps** | Integer | 0-40
`6` | **Seed** | Integer | 1-100
`7` | **Tile X** | Integer | 0-40
`8` | **Tile Y** | Integer | 0-40

Example:

```
xs brush/cellular2D 0 24 100 0 1 0 1 0 0
```
[Top](#)
# cellular3D

```
xs brush/cellular3D [Mode] [Scale] [Jitter] [Noise] [Power] [Cavity] [Seed] [Tile X] [Tile Y] [Tile Z]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-5
`1` | **Scale** | Integer | 1-100
`2` | **Jitter** | Integer | -100-100
`3` | **Noise** | Integer | 0-100
`4` | **Power** | Float | 0-10
`5` | **Cavity** | Integer | 0-100
`6` | **Seed** | Integer | 1-100
`7` | **Tile X** | Integer | 0-40
`8` | **Tile Y** | Integer | 0-40
`9` | **Tile Z** | Integer | 0-40

Example:

```
xs brush/cellular3D 0 24 100 0 1 50 1 0 0 0
```
[Top](#)
# truchet

```
xs brush/truchet [Mode] [Size] [Noise] [Seed]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-2
`1` | **Size** | Integer | 3-40
`2` | **Noise** | Float | 0-100
`3` | **Seed** | Integer | 1-100

Example:

```
xs brush/truchet 0 8 0 1
```
[Top](#)
# bricks

```
xs brush/bricks [Mode] [Direction] [Width] [Height] [Depth] [Grout Size] [Grout Color] [Offset] [Noise] [Threshold]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-2
`1` | **Direction** | Integer | 0-3
`2` | **Width** | Integer | 1-256
`3` | **Height** | Integer | 1-256
`4` | **Depth** | Integer | 1-256
`5` | **Grout Size** | Integer | 0-256
`6` | **Grout Color** | Integer | 0-255
`7` | **Offset** | Integer | 0-256
`8` | **Noise** | Float | 0-100
`9` | **Threshold** | Float | 0-100

Example:

```
xs brush/bricks 0 0 5 2 2 1 1 0 0 100
```
[Top](#)
# bricks_vert

```
xs brush/bricks_vert [Mode] [Direction] [Height] [Depth] [Width] [Grout Size] [Grout Color] [Offset] [Noise] [Threshold]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-2
`1` | **Direction** | Integer | 0-3
`2` | **Height** | Integer | 1-256
`3` | **Depth** | Integer | 1-256
`4` | **Width** | Integer | 1-256
`5` | **Grout Size** | Integer | 0-256
`6` | **Grout Color** | Integer | 0-255
`7` | **Offset** | Integer | 0-256
`8` | **Noise** | Float | 0-100
`9` | **Threshold** | Float | 0-100

Example:

```
xs brush/bricks_vert 0 0 5 2 3 1 1 0 0 100
```
[Top](#)
# diagonal

```
xs brush/diagonal [Direction] [Width A] [Width B] [Width C] [Width D] [Offset] [Shuffle]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Direction** | Integer | 0-5
`1` | **Width A** | Integer | 0-32
`2` | **Width B** | Integer | 0-32
`3` | **Width C** | Integer | 0-32
`4` | **Width D** | Integer | 0-32
`5` | **Offset** | Integer | 0-256
`6` | **Shuffle** | Integer | 0-256

Example:

```
xs brush/diagonal 0 2 0 0 0 0 0
```
[Top](#)
# grass

```
xs brush/grass [Direction] [Mode] [Density] [Growth] [Seed]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Direction** | Integer | 0-1
`1` | **Mode** | Integer | 0-4
`2` | **Density** | Integer | 1-256
`3` | **Growth** | Float | -1-1
`4` | **Seed** | Integer | 1-100

Example:

```
xs brush/grass 0 0 2 0.5 1
```
[Top](#)
# grid

```
xs brush/grid [Color A] [Color B] [Thickness] [Size X] [Size Y] [Size Z]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Color A** | Integer | 0-255
`1` | **Color B** | Integer | 0-255
`2` | **Thickness** | Integer | 1-256
`3` | **Size X** | Integer | 1-256
`4` | **Size Y** | Integer | 1-256
`5` | **Size Z** | Integer | 1-256

Example:

```
xs brush/grid 1 2 1 1 1 1
```
[Top](#)
# stairs

```
xs primitive/stairs [Mode] [Direction] [Count] [Height]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-2
`1` | **Direction** | Integer | 0-3
`2` | **Count** | Integer | 1-256
`3` | **Height** | Integer | 1-256

Example:

```
xs primitive/stairs 0 0 5 1
```
[Top](#)
# stairs_runs

```
xs primitive/stairs_runs [Mode] [Direction] [Count] [Height] [X/Y Gap] [Z Gap]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-3
`1` | **Direction** | Integer | 0-3
`2` | **Count** | Integer | 1-256
`3` | **Height** | Integer | 1-256
`4` | **X/Y Gap** | Integer | 0-256
`5` | **Z Gap** | Integer | 0-256

Example:

```
xs primitive/stairs_runs 0 0 5 1 0 0
```
[Top](#)
# stairs_stringer

```
xs primitive/stairs_stringer [Mode] [Direction] [Count] [Height] [Stringer]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-3
`1` | **Direction** | Integer | 0-3
`2` | **Count** | Integer | 1-256
`3` | **Height** | Integer | 1-256
`4` | **Stringer** | Integer | 0-256

Example:

```
xs primitive/stairs_stringer 0 0 5 1 0
```
[Top](#)
# tiles

```
xs brush/tiles [Width] [Height] [Depth] [Offset X] [Offset Y] [Offset Z]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Width** | Integer | 1-256
`1` | **Height** | Integer | 1-256
`2` | **Depth** | Integer | 1-256
`3` | **Offset X** | Integer | 0-256
`4` | **Offset Y** | Integer | 0-256
`5` | **Offset Z** | Integer | 0-256

Example:

```
xs brush/tiles 2 2 2 0 0 0
```
[Top](#)
# tiles_puzzle

```
xs brush/tiles_puzzle [Mode] [Size X] [Size Y] [Line Color] [Line Width] [Noise] [Seed]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-4
`1` | **Size X** | Integer | 1-256
`2` | **Size Y** | Integer | 1-256
`3` | **Line Color** | Integer | 0-255
`4` | **Line Width** | Integer | 0-256
`5` | **Noise** | Float | 0-100
`6` | **Seed** | Integer | 1-100

Example:

```
xs brush/tiles_puzzle 0 4 4 16 1 0 1
```
[Top](#)
# tiles_uneven

```
xs brush/tiles_uneven [Mode] [Min] [Max] [Line Color] [Line Width] [Noise] [Seed]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-5
`1` | **Min** | Integer | 1-256
`2` | **Max** | Integer | 1-256
`3` | **Line Color** | Integer | 0-255
`4` | **Line Width** | Integer | 0-256
`5` | **Noise** | Float | 0-100
`6` | **Seed** | Integer | 1-100

Example:

```
xs brush/tiles_uneven 0 4 8 16 1 0 1
```
[Top](#)
# weave

```
xs brush/weave [Mode] [Size] [Line Color] [Line Width] [Seed]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-2
`1` | **Size** | Integer | 1-256
`2` | **Line Color** | Integer | 0-255
`3` | **Line Width** | Integer | 0-256
`4` | **Seed** | Integer | 1-100

Example:

```
xs brush/weave 0 4 10 1 1
```
[Top](#)
# zigzag

```
xs brush/zigzag [Direction] [Width]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Direction** | Integer | 0-3
`1` | **Width** | Integer | 1-256

Example:

```
xs brush/zigzag 0 2
```
[Top](#)
# zigzag2

```
xs brush/zigzag2 [Direction] [Width A] [Width B]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Direction** | Integer | 0-3
`1` | **Width A** | Integer | 1-256
`2` | **Width B** | Integer | 1-256

Example:

```
xs brush/zigzag2 0 2 2
```
[Top](#)
# zigzag3

```
xs brush/zigzag3 [Direction] [Width A] [Width B] [Width C]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Direction** | Integer | 0-3
`1` | **Width A** | Integer | 1-256
`2` | **Width B** | Integer | 1-256
`3` | **Width C** | Integer | 1-256

Example:

```
xs brush/zigzag3 0 2 2 2
```
[Top](#)
# case

```
xs case [Color]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Color** | Integer | 0-255

Example:

```
xs case 1
```
[Top](#)
# cover

```
xs cover [Headroom] [Noise] [Seed]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Headroom** | Integer | 1-256
`1` | **Noise** | Float | 0-100
`2` | **Seed** | Integer | 1-100

Example:

```
xs cover 1 0 1
```
[Top](#)
# flood

```
xs flood [Height]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Height** | Integer | 1-256

Example:

```
xs flood 1
```
[Top](#)
# flood2

```
xs flood2 [Height]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Height** | Integer | 1-256

Example:

```
xs flood2 1
```
[Top](#)
# noise

```
xs noise [Target Color] [Size X] [Size Y] [Size Z] [Seed]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Target Color** | Integer | 0-255
`1` | **Size X** | Integer | 1-256
`2` | **Size Y** | Integer | 1-256
`3` | **Size Z** | Integer | 1-256
`4` | **Seed** | Integer | 1-100

Example:

```
xs noise 1 1 1 1 1
```
[Top](#)
# outline

```
xs outline [Color]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Color** | Integer | 0-255

Example:

```
xs outline 1
```
[Top](#)
# outline2

```
xs outline2 [Color]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Color** | Integer | 0-255

Example:

```
xs outline2 1
```
[Top](#)
# cylinder

```
xs primitive/cylinder [Rotation] [Thickness]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Rotation** | Integer | 0-2
`1` | **Thickness** | Integer | 0-100

Example:

```
xs primitive/cylinder 0 50
```
[Top](#)
# greebles1

```
xs primitive/greebles1 [Mode] [Count] [Width] [Height] [Depth] [Seed]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-1
`1` | **Count** | Integer | 1-256
`2` | **Width** | Integer | 1-256
`3` | **Height** | Integer | 1-256
`4` | **Depth** | Integer | 1-256
`5` | **Seed** | Integer | 1-100

Example:

```
xs primitive/greebles1 0 32 4 4 4 1
```
[Top](#)
# greebles2

```
xs primitive/greebles2 [Mode] [Min] [Max] [Depth] [Seed]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-2
`1` | **Min** | Integer | 1-256
`2` | **Max** | Integer | 1-256
`3` | **Depth** | Integer | 1-256
`4` | **Seed** | Integer | 1-100

Example:

```
xs primitive/greebles2 0 4 8 2 1
```
[Top](#)
# prism

```
xs primitive/prism [Mode] [Size X] [Size Y]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-1
`1` | **Size X** | Integer | 0-256
`2` | **Size Y** | Integer | 0-256

Example:

```
xs primitive/prism 0 12 12
```
[Top](#)
# pyramid

```
xs pyramid [Noise] [Seed]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Noise** | Float | 0-100
`1` | **Seed** | Integer | 1-100

Example:

```
xs pyramid 0 1
```
[Top](#)
# random

```
xs random [Threshold] [Color]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Threshold** | Float | 0-100
`1` | **Color** | Integer | 0-255

Example:

```
xs random 50 1
```
[Top](#)
# sand

```
xs sand [Mode] [Threshold]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-2
`1` | **Threshold** | Float | 0-100

Example:

```
xs sand 0 0
```
[Top](#)
# sand2

```
xs sand2 [Mode] [Threshold]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Mode** | Integer | 0-2
`1` | **Threshold** | Float | 0-100

Example:

```
xs sand2 0 0
```
[Top](#)
# slice_x

```
xs slice_x [Offset] [Count]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Offset** | Integer | 0-256
`1` | **Count** | Integer | 0-256

Example:

```
xs slice_x 0 0
```
[Top](#)
# slice_y

```
xs slice_y [Offset] [Count]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Offset** | Integer | 0-256
`1` | **Count** | Integer | 0-256

Example:

```
xs slice_y 0 0
```
[Top](#)
# slice_z

```
xs slice_z [Offset] [Count]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Offset** | Integer | 0-256
`1` | **Count** | Integer | 0-256

Example:

```
xs slice_z 0 0
```
[Top](#)
# soil

```
xs soil [Color] [Headroom]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Color** | Integer | 0-255
`1` | **Headroom** | Integer | 1-256

Example:

```
xs soil 1 1
```
[Top](#)
# soil_replace

```
xs soil_replace [Color] [Headroom]
```

ID | Argument | Type | Range
-- | -------- | ---- | -----
`0` | **Color** | Integer | 0-255
`1` | **Headroom** | Integer | 1-256

Example:

```
xs soil_replace 1 1
```
[Top](#)

<sub>This page was last generated: 2021-08-10 21:53:47.856398</sub>
