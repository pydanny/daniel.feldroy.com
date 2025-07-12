import marimo

__generated_with = "0.14.10"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---
        date: '2025-02-21T18:00:00.000000'
        description: Another reason to use functools.wraps!
        image: /public/logos/til-1.png
        published: true
        tags:
        - TIL
        - python
        title: 'TIL: Undecorating a functools.wraps decorated function'
        twitter_image: /public/logos/til-1.png
        ---
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In the Python standard library there is a function in the functools library that allows decorated functions to carry forward their original docstring. Executing it is rather easy:
        """
    )
    return


@app.cell
def _():
    from functools import wraps


    def kerpow(f):
        """Prints the string KERPOW!"""

        @wraps(f)
        def wrapper(*args, **kwds):
            print(f"KERPOW {f.__name__}!")
            return f(*args, **kwds)

        return wrapper
    return (kerpow,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let's try it out.
        """
    )
    return


@app.cell
def _(kerpow):
    @kerpow
    def adder(a, b):
        """Adds the arguments together"""
        return a + b
    return (adder,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let's call the function. What we should get in addition to the sum of the values passed is the printed value of "KERPOW" plus the name of the function.
        """
    )
    return


@app.cell
def _(adder):
    adder(1, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        As mentioned, the `functools.wraps` decorator preserves the docstring:
        """
    )
    return


@app.cell
def _(adder):
    adder.__doc__
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        As you can see, `functools.wraps` is an easy addition to any decorator that makes keeping documentation valid trivial to do.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        However, what if we want to use the `adder` function without printing "KERPOW adder!" to the terminal? In other words, can we remove the decorator?

        Fortunately, because we used `functools.wraps` we can do just that. You see, what `functools.wraps` does is add a `__wrapped__` attribute to the wrapped function. If we want to restore the function to the original we do this:
        """
    )
    return


@app.cell
def _(adder):
    adder_1 = adder.__wrapped__
    return (adder_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now if we call `adder`, we won't see "KERPOW adder!" any longer going to the terminal.
        """
    )
    return


@app.cell
def _(adder_1):
    adder_1(2, 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Postscript
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In a follow-up discussion about this TIL I learned that `functools.wraps` is syntactical sugar for the [functools.update_wrapper()](https://docs.python.org/3/library/functools.html#functools.update_wrapper) function. 
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
