#!/usr/bin/env python

import argparse
import os
import sys
import subprocess


def build(name: str) -> None:
    # Compile the document into a PDF.
    subprocess.call([
        "pdflatex",
        f"-output-directory={name}",
        os.path.join(name, f"{name}.tex"),
    ])


def copy(name: str, prepend: str) -> None:
    # Make a copy for distribution.
    subprocess.call([
        "cp",
        os.path.join(name, f"{name}.pdf"),
        f"{prepend}{'-' if prepend else ''}{name}.pdf",
    ])


def create(name: str, template_path: str) -> None:
    # Make the directory.
    subprocess.call(["mkdir", name])

    # Set the new path for the LaTeX file.
    new_path = os.path.join(name, f"{name}.tex")

    # Create the initial LaTeX file.
    if template_path:
        subprocess.call(["cp", template_path, new_path])
    else:
        subprocess.call(["touch", new_path])


def clean(name: str) -> None:
    # Delete eveything except the LaTeX file.
    subprocess.call(["find", name, '!', "-name", f"{name}.tex", "-type", 'f',
                     "-exec", "rm", "-f", "{}", '+'])


if __name__ == "__main__":
    # Create the parser.
    parser = argparse.ArgumentParser(description="Manage resume versions.")
    parser.add_argument(
        "action",
        type=str,
        choices=["build", "create", "clean"],
        help="Action to take. 'build' will generate a PDF. "
             "'create' will initialize a new version. 'clean' will remove all "
             "but the LaTeX file",
    )
    parser.add_argument(
        "name",
        nargs='+',
        type=str,
        help="Name of the version.",
    )
    parser.add_argument(
        "--template-path",
        "-b",
        default=os.getenv("RESUME_TEMPLATE_PATH", "./templates/base.tex"),
        type=str,
        help="Path to a base LaTeX template.",
    )
    parser.add_argument(
        "--no-copy",
        "-n",
        action="store_true",
        help="Do not copy the build."
    )
    parser.add_argument(
        "--prepend",
        "-p",
        default=os.getenv("RESUME_PREPEND", ''),
        type=str,
        help="Word to prepend to filename when copying build.",
    )
    args = parser.parse_args()

    # Get all currently defined versions.
    versions = [dir for dir in next(os.walk('.'))[1] if f"{dir}.tex" in
                next(os.walk(f"./{dir}"))[2]]

    # Handle the action accordingly.
    if args.action == "build":
        # Build each version.
        for name in args.name:
            if name not in versions:
                print(f"Warning: name '{name}' not found, skipping")
                continue

            # Build the resume version.
            build(name)

            # Perform copy to base project path.
            if not args.no_copy:
                copy(name, args.prepend.strip())
    elif args.action == "create":
        # Check if the template exists.
        if not os.path.exists(args.template_path):
            print("Warning: no template found, using a blank document")
            args.template_path = ''

        # Create each version.
        for name in args.name:
            # Verify all given names are valid.
            if name in versions:
                print(f"Warning: name '{name}' already created, skipping")
                continue

            # Create the resume version.
            create(name, args.template_path)
    elif args.action == "clean":
        # Clean each version.
        for name in args.name:
            if name not in versions:
                print(f"Warning: name '{name}' not found, skipping")
                continue

            # Clean the resume version.
            clean(name)
    else:
        sys.exit(f"action '{args.action}' not available")
