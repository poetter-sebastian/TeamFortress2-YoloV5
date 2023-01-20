import argparse
import glob, os
import sys
from pathlib import Path

import detect

if __name__ == "__main__":
    opt = detect.parse_opt()
    os.chdir("./OGE")
    for file in glob.glob("*.pt"):
        test = file
        opt.imgsz = [1080, 1920]
        opt.line_thickness = 1
        opt.conf_thres= 0.6
        opt.name = file
        opt.weights = test
        opt.source=detect.ROOT / "img"
        detect.check_requirements(exclude=('tensorboard', 'thop'))
        detect.run(**vars(opt));
        
