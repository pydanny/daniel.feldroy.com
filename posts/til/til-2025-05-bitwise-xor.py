import marimo

__generated_with = "0.14.10"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---
        date: '2025-05-07T03:30:43.170061'
        description: How to mark a comparison of booleans as True or False using bitwise XOR.
        image: /public/logos/til-1.png
        published: true
        tags:
        - TIL
        - python
        title: 'TIL: ^ bitwise XOR'
        twitter_image: /public/logos/til-1.png
        ---
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The bitwise XOR operator `^`, also known as `exclusive or`, can be used to compare boolean objects to see if one and only one is `True`. 

        Let's see it in action, first comparing three `False` booleans, which will return `False`.
        """
    )
    return


@app.cell
def _():
    False ^ False ^ False
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now let's demonstrate three different combinations of a single `True` and any number of `False` booleans, which will return `True` in each case.
        """
    )
    return


@app.cell
def _():
    print(True ^ False ^ False)
    print(False ^ True ^ False)
    print(False ^ False ^ True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        However, if we have two or more values that are `True`, the result will be `False` because more than one value are `True`. 
        """
    )
    return


@app.cell
def _():
    print(True ^ True ^ False)
    print(True ^ False ^ True)
    print(False ^ True ^ True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## What about non-boolean types?

        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The `^` operator only works with boolean types. If you try to use it on non-boolean types, you'll get a `TypeError`. For example, if you try to use it on integers or strings to check for truthiness, you'll get an error.
        """
    )
    return


@app.cell
def _():
    "" ^ "" ^ "one"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ```python
        -------------------------------------------------------------
        TypeError                   Traceback (most recent call last)
        Cell In[20], line 1
        ----> 1 '' ^ '' ^ 'one'

        TypeError: unsupported operand type(s) for ^: 'str' and 'str'
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To make this comparison works, you can convert the non-boolean types to boolean first. For example, you can use the `bool()` function to convert an integer or string to a boolean before using the `^` operator.
        """
    )
    return


@app.cell
def _():
    bool("") ^ bool("") ^ bool("one")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Updates

        - 2025-05-07: Updated the post to describe XOR only returns `True` if one (and only one) of the values is `True`. Removed the segment on `any()` as it is too far away in design from `XOR`.  Credit for this fix goes to [Curt Merrill](https://bsky.app/profile/cmerrill.com) and [Rens Dimmendaal](https://rensdimmendaal.com/).
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
