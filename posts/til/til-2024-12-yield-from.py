import marimo

__generated_with = "0.14.10"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---
        date: "2024-12-27T23:15:00.00Z"
        description: "A variant of the yield statement that can result in more concise code."
        published: true
        tags:
          - python
          - TIL
        time_to_read: 2
        title: "TIL: yield from"
        type: post
        ---
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Lets create a function that uses yield to deliver a generator.
        """
    )
    return


@app.cell
def _():
    def row_fetcher(rows=5):
        for _x in range(rows):
            yield _x
    row_fetcher()
    return (row_fetcher,)


@app.cell
def _(row_fetcher):
    _cursor = row_fetcher()
    print(next(_cursor))
    for _x in _cursor:
        print(_x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        That works, but we can use `yield from` to make things more concise. Like the result of `row_fetcher()`, it it converts the function into a generator expression.
        """
    )
    return


@app.cell
def _():
    def row_fetcher2(rows=5):
        yield from range(rows)


    row_fetcher2()
    return (row_fetcher2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The behavior is identical to a regular `yield`, just the [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar) of `yield from` delivers more concise code.
        """
    )
    return


@app.cell
def _(row_fetcher2):
    _cursor = row_fetcher2()
    print(next(_cursor))
    for _x in _cursor:
        print(_x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Thanks to Jeremy Howard for suggesting `yield from` in a pull request that prompted me to finally look it up.
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
