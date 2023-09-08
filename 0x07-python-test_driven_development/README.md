This directory contains Python Programs 
concerned with concepts testing and edge cases.
The topics worked on are:
-What is an interactive test
	A test that you can run and interact with in real time,
	as opposed to static tests that just run and produce
	a pass/fail result.
-Why tests are important
	Catch bugs early
	Ensure code quality and reliability
	Facilitate refactoring
	Provide documentation
	Give confidence to change code
-How to write Docstrings to create tests
	Use triple quotes to create a docstring
	Explain what the test is checking
	Show example inputs and expected outputs
-How to write documentation for each module and function
	Use docstrings to document modules, classes, and functions
	Explain purpose, parameters, returns, etc.
-What are the basic option flags to run tests
	python -m unittest [options]
	Common options: -v (verbose), -b (buffer stdout/stderr), -f (fail fast)
-How to find edge cases
	Look for boundary conditions
	Consider invalid/extreme inputs
	Account for empty/full data sets
	Think of errors users might see
