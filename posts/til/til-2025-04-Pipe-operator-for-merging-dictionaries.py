import marimo

__generated_with = "0.14.10"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---
        date: '2025-04-27T19:05:35.433062'
        description: In Python 3.9 and later, the pipe operator | can be used to merge dictionaries.
        image: /public/logos/til-1.png
        published: true
        tags:
        - TIL
        - python
        title: 'TIL: Pipe operator for merging dictionaries'
        twitter_image: /public/logos/til-1.png
        ---
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Pipe `|` returns a new dictionary containing the key-value pairs from both operands. 
        """
    )
    return


@app.cell
def _():
    a = {'a': 1, 'b': 2}
    b = {'c': 3, 'd': 4}
    _merged = a | b
    print(a)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If there are duplicate keys, the value from the right-hand operand will overwrite  the value from the left-hand operand.
        """
    )
    return


@app.cell
def _():
    left = {'a': 1, 'b': 2}
    right = {'a': 3, 'b': 4}
    _merged = left | right
    print(_merged)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The `|=` is related, updating the left-hand operand in place much like the `+=` operator.
        """
    )
    return


@app.cell
def _():
    original = {"a": 1, "b": 2}
    new = {"b": 3, "c": 4}
    original |= new  # Analogous to original.update(new)
    print(original)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
