import marimo

__generated_with = "0.14.10"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---
        date: "2025-01-01T19:30:00.00Z"
        description: "For the past six months or so I've been using fastcore. It provides two handy bunch-class style that I've leveraged into projects."
        published: false
        tags:
          - python
          - fastcore
          - bunch
        time_to_read: 2
        title: "Exploring fastcore bunch classes"
        type: post
        ---
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The fastcore library has a lot of really useful tools. As a fan of bunch classes, here's two useful utilities for working with them.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## AttrDict
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        `AttrDict` adds attributes to python `dict` without changing equality or how it prints.
        """
    )
    return


@app.cell
def _():
    from fastcore.basics import AttrDict
    return (AttrDict,)


@app.cell
def _(AttrDict):
    daughter = AttrDict(name="Uma", age=6)
    daughter
    return (daughter,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Equality is the same as a `dict`.
        """
    )
    return


@app.cell
def _(daughter):
    daughter == {"age": 6, "name": "Uma"}
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Values can be accessed either as `dict` or with `dot` notation.
        """
    )
    return


@app.cell
def _(daughter):
    daughter["name"]
    return


@app.cell
def _(daughter):
    daughter.name
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## NS

        `NS` extends `types.SimpleNamespace` (which I covered [here](/posts/til-2024-12-types-simplenamespace-is-a-bunch-class)), providing useful access functionality similar to that of `AttrDict`. Unlike `AttrDict`, equality is not that of a `dict` and is covered below.
        """
    )
    return


@app.cell
def _():
    from fastcore.basics import NS
    return (NS,)


@app.cell
def _(NS):
    daughter_1 = NS(name='Uma', age=6)
    return (daughter_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Equality of `NS` is with `types.SimpleNamespace`, which is the difference between it and `AttrDict`, whose equality is as a `dict` type.
        """
    )
    return


@app.cell
def _(daughter_1):
    import types
    daughter_1 == types.SimpleNamespace(name='Uma', age=6)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Values can be accessed either as `dict` or with `dot` notation.
        """
    )
    return


@app.cell
def _(daughter_1):
    daughter_1['name']
    return


@app.cell
def _(daughter_1):
    daughter_1.name
    return


@app.cell
def _(daughter_1):
    list(daughter_1)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
