import marimo

__generated_with = "0.14.10"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---
        date: "2024-10-16T12:00:00.00Z"
        description: "Writing a Jupyter notebook to clean up my blog's article locations"
        published: true
        tags:
          - python
          - blog
        time_to_read: 2
        title: File Location Fixup
        type: post
        ---
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        For a long time I kept all my blog articles in one directory called "[posts](https://github.com/pydanny/daniel-blog-fasthtml/tree/main/posts)". However, as I have over 650 articles, this meant that the directory was unweildy. So I switched to a recursive glob to find all [markdown](https://github.com/pydanny/daniel-blog-fasthtml/blob/feef9f67fbf4ef4571953a163284fa90cd7a7066/main.py#L109) and [Jupyter](https://github.com/pydanny/daniel-blog-fasthtml/blob/feef9f67fbf4ef4571953a163284fa90cd7a7066/main.py#L95) files inside the "posts" directory. Now I can have nested folders.

        Some of my articles are in special directories called things like "til" and "course.fast.ai". However, the vast majority were destined to be placed in directories that matched the year in which they were written. So anything written in 2010 was moved to the 2010 directory, and anything written this year (2024) was placed in the 2024 directory. As many of my articles were prefixed with their year and month, I could easily do this manually with the `mv` shell command.

        Alas, about 150 articles didn't have a prefix. I started to open each file to examine their date then moved them one-by-one into their proper date folder. 

        I moved about 10-20 files this way before I remembered I know how to code. Indeed., I could do this in a few lines of Python (or any language - I chose Python here). So I created a Jupyter notebook and in minutes the move was done. You can see the [big commit here](https://github.com/pydanny/daniel-blog-fasthtml/commit/452f30147e339b2e363a7567034744c7b48598ba).

        This article is [that Jupyter notebook](https://github.com/pydanny/daniel-blog-fasthtml/blob/main/posts/2024/file-location-cleanup.ipynb). I've attached frontmatter and set it in the 2024 folder. Enjoy!
        """
    )
    return


@app.cell
def _():
    from pathlib import Path
    from yaml import safe_load
    return Path, safe_load


@app.cell
def _(Path, safe_load):
    for path in Path("posts").glob("*.md"):
        # Get the year from the frontmatter
        raw = path.read_text()
        metadata = safe_load(raw.split("---")[1])
        date = metadata["date"]
        year = date[:4]

        # Make the year directory in the posts directory
        # If it exists already, then don't throw an error
        Path(f"posts/{year}").mkdir(exist_ok=True)

        # Now move the file over
        path.rename(f"posts/{year}/{path.name}")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
