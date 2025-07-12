import marimo

__generated_with = "0.14.10"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---
        date: "2025-01-26T16:30:00.00Z"
        description: "When using Python to interact with file systems, Pathlib is where you should start."
        published: false
        tags:
          - python
          - howto
          - fastcore  
        time_to_read: 5
        title: "Pathlib is fun!"
        type: post
        ---
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Directory objects
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        First, we import the `Path` class from pathlib. The `Path` is 99.9% of what you'll ever need to use.
        """
    )
    return


@app.cell
def _():
    from pathlib import Path
    return (Path,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let's create a object representation of the directory in which this file resides:
        """
    )
    return


@app.cell
def _(Path):
    dir_path = Path(".")
    dir_path
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now on this blog post's file:
        """
    )
    return


@app.cell
def _(Path):
    blog_post = Path("2025-01-pathlib-is-fun.ipynb")
    blog_post
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let's create a new file:
        """
    )
    return


@app.cell
def _(Path):
    new_file = Path("blarg.md")
    new_file.exists()  # Not yet created
    return (new_file,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Create the file using the `touch` method. This creates a blank text file
        """
    )
    return


@app.cell
def _(new_file):
    new_file.touch()
    new_file.exists()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Coding Standard: PEP-8
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        With a few exceptions, Pathlib adheres to the [PEP-8 style guide](https://peps.python.org/pep-0008/). Following any styleguide eases discovery and reduces coding errors.

        Below is a table that shows some of the naming differences
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""

        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""

        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
