import air
import pathlib
from datetime import datetime


def Socials(title, description, image, twitter_image, url):
    return [
        air.Meta(property="og:image", content=image),
        air.Meta(property="og:site_name", content="https://daniel.feldroy.com"),
        air.Meta(property="og:image:type", content="image/png"),
        air.Meta(property="og:type", content="website"),
        air.Meta(property="og:url", content=url),
        air.Meta(property="og:title", content=title),
        air.Meta(property="og:description", content=description),
        air.Meta(name="twitter:image", content=twitter_image),
        air.Meta(name="twitter:card", content="summary"),
        air.Meta(name="twitter:title", content=title),
        air.Meta(name="twitter:description", content=description),
        air.Link(rel="canonical", href=url),
    ]
    return


def Layout(
    *children,
    title="Daniel Roy Greenfeld",
    description="Daniel Roy Greenfeld's personal blog",
    image="https://f004.backblazeb2.com/file/daniel-feldroy-com/public/images/profile.jpg",
    twitter_image="https://f004.backblazeb2.com/file/daniel-feldroy-com/public/images/profile.jpg",
    url="http://daniel.feldroy.com/",
    status_code=200,
) -> air.AirResponse:
    "Generic layout for pages"
    body_children = air.layouts.filter_body_tags(children)
    return air.AirResponse(
        air.Html(
            air.Head(
                *Socials(title, description, image, twitter_image, url),
                air.Link(
                    rel="stylesheet",
                    href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css",
                ),
                air.Script(
                    src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.6/dist/htmx.min.js",
                    integrity="sha384-Akqfrbj/HpNVo8k11SXBb6TlBWmXXlYQrCSqEWmyKJe+hDm3Z/B2WVG4smwBkRVm",
                    crossorigin="anonymous",
                ),
                air.Style(":root { --pico-font-size: 100%; }"),
                air.Link(
                    rel="stylesheet",
                    href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/styles/atom-one-dark.css",
                    media="(prefers-color-scheme: dark)",
                ),
                air.Link(
                    rel="stylesheet",
                    href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/styles/atom-one-light.css",
                    media="(prefers-color-scheme: light)",
                ),
                air.Script(
                    src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"
                ),
                air.Script(
                    src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/languages/python.min.js"
                ),
                air.Script(
                    src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/languages/javascript.min.js"
                ),
                air.Script(
                    src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/languages/html.min.js"
                ),
                air.Script(
                    src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/languages/css.min.js"
                ),
                air.Link(rel="stylesheet", href="/public/style.css", type="text/css"),
                *air.layouts.filter_head_tags(children),
            ),
            air.Body(
                air.Header(
                    air.A(
                        air.Img(
                            class_="borderCircle",
                            alt="Daniel Roy Greenfeld",
                            src="https://f004.backblazeb2.com/file/daniel-feldroy-com/public/images/profile.jpg",
                            width="108",
                            height="108",
                        ),
                        href="/",
                    ),
                    air.A(air.H2("Daniel Roy Greenfeld"), href="/"),
                    air.P(
                        air.A("About", href="/about"),
                        " | ",
                        air.A("Articles", href="/posts"),
                        " | ",
                        air.A("Open Source", href="/open-source"),
                        " | ",
                        air.A("Books", href="/books"),
                        " | ",
                        air.A("Tags", href="/tags"),
                        " | ",
                        air.A("Search", href="/search"),
                    ),
                    style="text-align: center;",
                ),
                air.Main(*air.layouts.filter_body_tags(children), class_="container"),
                air.Footer(
                    air.Hr(),
                    air.P(
                        air.A(
                            "LinkedIn",
                            href="https://www.linkedin.com/in/danielfeldroy/",
                            target="_blank",
                        ),
                        " | ",
                        air.A(
                            "Bluesky",
                            href="https://bsky.app/profile/daniel.feldroy.com",
                            target="_blank",
                        ),
                        " | ",
                        air.A(
                            "Twitter",
                            href="https://twitter.com/pydanny",
                            target="_blank",
                        ),
                        " | ",
                        air.A(
                            "Github", href="https://github.com/pydanny", target="_blank"
                        ),
                        " | ",
                        # air.A("Mailing list", href="/mailing-list"),
                        # " | ",
                        "Feeds: ",
                        air.A("All", href="/feeds/atom.xml", target="_blank"),
                        ", ",
                        air.A("Python", href="/feeds/python.atom.xml", target="_blank"),
                        ", ",
                        air.A("TIL", href="/feeds/til.atom.xml", target="_blank"),
                    ),
                    air.P(
                        f"All rights reserved {datetime.now().year}, Daniel Roy Greenfeld"
                    ),
                    class_="container",
                ),
                air.Dialog(
                    air.Header(
                        air.H2("Search"),
                        air.Input(
                            name="q",
                            type="text",
                            id="search-input",
                            hx_trigger="keyup",
                            placeholder="Enter your search query...",
                            hx_get="/search-results",
                            hx_target=".search-results-modal",
                        ),
                        air.Div(class_="search-results-modal"),
                        class_="modal-content",
                    ),
                    id="search-modal",
                    style="display:none;",
                    class_="modal overflow-auto",
                ),
                air.Div(hx_trigger="keyup[key=='/'] from:body"),
                air.Script("""
            document.body.addEventListener('keydown', e => {
            if (e.key === '/') {
                e.preventDefault();
                document.getElementById('search-modal').style.display = 'block';
                document.getElementById('search-input').focus();
            }
            if (e.key === 'Escape') {
                document.getElementById('search-modal').style.display = 'none';
            }
            });

            document.getElementById('search-input').addEventListener('input', e => {
            htmx.trigger('.search-results', 'htmx:trigger', {value: e.target.value});
            });
            """),
                hx_boost="true",
            ),
        ).render(),
        status_code=status_code,
    )
