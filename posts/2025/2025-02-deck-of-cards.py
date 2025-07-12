import marimo

__generated_with = "0.14.10"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
          ---
        date: "2025-02-14T10:00:00.00Z"
        description: "Today is Valentine's Day. That makes it the perfect day to write a blog post about showing how to not just build a deck of cards, but show off cards from the heart suite."
        published: true
        tags:
          - python
          - fastcore
          - howto
        time_to_read: 5
        title: "Building a playing card deck"
        type: post
        ---
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        After trying out Belatro I found [Richard Schneider's venerable CardJS library](https://github.com/richardschneider/cardsJS). This notebook builds a playing card deck using the SVGs from that project. Python dependencies for this notebook:

        - rich
        - python-fasthtml
        """
    )
    return


@app.cell
def _():
    import pathlib
    from fastcore.basics import AttrDict, store_attr
    from fastcore.utils import L
    from fasthtml.common import show, NotStr
    from rich import print
    return AttrDict, L, NotStr, pathlib, print, show, store_attr


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Since we're making a deck of playing cards, let's create a Card class which can be used for handling both attributes and display of cards.
        """
    )
    return


@app.cell
def _(NotStr, pathlib, print, store_attr):
    class Card:
        def __init__(self, id, title, suite, value, order, loc):
            store_attr("id,title,suite,value,order,loc", self)
            self.img = pathlib.Path(loc).read_text()

        def __repr__(self):
            return f"<{self.title}>"

        def show(self):
            show(NotStr(self.img))


    card = Card("02H", "Two of Hearts", "heart", 2, 2, "cards/02H.svg")
    print(card)
    return Card, card


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In the above cell, we create a two of hearts. Now let's display the result to the screen. 
        """
    )
    return


@app.cell
def _(card):
    card.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Building the deck
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let's make 52 cards. Rather than hardcode out all of the cards themselves, we're going to loop through the directory of card images and then do a little bit of mapping to create a 52-card playing deck. 
        """
    )
    return


@app.cell
def _():
    number_map = {
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
    }
    return (number_map,)


@app.cell
def _(number_map):
    def get_number(name):
        for k, v in number_map.items():
            if str(k) in name:
                return k, v
    return (get_number,)


@app.cell
def _(AttrDict):
    suite_map = {
        "C": AttrDict(title="number of Clubs", suite="clubs"),
        "D": AttrDict(title="number of Diamonds", suite="diamonds"),
        "H": AttrDict(title="number of Hearts", suite="hearts"),
        "S": AttrDict(title="number of Spades", suite="spades"),
    }
    return (suite_map,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The base deck is unordered because that's how `pathlib.Path.glob()` seems to work. 
        """
    )
    return


@app.cell
def _():
    base_deck = {}
    return (base_deck,)


@app.cell
def _(Card, L, base_deck, get_number, pathlib, print, suite_map):
    _filez = L(pathlib.Path('cards').glob('*.svg')).filter(lambda x: 'BACK' not in str(x)).filter(lambda x: str(x.name)[0].isdigit())
    for _fil in _filez:
        integer, number = get_number(_fil.name)
        _suite = str(_fil.name[2])
        _ident = _fil.name.replace('.svg', '')
        _tmpl = suite_map[_suite]
        card_1 = Card(id=_ident, title=_tmpl.title.replace('number', number), suite=_tmpl.suite, value=integer, order=integer, loc=str(_fil))
        base_deck[_ident] = card_1
    print(base_deck)
    return


@app.cell
def _(AttrDict):
    face_map = {
        "A": AttrDict(title="Ace", value=11, order=14),
        "K": AttrDict(title="King", value=10, order=13),
        "Q": AttrDict(title="Queen", value=10, order=12),
        "J": AttrDict(title="Jack", value=10, order=11),
    }
    return (face_map,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Time for the face cards!
        """
    )
    return


@app.cell
def _(Card, L, base_deck, face_map, pathlib, print, suite_map):
    _filez = L(pathlib.Path('cards').glob('*.svg')).filter(lambda x: 'BACK' not in str(x)).filter(lambda x: str(x.name)[0].isdigit() is False)
    for _fil in _filez:
        _ident = _fil.name.replace('.svg', '')
        _suite = str(_fil.name[2])
        faced = face_map[str(_fil.name[1])]
        _tmpl = suite_map[_suite]
        card_2 = Card(id=_ident, title=_tmpl.title.replace('number', faced.title), suite=_tmpl.suite, value=faced.value, order=faced.order, loc=str(_fil))
        base_deck[_ident] = card_2
    print(base_deck)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Sorting the deck
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now that we have a deck with 52 cards, let's sort it.
        """
    )
    return


@app.cell
def _(L, base_deck, print):
    deck = {}
    for card_3 in L(base_deck.values()).sorted('order'):
        deck[card_3.id] = card_3
    print(deck)
    return (deck,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Displaying card faces
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In the cells below, you my expiraments to figure out how to display the cards so the cards are displayed. These lines of code happen after the display of the two of hearts closer to the top but were written first. After I got them working here I went back to the `Card` class and added the `show()` method.
        """
    )
    return


@app.cell
def _(NotStr, deck, show):
    show(NotStr(deck["FJH"].img))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let's put that in the `Card.show()` method, which you can see in action below.
        """
    )
    return


@app.cell
def _(deck):
    deck["FJH"].show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Attribution
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        I want to give special thanks to:

        - Audrey Roy-Greenfeld for building a life with me and showing me how to use the filter method on the `fastcore.L` object
        - Isaac Flath For helping me figure out how to get the cards faces to display on my blog
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
