import marimo

__generated_with = "0.14.10"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---
        date: "2025-03-14T21:30:00.00Z"
        description: "A really quick exploration of Pi in Python plus a call to action!"
        published: true
        tags:
          - python
          - blog
        time_to_read: 2
        title: "Pi Day"
        type: post
        ---
        """
    )
    return


@app.cell
def _():
    from math import pi
    return (pi,)


@app.cell
def _(pi):
    print(pi)
    return


@app.cell
def _(pi):
    print(pi**pi)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Don't forget to sign the petition to [nickname Python 3​.​14 to Pithon!](https://www.change.org/p/nickname-python-3-14-to-pithon)
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
