import marimo

__generated_with = "0.14.10"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---
        date: "2024-12-25T02:00:00.00Z"
        description: "Did you know that Python's types library has a bunch class implementation? How did I not see this before?!"
        published: true
        tags:
          - python
          - TIL
          - bunch
        time_to_read: 2
        title: "TIL: types.SimpleNamespace is a Bunch class"
        type: post
        ---
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Early in my coding career I stumbling across the easy dot notations of bunch classes. I've created my own and even documented it a [two](/posts/2011-11-loving-bunch-class) [times](/posts/exploring-the-bunch-class). What I did not know until recently was the `types` library in core Python provides easy bunch class functionality. Credit to Jeremy Howard for schooling me on this one.
        """
    )
    return


@app.cell
def _():
    from types import SimpleNamespace as ns
    return (ns,)


@app.cell
def _(ns):
    daughter = ns(age=6, name="Uma")
    daughter
    return (daughter,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Accessing attributes
        """
    )
    return


@app.cell
def _(daughter):
    daughter.name
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Accessing all the data at once
        """
    )
    return


@app.cell
def _(daughter):
    daughter.__dict__
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Useful for tracking age over time! And in list comprehension (and by extension generator expressions).
        """
    )
    return


@app.cell
def _(ns):
    ages = [ns(age=i, name="Uma") for i in range(5, 10)]
    ages
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
