#!/usr/bin/env python

import os
import sys
import subprocess

"""
This script compiles the versions of the curiculum vitae and stores a copy in
the outer most directory, which will be used for distribution.

It is assumed that the file
"""

PRETEXT = "hawkins"

def build(version):
    # Set the no extension path.
    no_ext = ''.join([version, '/', version])

    # Compile the document into a PDF.
    subprocess.call(["pdflatex", "-output-directory=" + version, no_ext + \
        ".tex"])

    # Make a copy for distribution.
    subprocess.call(["cp", no_ext + ".pdf", PRETEXT + '-' + \
        version + ".pdf"])

def create(name):
    text = """\\documentclass[10pt]{article}

\\usepackage[margin=0.5in]{geometry}
\\usepackage{enumitem}
\\usepackage{titling}
\\usepackage[T1]{fontenc}
\\usepackage{color}
\\usepackage{hyperref}

\\title{}
\\date{}
\\author{}

\\begin{document}

\\maketitle



\\end{document}
"""

    # Make the directory.
    subprocess.call(["mkdir", name])

    # Create the initial LaTeX file.
    with open(name + '/' + name + ".tex", 'w') as f:
        f.write(text)

if __name__ == "__main__":
    # Get the option, if given.
    try:
        opt = sys.argv[1]
    except IndexError:
        opt = ""

    # Get all versions in the directory.
    all_versions = []
    for (_, dirs, _) in os.walk('.'):
        all_versions.extend(dirs)
        break
    all_versions.remove(".git")

    # Check for the option given.
    if opt.lower() in ["build", 'c']:
        # Get which version to compile, if given.
        try:
            which = sys.argv[2]
        except IndexError:
            which = ''

        # Compile the given version.
        if which == "all":
            for version in all_versions:
                build(version)
        elif which in all_versions:
            build(which)
        else:
            print("The version given (" + which + ") is not found.")
    elif opt.lower() in ["new", 'n']:
        # Get the name of the version t create.
        try:
            name = sys.argv[2]
        except IndexError:
            name = ''

        # Create the version, if it does not already exist.
        if name not in all_versions:
            create(name)
        else:
            print("The name given (" + name + ") already exists.")
    elif opt == '':
        print("Please eneter an option; either 'compile' or 'new'.")
    else:
        print("The option " + opt + " is not valid.")
