# Resume
My resume is contained here. I have also included a helper script that will manage versions of resumes.

## My Versions
### Short (Resume)
A shortened version of my CV with only the most essential information.

### Long (CV)
Most of my academic and professional information compiled together.

## Helper Script
A Python script to help manage resume versions.

### Dependencies

* `python3`
* `pdflatex`

### Usage
There are three arguments that can be used.

1.  `build`: Build the LaTeX into a PDF and copy the output into the project's root directory.
2.  `create`: Create a new version and populate a directory with a template file.
3.  `clean`: Remove all files from a version except the LaTeX file.

### Flags
*   `--template-path` Set the path to use a template file when creating a new project. Setting to `''` will create an empty file. Can also be set with environment variable `RESUME_TEMPLATE_PATH`.
*   `--no-copy` Do not copy the built PDF file to the project's root.
*   `--preprend` Set the value to be prepended to the name of the version when copying to the projects root. Can also be set with environment variable `RESUME_PREPEND`.

#### Examples
*   `./resume --prepend andrew build short` will build the resume short version and copy the build to the project's root as `andrew-short.pdf`.
*   `./resume -n build long` will build the resume long version and will not copy the build to the project's root.
*   `./resume create 2019-12-20` will create a new version called `2019-12-20` and will build the directory and populate the LaTeX file.
