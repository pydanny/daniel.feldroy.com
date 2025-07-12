import marimo

__generated_with = "0.14.10"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---
        date: '2024-09-23T15:13:34.609190'
        description: A simple websockets example hosted in a Jupyter notebook!
        image: /public/logos/til-1.png
        published: true
        tags:
        - TIL
        - FastHTML
        - python
        - jupyter
        title: 'TIL: Using FastHTML in Jupyter notebooks plus websockets'
        twitter_image: /public/logos/til-1.png
        ---
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Websockets in Jupyter
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        A simple websockets example hosted in a Jupyter notebook! Check it out! 

        Use at least FastHTML 0.6.5. This code is heavily inspired by this [code](https://docs.fastht.ml/tutorials/by_example.html#websockets) written by Jeremy Howard.
        """
    )
    return


app._unparsable_cell(
    r"""
    # import necessary pieces
    from fasthtml.common import *
    from asyncio import sleep

    # Might be merged into fasthtml.common
    from fasthtml.jupyter import *
    """,
    name="_"
)


@app.cell
def _(Input):
    def mk_inp():
        return Input(id="msg")
    return (mk_inp,)


@app.cell
def _(FastJupy):
    # FastJupy() is a wrapper around the FastHTML() class
    # ws_hdr brings in the websocket headers
    app = FastJupy(ws_hdr=True)
    rt = app.route
    return app, rt


@app.cell
def _(Div, Form, Titled, mk_inp, rt):
    @rt("/")
    async def get(request):
        cts = Div(
            Div(id="notifications"),
            Form(mk_inp(), id="form", ws_send=True),
            hx_ext="ws",
            ws_connect="/ws",
        )
        return Titled("Websocket Test", cts)
    return


@app.cell
def _(Div):
    async def on_connect(send):
        print("Connected!")
        await send(Div("Hello, you have connected", id="notifications"))


    async def on_disconnect(ws):
        print("Disconnected!")
    return on_connect, on_disconnect


@app.cell
def _(Div, app, mk_inp, on_connect, on_disconnect, sleep):
    @app.ws("/ws", conn=on_connect, disconn=on_disconnect)
    async def ws(msg: str, send):
        await send(Div("Hello " + msg, id="notifications"))
        await sleep(2)
        return Div("Goodbye " + msg, id="notifications"), mk_inp()
    return


@app.cell
def _(JupyUvi, app):
    port = 8000
    server = JupyUvi(app, port=port)
    return (server,)


@app.cell
def _(HTMX):
    HTMX()
    return


@app.cell
def _(server):
    # Run me if you want to gracefully stop the HTTP server
    # without restarting Jupyter
    server.stop()
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
