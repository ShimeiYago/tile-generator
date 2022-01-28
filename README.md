# Tile Generator

This generates tile images from a large image.

## Requirement

- python 3.10.0 or more

## Usage

`./tile-generator.py {img_path} -d {DEPTH} -o {OUTDIR}`

- (Required) img_path: Path of original large image.
- (Optional) DEPTH: Depth for zoom. Default is `3`.
- (Optional) OUTDIR: Output directory path. Default is `./tiles`.

## Tile image path
You can access generated tile image with `OUTDIR/{z}/{x}/{y}.png`

## Author
[ShimeiYago](https://github.com/ShimeiYago)
