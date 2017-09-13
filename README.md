Curriculum Vitae
================

This project is really just a way for me to save my curriculum vitae and résumé on GitHub with version control.
The first two components are versions of my professional and academic credentials.
The final component is a generating script to help with the management of the documents.

---

Curriculum Vitae (CV)
---------------------
Most of my academic and professional information compiled together.

Résumé
------
A shortened version of my CV with only minimally necessary information.

---

Generating Script
-----------------
A Python script to compile the LaTeX files and copy a version to be distributed.
Usage is `$ python generate.py build cv` to build the cv version.
Also permitted is the `all` argument to build all versions in the directory.
To create a new version use `$ python generate.py new 'name'`.
This will create a directory with the name given and generate a template LaTeX script.
