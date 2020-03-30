import glob
import os

import ffmpeg


def create_video(input_glob, output):
    from cairosvg import svg2png
    
    files = glob.glob(input_glob)

    for f in files:
        svg2png(url=f, write_to='output.png')

    pathlist = [os.path.dirname(__file__), 'util', 'bin', os.name]
    os.environ["PATH"] += os.pathsep + os.path.join(*pathlist)

    (
        ffmpeg
            .input(input_glob, pattern_type='glob', framerate=25)
            .output(output)
            .run()
    )


def generate_html_page(image_files):
    pass

if __name__ == '__main__':
    create_video('out/output*.svg', 'test.mp4')
