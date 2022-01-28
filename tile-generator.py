#!/usr/bin/env python3
# coding: UTF-8

import argparse
import cv2
import os

IMG_EXTENSION = "png"

def main():
    parser = argparse.ArgumentParser(description='This script generates tile images from a large image.')
    parser.add_argument('img_path', type=str, help='original image path')
    parser.add_argument('-d', '--depth', type=int, default=3, help='depth for zoom')
    parser.add_argument('-o', '--outdir', type=str, default='tiles', help='output directory name')
    args = parser.parse_args()

    # load image
    img = cv2.imread(args.img_path, cv2.IMREAD_UNCHANGED)
    height, width = img.shape[:2]

    for d in range(args.depth):
        save_splitted_image(img, d, args.outdir, height, width)


def save_splitted_image(img, depth, base_outdir, height, width):
    if depth == 0:
        outdir = os.path.join(base_outdir, "0", "0")
        os.makedirs(outdir, exist_ok=True)
        cv2.imwrite(os.path.join(outdir, f"0.{IMG_EXTENSION}"), img)
        return

    n_split = 2 ** depth

    cx=0
    cy=0
    for x in range(n_split):
        outdir = os.path.join(base_outdir, str(depth), str(x))
        os.makedirs(outdir, exist_ok=True)

        for y in range(n_split):
            splitted_img = img[cy:cy+int(height/n_split), cx:cx+int(width/n_split), :]
            cv2.imwrite(os.path.join(outdir, f"{y}.{IMG_EXTENSION}"), splitted_img)
            cy = cy + int(height/n_split)
        cy=0
        cx=cx+int(width/n_split)


if __name__ == '__main__':
    main()
