---
date: '2026-05-04T11:55:23.590783+00:00'
description: For when I want a word count that ignores Markdown symbols
published: true
tags:
- python
- writing
title: Word counter that ignores Markdown
---

I've been doing a lot of writing recently, and tracking my word count. I write in markdown. I could just render the text using a markdown library and then do a count on the generated output, but then I wouldn't have the fun of writing out a bunch of regular expressions. Yes, I know the cautionary meme by that says:

> "Some people, when confronted with a problem, think ‘I know, I’ll use regular expressions.’ Now they have two problems."
> -- Jamie Zawinski

I don't care.

I love working in regular expressions. It was the one thing I got out of my brief foray in Perl at the very start of my software development career. I carried it into my Java and ColdFusion days and periodically used it in Python. Noodling with getting a regular expression just right is a very fun puzzle for me.

So here you go, a Python-powered word counter powered by my desire to noodle with regular expressions:

```python
#!/usr/bin/env python3
"""
word_count.py — Count words in a Markdown file or a directory of markdown files.

Dependencies:
    typer
    rich

Usage:
    python word_count.py README.md
    python word_count.py README.md --no-strip-markdown
    python word_count.py README.md --verbose
    python word_count.py book/
"""

import re
from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

app = typer.Typer(
    name="word-count",
    help="Count words in Markdown files.",
    add_completion=False,
)
console = Console()


MARKDOWN_PATTERNS = [
    r"```[\s\S]*?```",  # fenced code blocks
    r"`[^`]+`",  # inline code
    r"!\[.*?\]\(.*?\)",  # images
    r"\[.*?\]\(.*?\)",  # links => keep link text
    r"^#{1,6}\s+",  # ATX headings
    r"^\s*[-*+]\s+",  # unordered list markers
    r"^\s*\d+\.\s+",  # ordered list markers
    r"[*_]{1,2}([^*_]+)[*_]{1,2}",  # bold / italic => keep inner text
    r"~~([^~]+)~~",  # strikethrough => keep inner text
    r"^>+\s*",  # blockquote markers
    r"^\s*\|.*\|\s*$",  # table rows (kept as-is, words counted)
    r"^[-*_]{3,}\s*$",  # horizontal rules
    r"<!--[\s\S]*?-->",  # HTML comments
    r"<[^>]+>",  # remaining HTML tags
]

_STRIP_RE = re.compile("|".join(MARKDOWN_PATTERNS), re.MULTILINE)


def strip_markdown(text: str) -> str:
    """Remove Markdown syntax, keeping readable prose."""
    # Replace links/images with their label text
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
    # Remove fenced code blocks entirely
    text = re.sub(r"```[\s\S]*?```", "", text)
    # Remove inline code
    text = re.sub(r"`[^`]+`", "", text)
    # Unwrap bold / italic
    text = re.sub(r"[*_]{1,2}([^*_\n]+)[*_]{1,2}", r"\1", text)
    text = re.sub(r"~~([^~]+)~~", r"\1", text)
    # Remove HTML comments and tags
    text = re.sub(r"<!--[\s\S]*?-->", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    # Strip leading syntax characters
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^>+\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)
    return text


def count_stats(text: str) -> dict:
    words = text.split()
    lines = text.splitlines()
    chars_no_space = len(re.sub(r"\s", "", text))
    sentences = len(re.findall(r"[.!?]+", text))
    return {
        "words": len(words),
        "lines": len(lines),
        "chars": len(text),
        "chars_no_space": chars_no_space,
        "sentences": max(sentences, 1),
        "avg_word_len": (
            round(sum(len(w) for w in words) / len(words), 1) if words else 0.0
        ),
        "reading_time_min": max(1, round(len(words) / 200)),  # ~200 wpm
    }


def _count_single_file(
    file: Path,
    strip: bool,
    verbose: bool,
    plain: bool,
) -> dict:
    """Count words for a single file, print output, and return stats."""
    raw = file.read_text(encoding="utf-8")
    text = strip_markdown(raw) if strip else raw
    stats = count_stats(text)

    if plain:
        typer.echo(f"{file.name}\t{stats['words']}")
        return stats

    if not verbose:
        console.print(
            Panel(
                f"[bold cyan]{stats['words']:,}[/bold cyan] words  ·  "
                f"[dim]{stats['reading_time_min']} min read[/dim]",
                title=f"[bold]{file.name}[/bold]",
                border_style="cyan",
            )
        )
        return stats

    # Verbose: full table
    table = Table(box=box.ROUNDED, show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="bold")
    table.add_column("Value", justify="right")

    rows = [
        ("Words", f"{stats['words']:,}"),
        ("Lines", f"{stats['lines']:,}"),
        ("Characters (with spaces)", f"{stats['chars']:,}"),
        ("Characters (no spaces)", f"{stats['chars_no_space']:,}"),
        ("Sentences (approx.)", f"{stats['sentences']:,}"),
        ("Avg word length", f"{stats['avg_word_len']} chars"),
        ("Estimated reading time", f"{stats['reading_time_min']} min"),
        ("Markdown stripped", "yes" if strip else "no"),
    ]
    for label, value in rows:
        table.add_row(label, value)

    console.print()
    console.print(f"  [bold]{file}[/bold]", style="dim")
    console.print(table)
    console.print()
    return stats


@app.command()
def count(
    path: Path = typer.Argument(
        ...,
        help="Path to a Markdown file or a directory with digit-prefixed .md files.",
        exists=True,
        file_okay=True,
        dir_okay=True,
        readable=True,
    ),
    strip: bool = typer.Option(
        True,
        "--strip-markdown/--no-strip-markdown",
        help="Strip Markdown syntax before counting (default: True).",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Show a full breakdown table.",
    ),
    plain: bool = typer.Option(
        False,
        "--plain",
        help="Print a bare number (word count only) — useful for scripting.",
    ),
):
    """Count words in a Markdown FILE or all digit-prefixed .md files in a directory."""
    if path.is_file():
        _count_single_file(path, strip, verbose, plain)
        return

    # Directory mode: find .md files starting with a digit
    files = sorted(f for f in path.glob("[0-9]*.md") if f.is_file())
    if not files:
        console.print(f"[red]No digit-prefixed .md files found in {path}[/red]")
        raise typer.Exit(code=1)

    total_words = 0
    for f in files:
        stats = _count_single_file(f, strip, verbose, plain)
        total_words += stats["words"]

    if plain:
        typer.echo(f"TOTAL\t{total_words}")
    else:
        console.print(
            Panel(
                f"[bold green]{total_words:,}[/bold green] words across "
                f"[bold]{len(files)}[/bold] files  ·  "
                f"[dim]{max(1, round(total_words / 200))} min read[/dim]",
                title=f"[bold]{path}[/bold] — Total",
                border_style="green",
            )
        )


if __name__ == "__main__":
    app()
```