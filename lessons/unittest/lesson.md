---
layout: page
title: 'Unit Testing in Python'
visible: true
---

# A Brief Introduction to the Python unittest Module

 - **Authors**: Andre R. Erler
 - **Research field**: Atmospheric Physics
 - **Lesson topic**: Unit Testing (software development)
 - **Lesson content URL**: <https://github.com/UofTCoders/studyGroup/tree/gh-pages/lessons/unittest>

The [unittest](https://docs.python.org/2/library/unittest.html) module primarily provides a class TestCase to facilitate the writing of tests for "units" of code inside a larger project.
Larger software projects benefit from unit tests, because smaller units of the software can be tested individually and checked for errors before they are added to the main project. After a project has grown over time, a suite of unit tests can also be very helpful in debugging, because the source of an error can quickly be located.

Typically test cases are implemented as child classes of the `unittest.TestCase` class. The methods `TestCase.setUp()` can be overloaded to provide common setup procedures for all test methods; the method `TestCase.tearDown()` can be used for cleanup; both methods are executed before (after) each test. All methods of the form `TestCase.test*()` are considered test cases and will be executed by `unittest`, if `unittest.main()` is called. Alternatively, tests can be run using the `python -m unittest` command with the module name.

To run several tests suites at once, the command line utility `nosetests` (available in the separate `nose` package) can be used: it scans all Python scrips in the current directory and executes all available test cases.

The code used during the lesson is available in the [inclass](https://github.com/UofTCoders/studyGroup/tree/gh-pages/lessons/unittest/inclass) folder, the somewhat longer original material is available in the [original](https://github.com/UofTCoders/studyGroup/tree/gh-pages/lessons/unittest/original) folder.

An example of a more advanced use case, where individual test can be selected and inheritance between TestCase's is used, can be found [here](https://github.com/aerler/GeoPy/tree/master/src/geodata_test.py).