import marimo

__generated_with = "0.14.10"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---
        date: "2025-01-14T15:30:00.00Z"
        description: "Two libraries in Python's standard library that are useful for keeping load testing code all in one module."
        published: true
        tags:
          - python
          - TIL
          - load testing
        time_to_read: 2
        title: "TIL: Using inspect and timeit together"
        type: post
        ---
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        When working with `timeit` you either have to write code in string variables or load a seperate Python module as code. The former is a really not a good idea, the latter is ideal but annoying for quick tests. So I thought this up today, probably reinventing what someone else has done. 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        For an example let's define a simple function we want to test that generates a random 10 character string:
        """
    )
    return


@app.cell
def _():
    def get_random_string(length=10):
        from random import choice
        from string import ascii_letters

        return "".join(choice(ascii_letters) for _ in range(length))


    get_random_string()
    return (get_random_string,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        You'll notice that the imports are in the calling function. That makes the next step a bit easier. That's where we use `inspect.getsource()` to save the code of get_random_string to a variable called `setup_stmt`.
        """
    )
    return


@app.cell
def _(get_random_string):
    from inspect import getsource

    setup_stmt = getsource(get_random_string)
    print(setup_stmt)
    # The 'code' below is a printed string in a notebook cell, not actual code
    return (setup_stmt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Next step is we create a `code_stmt` variable that calls that function.
        """
    )
    return


@app.cell
def _():
    code_stmt = "get_random_string()"
    return (code_stmt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now we can plug that into a timeit module to see how fast it runs.
        """
    )
    return


@app.cell
def _(code_stmt, setup_stmt):
    from timeit import timeit

    timeit(stmt=code_stmt, setup=setup_stmt)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Again, the advantage of this approach is that it's all in one module and we can easily test that the function works before sticking it in timeout.
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
