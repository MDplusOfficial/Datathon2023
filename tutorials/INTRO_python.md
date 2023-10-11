# Introduction to Python for Medical Students

Never coded in Python before but want to learn how? This tutorial serves as a basic introduction to Python from the ground up, and will get you ready to tackle this year's datathon in no time!

> **Note**: Looking for how to use Python to load and analyze the MIMIC-IV dataset? Check out [this tutorial](../tutorials/MIMIC_python.md) instead.

## What is Python?

[Python](https://www.python.org) is a programming language that is built for easy legibility and for both beginner and advanced programmers. It has become the primary language used to do almost anything related to data science and AI (mostly AI). For this reason, Python is an incredibly popular language and a good skill to have to do anything from data anlysis to building your own machine learning models.

There are two primary versions of Python: Python 2 and Python 3. Python 2 is outdated and no longer used, but you may stumble across some legacy resources online that use it. Therefore, always make sure to check that any reference material or code is written for Python 3.

Most modern computers already have Python installed. To confirm that it's installed, open up a Terminal window (or equivalent shell application) and type the following:

```bash
python --version
```

If you see an output that looks like `Python 3.x.x`, then you're good to go! Otherwise, you can follow the installation instructions [here](https://wiki.python.org/moin/BeginnersGuide/Download).

# Importing Modules

As we'll soon discover, `modules` (sometimes called "packages") are an important component of programming in Python. For this tutorial, there's only one module that we need to download: `numpy` (again, we will talk about what this is in the tutorial to come). For now, we can install `numpy` using `pip`, which is a package management tool for Python:

```python
pip install numpy
```

Now, to run the tutorial, run the following code in your Terminal:

```python
python code/python_/intro.py 
```

The output from this code won't make any sense unless you read the comments in the file along with the output. Therefore, we recommend you read very closely through the comments of the code and reference the printed output as appropriate to best understand the material. The source code to read can be found [here](../code/python_/intro.py).

## Additional Questions?

Feel free to reach out to [Michael Yao](mailto:michael.yao@pennmedicine.upenn.edu) with any questions or concerns!

