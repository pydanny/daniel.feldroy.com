import marimo

__generated_with = "0.14.9"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""# Hello, world""")
    return


@app.function
def randomizer():
    from random import randint

    return randint(1, 20)


@app.cell
def _():
    value = randomizer()
    return (value,)


@app.cell
def _(value):
    value
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
