import marimo

__generated_with = "0.13.10"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path
    import subprocess

    return Path, subprocess


@app.cell
def _(Path, subprocess):
    def list_files():
        changed = []
        for path in Path(".").glob("**/*.ipynb"):
            marimo_path = Path(f"{path.parent}/{path.stem}.py")
            md_path = f"{path.parent}/{path.stem}.md"
            if marimo_path.exists():
                marimo_path.unlink()
            cmd = f"marimo convert {path} -o {marimo_path}"
            subprocess.run(
                ["marimo", "convert", str(path), "-o", str(marimo_path)],
                capture_output=True,
                text=True,
            )
            print(cmd)
            cmd = f"marimo export md {marimo_path} -o {md_path}"
            subprocess.run(
                ["marimo", "export", "md", str(marimo_path), "-o", str(md_path)],
                capture_output=True,
                text=True,
            )
            print(cmd)
            changed.append(md_path)
            path.unlink()
            if marimo_path.exists():
                marimo_path.unlink()
        print("-" * 20)
        for p in changed:
            print(p)

    return (list_files,)


@app.cell
def _(list_files):
    list_files()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
