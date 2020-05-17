# twemoji-colr

Project to create a COLR/CPAL-based color OpenType font
from the [Twemoji](https://twitter.github.io/twemoji/) collection of emoji images.

Note that the resulting font will **only** be useful on systems that support
layered color TrueType fonts; this includes Windows 8.1 and later,
as well as Mozilla Firefox and other Gecko-based applications running on
any platform.

Systems that do not support such color fonts will show blank glyphs
if they try to use this font.

## Getting started

This project makes use of [grunt-webfont](https://github.com/sapegin/grunt-webfont)
and an additional [node.js](https://nodejs.org/en/) script.
Therefore, installation of Node.js (and its package manager [npm](https://www.npmjs.com/)) is a prerequisite.
Grunt will be installed as a package dependency — no need to install it globally.

The necessary tools can be installed via npm:

    # install dependencies from packages.json, including `grunt-webfont`.
    npm install

The build process also requires [fontforge](https://fontforge.github.io/)
and the TTX script from the [font-tools](https://github.com/behdad/fonttools/) package to be installed, and assumes standard Perl and Python are available.

Both FontForge and font-tools can be installed via `homebrew` on OS X, or package managers on Linux:

    # OS X
    brew install fonttools fontforge

    # Ubuntu, for example
    sudo apt-get install fonttools fontforge python-fontforge
	
UPDATE:
For generation of the outlines more tools are needed:
- rsvg-convert
- convert (aka Imagemagick)
- mkbitmap (part of Potrace)
- potrace

## Building the font

Once the necessary build tools are all in place, simply running

    make

should build the color-emoji font `build/Twemoji Evengard.ttf` from the source SVG files found in `twe-svg.zip` file and `extras`, `overrides` directories.
