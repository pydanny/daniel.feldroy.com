"""
Name: md_testrunner.py
Usage: python md_test_runner.py blogpost.md
Tested on: Python 10
"""

import pathlib
import re
import subprocess
import sys


try:
    from rich import print
    import pytest  # noqa: F401
except ImportError:
    print("Please install rich: pip install rich pytest")
    sys.exit(1)

open_pattern = re.compile("\s*`{3}\s*python")
close_pattern = re.compile("\s*`{3}")
test_filename = "testfile.py"


def main(path: pathlib.Path):
    # Create an array of the Python code called "code"
    code = []
    in_python = False

    # Read the file line by line
    text = path.read_text()
    
    for line in text.splitlines():
        if re.match(open_pattern, line) is not None:
            in_python = True
            continue
        if in_python == True and re.match(close_pattern, line):
            in_python = False
        if in_python == True:
            code.append(line)

    # Save the code as a string to the testfile
    # `tempfile.NamedTempFile` fails here because the `write()` doesn't seem to occur
    # until the `with` statement is finished. I would love to be wrong in that, using
    # a tempfile is the cleaner approach. Please let me know a better approach.
    test_filepath = pathlib.Path(test_filename)
    test_filepath.write_text("\n".join(code))

    # Run the code
    cmd = ["pytest", test_filename]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = proc.communicate()

    # Display the results
    print("Output: " + output.decode("ascii"))
    print("Error: " + error.decode("ascii"))
    print("Code: " + str(proc.returncode))

    # Cleanup
    test_filepath.unlink()


if __name__ == "__main__":
    path = pathlib.Path(sys.argv[1])
    main(path)